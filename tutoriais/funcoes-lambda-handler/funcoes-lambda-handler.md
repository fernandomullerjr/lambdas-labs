
# ###############################################################################################################################################################
# ###############################################################################################################################################################
# ###############################################################################################################################################################
# ###############################################################################################################################################################
#  Git

git status
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git add .
git commit -m "Funções em Python - AWS Lambdas"
git push
git status







# ###############################################################################################################################################################
# ###############################################################################################################################################################
# ###############################################################################################################################################################
# ###############################################################################################################################################################
#  Funções em Python - AWS Lambdas

Claro! Abaixo está um exemplo de código em Python que você pode usar no AWS Lambda, com as três funções descritas: uma função "hello_world" que retorna uma resposta simples, uma função "get_current_time" que faz uma solicitação HTTP para obter o horário exato de uma página e uma função "lambda_handler" que chama as outras duas funções:

~~~~python

import requests

def hello_world():
    return "Hello, world!"

def get_current_time():
    response = requests.get("https://exemplo.com/horario")  # substitua com a URL correta
    if response.status_code == 200:
        return response.text
    else:
        return "Não foi possível obter o horário."

def lambda_handler(event, context):
    # Chamada das outras funções
    result_hello_world = hello_world()
    result_current_time = get_current_time()

    # Retorno das respostas
    return {
        "statusCode": 200,
        "body": {
            "hello_world": result_hello_world,
            "current_time": result_current_time
        }
    }
~~~~

Lembre-se de substituir a URL correta na função "get_current_time" para que ela obtenha o horário exato de uma página real. Além disso, você pode ajustar as respostas e a estrutura de retorno do "lambda_handler" de acordo com suas necessidades.










"errorMessage": "Unable to import module 'lambda1': No module named 'requests'",