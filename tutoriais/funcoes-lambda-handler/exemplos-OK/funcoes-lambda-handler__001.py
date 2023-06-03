
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