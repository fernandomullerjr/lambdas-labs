
import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'devops-luxor'
    object_name = 'base1.json'
    
    try:
        response = s3.get_object(Bucket=bucket_name, Key=object_name)
        content = response['Body'].read()
        
        # Chamar a função que converte o JSON para HTML
        html_content = json_to_html(content)
        
        # Chamar a função que envia o arquivo HTML para o bucket S3
        put_html_to_s3(html_content)
        
        return {
            'statusCode': 200,
            'body': json.dumps({'content': content.decode('utf-8')})
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

def json_to_html(json_content):
    # Implementar a conversão de JSON para HTML aqui
    return html_content

def put_html_to_s3(html_content):
    s3 = boto3.resource('s3')
    bucket_name = 'devops-luxor'
    object_name = 'relatorio-final.html'
    
    try:
        s3.Bucket(bucket_name).put_object(Key=object_name, Body=html_content)
        print("Arquivo HTML salvo com sucesso!")
    except Exception as e:
        print(e)