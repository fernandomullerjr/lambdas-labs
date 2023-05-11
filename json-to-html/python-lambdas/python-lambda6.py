import boto3
import locale
from datetime import datetime
import json
from jinja2 import Template

def gerar_relatorio(event, context):
    inspector2 = boto3.client('inspector2')
    s3 = boto3.client('s3')
    sns = boto3.client('sns')
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')  # Define a localização para o Brasil
    timestamp = datetime.now().strftime('%Y_%m___%d-%m-%Y-%H-%M-%S')  # Obtém a data e hora atual e formata no padrão brasileiro, adiciona ano e mes no começo, apenas para ordenar.
    # OBS: Timezone é americano.
    key_prefix = f'amazon-inspector/{timestamp}/'  # Adiciona o timestamp ao keyPrefix
    response = inspector2.create_findings_report(
        filterCriteria={
            'resourceTags': [
                        {
                            'comparison': 'EQUALS',
                            'key': 'DevOpsRelatorioAmazonInspector',
                            'value': '1'
                        }
                    ]
        },
        reportFormat='JSON',
        s3Destination={
            'bucketName': 'devops-luxor',
            'keyPrefix': key_prefix,
            'kmsKeyArn': 'arn:aws:kms:sa-east-1:574635504822:key/1976dff8-ac85-4e37-9400-ab0a4513f790'
        }
    )
    # Extrai o reportId da resposta e faz o print
    report_id = response['reportId']
    print(f"Report ID: {report_id}")
    
    
    # Lê o arquivo JSON gerado pelo Amazon Inspector
    bucket_name = 'devops-luxor'
    json_key = f'{key_prefix}{report_id}.json'
    json_object = s3.get_object(Bucket=bucket_name, Key=json_key)
    json_content = json_object['Body'].read().decode('utf-8')
    # Converte o conteúdo do arquivo JSON para o formato HTML
    html_key = f'{key_prefix}report.html'
    template = Template('''
    <html>
        <head>
            <title>Relatório do Amazon Inspector</title>
        </head>
        <body>
            <h1>Relatório do Amazon Inspector</h1>
            <h2>Report ID: {{ report_id }}</h2>
            <h2>Timestamp: {{ timestamp }}</h2>
            <p>{{ json_content }}</p>
        </body>
    ''')

    # Cria o objeto de resposta
    response_dict = {
        'statusCode': 200,
        'body': {
            'report_id': report_id,
            'timestamp': timestamp,
            'template': template,
            'message': f'Relatório gerado com sucesso. Report ID: {report_id}'
        }
    }

    return response_dict
#    html_content = gerar_html(json_content)
#    html_key = f'{key_prefix}{report_id}.html'

#    s3.put_object(Body=html_content, Bucket=bucket_name, Key=html_key)