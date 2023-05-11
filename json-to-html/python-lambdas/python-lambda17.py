import boto3
import locale
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
    json_object = s3.get_object(Bucket='devops-luxor', Key='amazon-inspector/2023_05___05-05-2023-23-48-55/c7974469-dd40-4c19-8aae-ea296eb3093d.json')
    json_content = json_object['Body'].read().decode('utf-8')

#    s3 = boto3.resource('s3', region_name='sa-east-1')
#    bucket = s3.Bucket('devops-luxor')
#    object_key = 'amazon-inspector/2023_05___05-05-2023-23-48-55/c7974469-dd40-4c19-8aae-ea296eb3093d.json'
#    object_data = bucket.Object(object_key).get()['Body'].read()

    # Cria o objeto de resposta
    response_dict = {
        'statusCode': 200,
        'body': {
            'report_id': report_id,
            'timestamp': timestamp,
            'json_key': json_key,
            'json_content': json_content,
#            'object_data': object_data,
            'message': f'Relatório gerado com sucesso. Report ID: {report_id}'
        }
    }
    
    # Retorna o objeto de resposta como uma string JSON
    return response_dict