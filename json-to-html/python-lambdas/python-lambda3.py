
import boto3

def gerar_relatorio(event, context):
    inspector2 = boto3.client('inspector2')
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
            'keyPrefix': 'amazon-inspector/',
            'kmsKeyArn': 'arn:aws:kms:sa-east-1:574635504822:key/1976dff8-ac85-4e37-9400-ab0a4513f790'
        }
    )
    # Extrai o reportId da resposta e faz o print
    report_id = response['reportId']
    print(f"Report ID: {report_id}")

    # Retorna um objeto JSON com a resposta
    return {
        'statusCode': 200,
        'body': {
            'report_id': report_id,
            'message': f'Relatório gerado com sucesso. Report ID: {report_id}'
        }
    }
