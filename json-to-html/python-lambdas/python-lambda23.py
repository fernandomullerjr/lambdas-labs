import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = event['bucket_name']
    object_name = event['object_name']
    
    try:
        response = s3.get_object(Bucket=bucket_name, Key=object_name)
        content = response['Body'].read()
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