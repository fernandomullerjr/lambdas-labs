import requests

def hello_world():
    return "Hello, world!"

def get_current_time():
    response = requests.get("http://www.horacerta.com.br/index.php?city=sao_paulo")  # substitua com a URL correta
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