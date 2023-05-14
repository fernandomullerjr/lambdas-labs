

# ###############################################################################################################################################################
# ###############################################################################################################################################################
# ###############################################################################################################################################################
# ###############################################################################################################################################################
#  Git

git status
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git add .
git commit -m "Lambda Labs - JSON 2 HTML"
git push
git status











# ###############################################################################################################################################################
# ###############################################################################################################################################################
# ###############################################################################################################################################################
# ###############################################################################################################################################################
# 
# Dia 11/05/2023

- Criando nova

/home/fernando/cursos/lambdas-labs/json-to-html/python-lambdas/python-lambda22.py


- Ativando inspector na região da Virginia

- Subindo EC2

Elastic IP addresses
 35.169.22.123 (ip-elastico-ec2-lab) [Public IP]

Public IPv4 DNS
 ec2-35-169-22-123.compute-1.amazonaws.com



- Criado bucket
devops-luxor





# ###############################################################################################################################################################
# ###############################################################################################################################################################
# ###############################################################################################################################################################
# ###############################################################################################################################################################
# PENDENTE

- Stop/Start na EC2
- Via "python-lambda22.py",   Criar script que faça:
    1. Obtenha arquivo JSON do S3.
    2. Converta o JSON para HTML.
    3. Salvar o HTML no bucket do S3.
- Devolver ip elástico da EC2.
- Desativar Amazon Inspector antes do fim do Trial.
- Terminate EC2.
- Deletar funções Lambda.





# ###############################################################################################################################################################
# ###############################################################################################################################################################
# ###############################################################################################################################################################
# ###############################################################################################################################################################
# Dia 13/05/2023

1 - Ler(get) arquivo JSON do bucket do S3.
2 - Converter o JSON para HTML.
3 - Enviar(put) arquivo HTML para o bucket do S3.
4 - Efetuar envio do arquivo HTML via email utilizando o SNS.



Claro, aqui está um exemplo de código Python que utiliza o serviço Lambda da AWS para fazer o GET de um objeto em um bucket S3, usando as variáveis "bucket_name" e "object_name" para especificar o nome do bucket e do objeto:

~~~~python

import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = event['bucket_name']
    object_name = event['object_name']
    
    try:
        response = s3.get_object(Bucket=bucket_name, Key=object_name)
        content = response['Body'].read()
        print(content)
    except Exception as e:
        print(e)
        raise e
~~~~

Este código usa a biblioteca boto3 para se comunicar com o serviço S3 da AWS. A função lambda_handler é executada quando a Lambda é acionada. As variáveis bucket_name e object_name são recuperadas do objeto "event" passado para a função. Em seguida, a função tenta obter o objeto especificado no bucket usando o método get_object. Se for bem sucedido, o conteúdo do objeto é lido e impresso na saída. Caso contrário, uma exceção é gerada e lançada.

Certifique-se de que as credenciais de acesso à AWS estejam configuradas corretamente na máquina em que o código será executado. Além disso, lembre-se de que a função Lambda deve ter permissão para acessar o bucket S3 e o objeto específico.




a saída é impressa na console da Lambda neste caso?
ChatGPT

Sim, a saída é impressa na console da Lambda neste caso. No código que forneci, a função print() é usada para imprimir o conteúdo do objeto na saída padrão da Lambda. A saída pode ser visualizada na console de monitoramento da Lambda no painel de controle da AWS.

Se você deseja que a saída seja retornada para o invocador da função Lambda, você pode modificar o código para retornar uma resposta HTTP, como um JSON. Por exemplo:

~~~~python

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
~~~~

Neste caso, o conteúdo do objeto é retornado em um objeto JSON com o código de status HTTP 200 (OK). Se ocorrer algum erro, um objeto JSON com o código de status HTTP 500 (Erro interno do servidor) é retornado.