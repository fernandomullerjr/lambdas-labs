import boto3
import locale
from datetime import datetime

def gerar_relatorio(event, context):
    inspector2 = boto3.client('inspector2')
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

    # TESTANDO o print do prefixo inteiro
    json_key = f'{key_prefix}{report_id}.json'
    
    # Cria o objeto de resposta
    response_dict = {
        'statusCode': 200,
        'body': {
            'report_id': report_id,
            'timestamp': timestamp,
            'json_key': json_key,
            'message': f'Relatório gerado com sucesso. Report ID: {report_id}'
        }
    }
    
    # Retorna o objeto de resposta como uma string JSON
    return response_dict