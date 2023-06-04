import boto3
import json
import pandas as pd
import pdfkit

s3 = boto3.client('s3')

def read_json_from_s3(bucket, key):
    response = s3.get_object(Bucket=bucket, Key=key)
    json_data = response['Body'].read().decode('utf-8')
    return json.loads(json_data)

def convert_json_to_pdf(json_data):
    df = pd.DataFrame.from_dict(json_data)
    html = df.to_html(index=False)
    pdfkit.from_string(html, '/tmp/relatorio.pdf')

def upload_pdf_to_s3(bucket, key):
    s3.upload_file('/tmp/relatorio.pdf', bucket, key)

def lambda_handler(event, context):
    # Define o bucket do S3 e o caminho do arquivo JSON
    bucket = 'devops-luxor'
    json_key = 'base1.json'

    # Lê o arquivo JSON do S3
    json_data = read_json_from_s3(bucket, json_key)

    # Converte o JSON para PDF utilizando o pandas
    convert_json_to_pdf(json_data)

    # Define o nome do arquivo PDF convertido
    pdf_key = 'relatorio-final-pdf.pdf'

    # Envia o PDF convertido para o S3
    upload_pdf_to_s3(bucket, pdf_key)