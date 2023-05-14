

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






A variável é definida a partir dos valores passados para a função lambda_handler por meio do parâmetro event. No código fornecido, a linha bucket_name = event['bucket_name'] define o valor da variável bucket_name, enquanto a linha object_name = event['object_name'] define o valor da variável object_name.

Portanto, para definir o valor dessas variáveis, você deve passá-las como um dicionário no evento de entrada do seu lambda. Por exemplo, se você quiser buscar um objeto chamado meu-arquivo.txt no bucket meu-bucket, o evento de entrada pode ser:

~~~~json

{
    "bucket_name": "meu-bucket",
    "object_name": "meu-arquivo.txt"
}
~~~~

Assim, o código irá utilizar esses valores para buscar o objeto correto no bucket especificado.





- Criada policy no IAM
/home/fernando/cursos/lambdas-labs/json-to-html/python-lambdas/policy-devops-luxor.json
s3-permite-acesso-bucket-devops-luxor



Ocorreu erro abaixo:

~~~~JSON
"Response
{
  "errorMessage": "'devops-luxor'",
  "errorType": "KeyError",
  "requestId": "1efb5018-77f1-420f-a64a-ce59cc8ac17d",
  "stackTrace": [
    "  File \"/var/task/lambda_function.py\", line 6, in lambda_handler\n    bucket_name = event['devops-luxor']\n"
  ]
}"
~~~~



- Ajustando
e ao invés de passar um evento, passar as variáveis de forma fixa no código no começo do código, como ficaria?
ChatGPT

Caso queira passar as variáveis de forma fixa no início do código, você pode simplesmente remover a leitura do evento e definir diretamente os valores para as variáveis bucket_name e object_name.

Por exemplo, suponha que você deseja definir o valor devops-luxor para bucket_name e base1.json para object_name. Nesse caso, o código ficaria da seguinte forma:

~~~~python

import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'devops-luxor'
    object_name = 'base1.json'
    
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

Observe que, nesse caso, a variável event não é mais utilizada, já que as variáveis bucket_name e object_name foram definidas diretamente no código.


- Editado:
/home/fernando/cursos/lambdas-labs/json-to-html/python-lambdas/python-lambda23.py


- Teste, OK:

~~~~JSON
Response
{
  "statusCode": 200,
  "body": "{\"content\": \"{\\n    \\\"findings\\\": [\\n 
[restante omitido...]
}
~~~~














Para converter um JSON para HTML em Python, podemos usar uma biblioteca chamada json2html. Primeiro, precisamos instalá-la usando o pip. No prompt de comando, digite o seguinte comando:

pip install json2html

Depois de instalada a biblioteca, podemos usar o seguinte código para converter um JSON para HTML:

python

import json
from json2html import json2html

def json_to_html(json_string):
    json_object = json.loads(json_string)
    html_string = json2html.convert(json=json_object)
    return html_string

Onde json_string é uma string contendo o JSON que desejamos converter para HTML. A função json_to_html converte o JSON para um objeto Python e, em seguida, usa a função convert da biblioteca json2html para gerar uma string HTML.

Podemos chamar essa função com o seguinte código:

python

json_string = '{"name": "John", "age": 30, "city": "New York"}'
html_string = json_to_html(json_string)
print(html_string)

Este código converte o seguinte JSON:

json

{
  "name": "John",
  "age": 30,
  "city": "New York"
}

Para o seguinte HTML:

html

<table border="1"><tr><th>name</th><td>John</td></tr><tr><th>age</th><td>30</td></tr><tr><th>city</th><td>New York</td></tr></table>

Este é um exemplo simples de conversão de um JSON para HTML, mas a biblioteca json2html oferece muitas opções de formatação e personalização. Consulte a documentação da biblioteca para saber mais.
User
não tenho acesso para instalar o json2html via pip, pois o código será executado via AWS Lambda
ChatGPT

Você pode incluir a biblioteca json2html diretamente no pacote que será enviado para a AWS Lambda. Isso pode ser feito baixando o pacote json2html no seu ambiente local e incluindo-o no diretório do seu projeto.

Por exemplo, suponha que você tenha baixado o pacote json2html em um diretório chamado "libs" e seu projeto esteja organizado da seguinte maneira:

markdown

meu_projeto/
|_ lambda_function.py
|_ libs/
   |_ json2html/
      |_ json2html.py
      |_ ...

Em seguida, você pode importar a biblioteca json2html no seu código Python da seguinte maneira:

python

from libs.json2html import json2html
import json

def lambda_handler(event, context):
    json_data = {"nome": "João", "sobrenome": "Silva", "idade": 30}
    html = json2html.convert(json = json.dumps(json_data))
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html"},
        "body": html
    }

Dessa forma, quando você empacotar o seu projeto e enviar para a AWS Lambda, a biblioteca json2html estará incluída no pacote.










# PENDENTE
- Ver como instalar modulos do Python no AWS Lambda, para poder utilizar o json2html, por exemplo.
- Instalar o "bs4 import BeautifulSoup" também.








- Ver como instalar modulos do Python no AWS Lambda, para poder utilizar o json2html, por exemplo.
https://www.youtube.com/watch?v=n74poysXaJM


pip install json2html -t .