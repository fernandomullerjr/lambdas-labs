import boto3
import locale
from datetime import datetime
import json

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
    json_key = f'{key_prefix}{report_id}.json'
    json_content = read_json_from_s3('devops-luxor', json_key)

    # Converte o conteúdo do arquivo JSON para o formato HTML
    html_key = f'{key_prefix}report.html'
    html_content = generate_html(json_content, report_id, timestamp)
    save_to_s3(html_content, 'devops-luxor', html_key)

    # Cria o objeto de resposta
    response_dict = {
        'statusCode': 200,
        'body': {
            'report_id': report_id,
            'timestamp': timestamp,
            'html_template': html_content,
            'message': f'Relatório gerado com sucesso. Report ID: {report_id}'
        }
    }

    return response_dict

def read_json_from_s3(bucket_name, json_key):
    s3 = boto3.client('s3')
    json_object = s3.get_object(Bucket=bucket_name, Key=json_key)
    json_content = json_object['Body'].read().decode('utf-8')
    return json_content

def generate_html(json_content, report_id, timestamp):
    html_template = '''
    <html>
        <head>
            <title>Relatório do Amazon Inspector</title>
        </head>
        <body>
            <h1>Relatório do Amazon Inspector</h1>
            <h2>Report ID: {report_id}</h2>
            <h2>Timestamp: {timestamp}</h2>
            <p>{json_content}</p>
        </body>
    </html>
    '''

    html_content = html_template.format(report_id=report_id, timestamp=timestamp, json_content=json_content)
    return html_content

def save_to_s3(content, bucket_name, key):
    s3 = boto3.client('s3')
    s3.put_object(Body=content, Bucket=bucket_name, Key=key)
