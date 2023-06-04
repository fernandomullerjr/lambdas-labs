
import boto3
import json
import pandas as pd
from weasyprint import HTML

s3 = boto3.client('s3')

def read_json_from_s3(bucket, key):
    response = s3.get_object(Bucket=bucket, Key=key)
    json_data = response['Body'].read().decode('utf-8')
    return json.loads(json_data)

def convert_json_to_html(json_data):
    df = pd.DataFrame.from_dict(json_data)
    html = df.to_html(index=False)
    return html

def convert_html_to_pdf(html):
    pdf_bytes = HTML(string=html).write_pdf()
    return pdf_bytes

def upload_pdf_to_s3(bucket, key, pdf_bytes):
    s3.put_object(Body=pdf_bytes, Bucket=bucket, Key=key)

def lambda_handler(event, context):
    # Define o bucket do S3 e o caminho do arquivo JSON
    bucket = 'devops-luxor'
    json_key = 'base1.json'

    # Lê o arquivo JSON do S3
    json_data = read_json_from_s3(bucket, json_key)

    # Converte o JSON para HTML utilizando o pandas
    html = convert_json_to_html(json_data)

    # Converte o HTML para PDF utilizando o weasyprint
    pdf_bytes = convert_html_to_pdf(html)

    # Define o nome do arquivo PDF convertido
    pdf_key = 'relatorio-final-pandas.pdf'

    # Envia o PDF convertido para o S3
    upload_pdf_to_s3(bucket, pdf_key, pdf_bytes)