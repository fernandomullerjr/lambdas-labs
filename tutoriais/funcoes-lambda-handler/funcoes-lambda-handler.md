
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





- Testando:
/home/fernando/cursos/lambdas-labs/tutoriais/funcoes-lambda-handler/lambda1.py

- ERRO
"errorMessage": "Unable to import module 'lambda1': No module named 'requests'",








- Nova lambda

Aqui está um exemplo de código em Python que você pode usar no AWS Lambda, com as quatro funções descritas: uma função "hello_world" que retorna uma resposta simples, uma função "simple_calculation" que realiza um cálculo simples e retorna o resultado, uma função "generate_response_message" que obtém o resultado do cálculo anterior e cria uma mensagem de resposta interpolando esse valor em uma mensagem, e uma função "lambda_handler" que chama as outras três funções:

~~~~python

def hello_world():
    return "Hello, world!"

def simple_calculation(num1, num2):
    return num1 + num2

def generate_response_message(result):
    message = f"O resultado do cálculo é: {result}"
    return message

def lambda_handler(event, context):
    # Chama a função hello_world
    result_hello_world = hello_world()

    # Chama a função simple_calculation
    num1 = 5
    num2 = 3
    result_calculation = simple_calculation(num1, num2)

    # Chama a função generate_response_message
    response_message = generate_response_message(result_calculation)

    # Retorno da resposta
    return {
        "statusCode": 200,
        "body": {
            "hello_world": result_hello_world,
            "calculation_result": result_calculation,
            "response_message": response_message
        }
    }
~~~~

Neste exemplo, a função "hello_world" simplesmente retorna a mensagem "Hello, world!". A função "simple_calculation" recebe dois números (num1 e num2), realiza uma soma simples e retorna o resultado. A função "generate_response_message" recebe o resultado do cálculo anterior e cria uma mensagem interpolando esse valor. Por fim, a função "lambda_handler" chama as três funções, armazena os resultados em variáveis e retorna uma resposta contendo esses resultados.

Você pode ajustar os números e as mensagens de acordo com suas necessidades.

- Testando:
/home/fernando/cursos/lambdas-labs/tutoriais/funcoes-lambda-handler/lambda2.py

- Funcionou, OK:

~~~~bash
Test Event Name
teste

Response
{
  "statusCode": 200,
  "body": {
    "hello_world": "Hello, world!",
    "calculation_result": 8,
    "response_message": "O resultado do cálculo é: 8"
  }
}
~~~~