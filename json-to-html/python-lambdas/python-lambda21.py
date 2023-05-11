import boto3
import locale
import json
from datetime import datetime

def gerar_relatorio(event, context):
    inspector2 = boto3.client('inspector2')
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')  # Define a localização para o Brasil
    timestamp = datetime.now().strftime('%Y_%m___%d-%m-%Y-%H-%M-%S')  # Obtém a data e hora atual e formata no padrão brasileiro, adiciona ano e mes no começo, apenas para ordenar.
    # OBS: Timezone é americano.
    key_prefix = f'amazon-inspector/{timestamp}/'  # Adiciona o timestamp ao keyPrefix
    bucket_name = 'devops-luxor'
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
            'bucketName': bucket_name,
            'keyPrefix': key_prefix,
            'kmsKeyArn': 'arn:aws:kms:sa-east-1:574635504822:key/1976dff8-ac85-4e37-9400-ab0a4513f790'
        }
    )
    # Extrai o reportId da resposta e faz o print
    report_id = response['reportId']
    print(f"Report ID: {report_id}")

    # TESTANDO o print do prefixo inteiro
    json_key = f'{key_prefix}{report_id}.json'

    # S3, obtendo
    s3 = boto3.client('s3', region_name='sa-east-1')
    bucket_name = bucket_name
    json_object = s3.get_object(Bucket='devops-luxor', Key='amazon-inspector/2023_05___05-05-2023-14-52-13/6bc8a3e8-0277-4ccf-a2f3-19957b6fa734.json')
    json_content = json_object['Body'].read().decode('utf-8')

    # Converte o JSON para um dicionário Python
    report_dict = json.loads(json_content)

    # Gera o HTML a partir do dicionário Python
    html_content = f'''
        <html>
            <head>
                <title>Relatório do Amazon Inspector</title>
            </head>
            <body>
                <h1>Relatório do Amazon Inspector</h1>
                <p>Report ID: {report_id}</p>
                <p>Timestamp: {timestamp}</p>
                <h2>Findings</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Finding</th>
                            <th>Severity</th>
                            <th>Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        {"".join(["<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(escape(finding["id"]), escape(finding["severity"]), escape(finding["description"])) for finding in report_dict["findings"]])}
                    </tbody>
                </table>
            </body>
        </html>
    '''
    
    # Salva o HTML gerado no S3
    html_key = f'amazon-inspector/2023_05___05-05-2023-14-52-13/convertido.html'
    s3.put_object(Bucket='devops-luxor', Key=html_key, Body=html_content, ContentType='text/html')

    # Cria o objeto de resposta
    response_dict = {
        'statusCode': 200,
        'body': {
            'report_id': report_id,
            'timestamp': timestamp,
            'json_key': json_key,
            'json_content': json_content,
            'html_content': html_content,
            'message': f'Relatório gerado com sucesso. Report ID: {report_id}'
        }
    }
    
    # Retorna o objeto de resposta como uma string JSON
    return response_dict