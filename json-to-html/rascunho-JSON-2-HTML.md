

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

~~~~python

import json
from json2html import json2html

def json_to_html(json_string):
    json_object = json.loads(json_string)
    html_string = json2html.convert(json=json_object)
    return html_string
~~~~

Onde json_string é uma string contendo o JSON que desejamos converter para HTML. A função json_to_html converte o JSON para um objeto Python e, em seguida, usa a função convert da biblioteca json2html para gerar uma string HTML.

Podemos chamar essa função com o seguinte código:

~~~~python

json_string = '{"name": "John", "age": 30, "city": "New York"}'
html_string = json_to_html(json_string)
print(html_string)
~~~~

Este código converte o seguinte JSON:

~~~~json

{
  "name": "John",
  "age": 30,
  "city": "New York"
}
~~~~

Para o seguinte HTML:

~~~~html

<table border="1"><tr><th>name</th><td>John</td></tr><tr><th>age</th><td>30</td></tr><tr><th>city</th><td>New York</td></tr></table>
~~~~


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
https://www.youtube.com/watch?v=n74poysXaJM
- Instalar o "bs4 import BeautifulSoup" também.








- Ver como instalar modulos do Python no AWS Lambda, para poder utilizar o json2html, por exemplo.
https://www.youtube.com/watch?v=n74poysXaJM

cd
/home/fernando/cursos/lambdas-labs/modulos/json2html
pip install json2html -t .






1 - Ler(get) arquivo JSON do bucket do S3.
2 - Converter o JSON para HTML.
3 - Enviar(put) arquivo HTML para o bucket do S3.
4 - Efetuar envio do arquivo HTML via email utilizando o SNS.




# PENDENTE
- Ver como instalar modulos do Python no AWS Lambda, para poder utilizar o json2html, por exemplo. Utilizando camadas no AWS-Lambda.
https://www.youtube.com/watch?v=n74poysXaJM
- Instalar o "bs4 import BeautifulSoup" também.
- Usar o código do base8, fazer todo o processo com sumário+conversão-html.













# ###############################################################################################################################################################
# ###############################################################################################################################################################
# ###############################################################################################################################################################
# ###############################################################################################################################################################
# Dia 14/05/2023



- Ajustando SSM para EC2 ser coletada pelo Amazon Inspector

https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-ec2.html

Successfully attached ec2-basico to instance i-0db6e68a367e54c2b




22:25h
	LINUX	
Actively monitoring
Resource is being continuously monitored by Inspector.


- Verificando que a EC2 ficou OK agora, sendo coletada corretamente pelo Amazon Inspector.





# PENDENTE
- Ver como instalar modulos do Python no AWS Lambda, para poder utilizar o json2html, por exemplo. Utilizando camadas no AWS-Lambda.
https://www.youtube.com/watch?v=n74poysXaJM
- Instalar o "bs4 import BeautifulSoup" também.
- Usar o código do base8, fazer todo o processo com sumário+conversão-html.

- Stop/Start na EC2
- Via "python-lambda22.py",   Criar script que faça:
    1. Obtenha arquivo JSON do S3.
    2. Converta o JSON para HTML.
    3. Salvar o HTML no bucket do S3.
- Devolver ip elástico da EC2.
- Desativar Amazon Inspector antes do fim do Trial.
- Terminate EC2.
- Deletar funções Lambda.






## GPT

Para criar as funções adicionais solicitadas, você pode adaptar o código da seguinte forma:

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
        
        # Chamar a função que converte o JSON para HTML
        html_content = json_to_html(content)
        
        # Chamar a função que envia o arquivo HTML para o bucket S3
        put_html_to_s3(html_content)
        
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

def json_to_html(json_content):
    # Implementar a conversão de JSON para HTML aqui
    return html_content

def put_html_to_s3(html_content):
    s3 = boto3.resource('s3')
    bucket_name = 'devops-luxor'
    object_name = 'relatorio-final.html'
    
    try:
        s3.Bucket(bucket_name).put_object(Key=object_name, Body=html_content)
        print("Arquivo HTML salvo com sucesso!")
    except Exception as e:
        print(e)
~~~~

A função json_to_html deve ser implementada para converter o conteúdo JSON obtido do bucket S3 para o formato HTML desejado. Você pode usar uma biblioteca externa, como json2html, ou implementar sua própria lógica de conversão.

A função put_html_to_s3 deve ser responsável por enviar o arquivo HTML para o bucket S3 com o nome relatorio-final.html. Note que esta função usa a biblioteca boto3.resource em vez de boto3.client. Isso porque precisamos acessar o método put_object, que não está disponível no cliente S3.

Para testar todas as funções ao mesmo tempo via console da AWS, basta criar um novo evento de teste e executar a função lambda_handler. Todas as funções adicionais serão chamadas dentro desta função. Certifique-se de que o bucket S3 esteja configurado corretamente e que as permissões de acesso estejam configuradas para permitir a escrita de objetos no bucket.






Claro! Segue abaixo um exemplo completo de como implementar a função json_to_html utilizando a biblioteca json2html para converter o conteúdo JSON para o formato HTML:

~~~~python

import json
import json2html

def json_to_html(json_content):
    # Converte o conteúdo JSON para o formato HTML utilizando a biblioteca json2html
    table = json2html.json2html.convert(json = json.loads(json_content))

    # Define o HTML completo, adicionando cabeçalho e rodapé
    html_content = """
    <html>
        <head>
            <title>Relatório JSON para HTML</title>
        </head>
        <body>
            <h1>Relatório JSON para HTML</h1>
            {}
            <hr>
            <p>Gerado automaticamente pela Lambda AWS</p>
        </body>
    </html>
    """.format(table)

    return html_content
~~~~

Nesse exemplo, utilizamos a biblioteca json2html para converter o conteúdo JSON para o formato HTML. O resultado da conversão é armazenado em uma variável chamada table. Em seguida, definimos o HTML completo, incluindo cabeçalho e rodapé, e usamos a variável table para inserir a tabela no corpo do documento.

Lembre-se de importar a biblioteca json2html no início do arquivo para que ela seja reconhecida pela função json_to_html.







## Camadas

- Criando Layers no AWS Lambda

json2html-camadas
Create version

    Successfully created layer json2html-camadas version 1.

Version
	
Version ARN
	
Description
1	arn:aws:lambda:us-east-1:261106957109:layer:json2html-camadas:1	Modulo json2html para usar no Python








- Botão "Layers"
    Add Layer
    Custom Layers
    json2html-camadas
    Version 1



- Erro ao testar Lambda24
/home/fernando/cursos/lambdas-labs/json-to-html/python-lambdas/python-lambda24.py

~~~~bash
Test Event Name
teste1

Response
{
  "errorMessage": "Unable to import module 'python-lambda24': No module named 'json2html'",
  "errorType": "Runtime.ImportModuleError",
  "requestId": "3d8aaab7-e9ab-40ea-9cc8-f4b1f7a410b3",
  "stackTrace": []
}

~~~~




fiz a criação de uma camada no AWS Lambda, mas ao tentar utilizar a biblioteca json2html ocorre o erro abaixo no AWS Lambda:


Response
{
  "errorMessage": "Unable to import module 'python-lambda24': No module named 'json2html'",
  "errorType": "Runtime.ImportModuleError",
  "requestId": "3d8aaab7-e9ab-40ea-9cc8-f4b1f7a410b3",
  "stackTrace": []
}
ChatGPT

Esse erro ocorre porque o pacote json2html não foi incluído na camada que você criou.

Para resolver esse problema, você pode criar uma camada com o pacote json2html e incluir essa camada na sua função Lambda.

Siga os passos abaixo para criar uma camada com o pacote json2html:

    Crie uma nova pasta em seu computador e nomeie-a json2html-layer.
    Dentro dessa pasta, crie outra pasta chamada python.
    Abra um terminal na pasta python e execute o comando pip install json2html -t . Esse comando irá instalar o pacote json2html na pasta python.
    Compacte o conteúdo da pasta json2html-layer em um arquivo zip. Certifique-se de que o arquivo zip contenha a pasta python e o pacote json2html.

Com a camada json2html criada, você pode adicioná-la à sua função Lambda seguindo os passos abaixo:

    Acesse o console da AWS e navegue até a página de sua função Lambda.
    Na seção Camadas, clique em Adicionar camada.
    Selecione Camada personalizada e faça o upload do arquivo zip da camada json2html.
    Clique em Adicionar.

Após seguir esses passos, o pacote json2html estará disponível na sua função Lambda e o erro de importação deverá ser resolvido.


não seria pip3?
ChatGPT

Sim, você está correto. O comando correto para instalar o pacote json2html utilizando o pip3 seria pip3 install json2html -t ..

Peço desculpas pela minha resposta anterior estar incorreta. É sempre importante utilizar o comando correto para evitar problemas de compatibilidade e garantir que o pacote seja instalado corretamente. Obrigado por apontar o erro!



pip3 install json2html -t .








- Criando version da Layer

json2html-camadas
Create version

    Successfully created layer json2html-camadas version 2.

2	arn:aws:lambda:us-east-1:261106957109:layer:json2html-camadas:2	Modulo json2html para usar no Python - usando pip3 agora








usei o pip3 e na camada baixei o zip com este novo pacote, mas segue o erro:

 "Unable to import module 'python-lambda24': No module named 'json2html'",
ChatGPT

Se você já criou uma camada com o pacote json2html e a adicionou à sua função Lambda, é possível que o erro esteja ocorrendo por um dos seguintes motivos:

    O nome da camada ou da função não está correto: verifique se o nome da camada e o nome da função estão digitados corretamente e que estão em conformidade com o que foi especificado na configuração da camada e da função Lambda.

    A camada foi adicionada a uma região diferente da região onde a função Lambda está localizada: verifique se a camada foi adicionada à mesma região da função Lambda.

    A versão da camada não está correta: verifique se a versão da camada que foi adicionada à função Lambda está correta e é compatível com a versão da linguagem que a função Lambda está usando.

    A camada não está sendo acessada corretamente pela função Lambda: verifique se o caminho do pacote json2html está correto e que ele está sendo importado corretamente na sua função Lambda.

Tente verificar se algum desses pontos pode estar causando o erro e faça os ajustes necessários. Se ainda assim o erro persistir, tente criar uma nova camada com o pacote json2html e adicioná-la à sua função Lambda.








- Criada uma terceira camada para Lambda
3	arn:aws:lambda:us-east-1:261106957109:layer:json2html-camadas:3	Modulo json2html para usar no Python - usando pip3 E mudando ordem das pastas

- Testando:
/home/fernando/cursos/lambdas-labs/json-to-html/python-lambdas/python-lambda24.py

- Resolvido
importou o módulo json2html com sucesso!
importou o módulo json2html com sucesso!
importou o módulo json2html com sucesso!
importou o módulo json2html com sucesso!

Test Event Name
teste1

~~~~json
Response
{
  "statusCode": 200,
  "body": "{\"content\": \"{\\n    \\\"findings\\\": [\\n        {\\n            \\\"awsAccountId\\\": \\\"814635504079\\\",\\n            \\\"description\\\": \\\" Heap-based Buffer Overflow in GitHub repository vim/vim prior to 9.0.1376.\\\",\\n            \\\"exploitAvailable\\\": \\\"NO\\\",\\n            \\\"findingArn\\\": \\\"arn:aws:inspector2:sa-east-1:814635504079:finding/0013598e4e083e9999d68962dd571249\\\",\\n            \\\"firstObservedAt\\\": \\\"2023-05-04T14:15:25.841Z\\\",\\n            \\\"fixAvailable\\\": \\\"YES\\\",\\n            \\\"lastObservedAt\\\": \\\"2023-05-04T14:15:25.841Z\\\",\\n            \\\"packageVulnerabilityDetails\\\": {\\n                \\\"cvss\\\": [\\n                    {\\n                        \\\"baseScore\\\": 6.6,\\n                        \\\"scoringVector\\\": \\\"CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:H\\\",\\n                        \\\"source\\\": \\\"NVD\\\",\\n                        \\\"version\\\": \\\"3.1\\\"\\n                    }\\n                ],\\n                \\\"referenceUrls\\\": [\\n                    \\\"https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1170\\\",\\n                    \\\"https://ubuntu.com/security/notices/USN-5963-1\\\"\\n                ],\\n                \\\"relatedVulnerabilities\\\": [],\\n                \\\"source\\\": \\\"UBUNTU_CVE\\\",\\n                \\\"sourceUrl\\\": \\\"https://people.canonical.com/~ubuntu-security/cve/2023/CVE-2023-1170.html\\\",\\n                \\\"vendorCreatedAt\\\": \\\"2023-03-03T23:15:00Z\\\",\\n                \\\"vendorSeverity\\\": \\\"medium\\\",\\n                \\\"vulnerabilityId\\\": \\\"CVE-2023-1170\\\",\\n                \\\"vulnerablePackages\\\": [\\n                    {\\n                        \\\"arch\\\": \\\"X86_64\\\",\\n                        \\\"epoch\\\": 2,\\n                        \\\"fixedInVersion\\\": \\\"2:8.1.2269-1ubuntu5.12\\\",\\n                        \\\"name\\\": \\\"vim\\\",\\n                        \\\"packageManager\\\": \\\"OS\\\",\\n                        \\\"release\\\": \\\"1ubuntu5.9\\\",\\n                        \\\"remediation\\\": \\\"apt update && apt install --only-upgrade vim\\\",\\n                        \\\"version\\\": \\\"8.1.2269\\\"\\n                    },\\n                    {\\n                        \\\"arch\\\": \\\"X86_64\\\",\\n                        \\\"epoch\\\": 2,\\n                        \\\"fixedInVersion\\\": \\\"2:8.1.2269-1ubuntu5.12\\\",\\n                        \\\"name\\\": \\\"vim-tiny\\\",\\n                        \\\"packageManager\\\": \\\"OS\\\",\\n                        \\\"release\\\": \\\"1ubuntu5.9\\\",\\n                        \\\"remediation\\\": \\\"apt update && apt install --only-upgrade vim-tiny\\\",\\n                        \\\"version\\\": \\\"8.1.2269\\\"\\n                    }\\n                ]\\n            },\\n            \\\"remediation\\\": {\\n                \\\"recommendation\\\": {\\n                    \\\"text\\\": \\\"None Provided\\\"\\n                }\\n            },\\n            \\\"resources\\\": [\\n                {\\n                    \\\"details\\\": {\\n                        \\\"awsEc2Instance\\\": {\\n                            \\\"iamInstanceProfileArn\\\": \\\"arn:aws:iam::814635504079:instance-profile/RunCommand\\\",\\n                            \\\"imageId\\\": \\\"ami-06e297f909059c171\\\",\\n                            \\\"ipV4Addresses\\\": [\\n                                \\\"172.30.4.168\\\"\\n                            ],\\n                            \\\"ipV6Addresses\\\": [],\\n                            \\\"keyName\\\": \\\"appmax-21-08-2018-0\\\",\\n                            \\\"launchedAt\\\": \\\"2023-05-04T14:13:47Z\\\",\\n                            \\\"platform\\\": \\\"UBUNTU_20_04\\\",\\n                            \\\"subnetId\\\": \\\"subnet-0aa87558d279ec9b4\\\",\\n                            \\\"type\\\": \\\"c5.4xlarge\\\",\\n                            \\\"vpcId\\\": \\\"vpc-91831ff4\\\"\\n                        }\\n                    },\\n                    \\\"id\\\": \\\"i-0415ee9c35d4406ef\\\",\\n                    \\\"partition\\\": \\\"aws\\\",\\n                    \\\"region\\\": \\\"sa-east-1\\\",\\n                    \\\"tags\\\": {\\n                        \\\"aws:autoscaling:groupName\\\": \\\"appmax-asg-php-7-requisicoes\\\",\\n                        \\\"aws:ec2:fleet-id\\\": \\\"fleet-2d8e1d2f-f834-6bbe-2e18-84a8a3ec40b1\\\",\\n                        \\\"DevOpsRelatorioAmazonInspector\\\": \\\"1\\\",\\n                        \\\"Billing\\\": \\\"arquitetura\\\",\\n                        \\\"Ambiente\\\": \\\"appmax-prod-php-7-requisicoes\\\",\\n                        \\\"aws:ec2launchtemplate:version\\\": \\\"26\\\",\\n                        \\\"aws:ec2launchtemplate:id\\\": \\\"lt-09332363f4cb896d3\\\",\\n                        \\\"syncuser\\\": \\\"on\\\",\\n                        \\\"Name\\\": \\\"[Appmax] AutoScaling-PHP-7-requisicoes\\\"\\n                    },\\n                    \\\"type\\\": \\\"AWS_EC2_INSTANCE\\\"\\n                }\\n            ],\\n            \\\"severity\\\": \\\"MEDIUM\\\",\\n            \\\"status\\\": \\\"ACTIVE\\\",\\n            \\\"title\\\": \\\"CVE-2023-1170 - vim, vim-tiny\\\",\\n            \\\"type\\\": \\\"PACKAGE_VULNERABILITY\\\",\\n            \\\"updatedAt\\\": \\\"2023-05-04T14:15:25.841Z\\\"\\n        },\\n        {\\n            \\\"awsAccountId\\\": \\\"814635504079\\\",\\n            \\\"description\\\": \\\" Stack-based Buffer Overflow in GitHub repository vim/vim prior to 9.0.\\\",\\n            \\\"exploitAvailable\\\": \\\"NO\\\",\\n            \\\"findingArn\\\": \\\"arn:aws:inspector2:sa-east-1:814635504079:finding/ff52658379d87f999c4359cc123f4732\\\",\\n            \\\"firstObservedAt\\\": \\\"2023-05-04T14:17:08.924Z\\\",\\n            \\\"fixAvailable\\\": \\\"YES\\\",\\n            \\\"lastObservedAt\\\": \\\"2023-05-04T14:17:08.924Z\\\",\\n            \\\"packageVulnerabilityDetails\\\": {\\n                \\\"cvss\\\": [\\n                    {\\n                        \\\"baseScore\\\": 6.8,\\n                        \\\"scoringVector\\\": \\\"AV:N/AC:M/Au:N/C:P/I:P/A:P\\\",\\n                        \\\"source\\\": \\\"NVD\\\",\\n                        \\\"version\\\": \\\"2.0\\\"\\n                    },\\n                    {\\n                        \\\"baseScore\\\": 7.8,\\n                        \\\"scoringVector\\\": \\\"CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H\\\",\\n                        \\\"source\\\": \\\"NVD\\\",\\n                        \\\"version\\\": \\\"3.1\\\"\\n                    }\\n                ],\\n                \\\"referenceUrls\\\": [\\n                    \\\"https://ubuntu.com/security/notices/USN-5723-1\\\",\\n                    \\\"https://ubuntu.com/security/notices/USN-5995-1\\\",\\n                    \\\"https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2304\\\"\\n                ],\\n                \\\"relatedVulnerabilities\\\": [],\\n                \\\"source\\\": \\\"UBUNTU_CVE\\\",\\n                \\\"sourceUrl\\\": \\\"https://people.canonical.com/~ubuntu-security/cve/2022/CVE-2022-2304.html\\\",\\n                \\\"vendorCreatedAt\\\": \\\"2022-07-05T13:15:00Z\\\",\\n                \\\"vendorSeverity\\\": \\\"medium\\\",\\n                \\\"vulnerabilityId\\\": \\\"CVE-2022-2304\\\",\\n                \\\"vulnerablePackages\\\": [\\n                    {\\n                        \\\"arch\\\": \\\"X86_64\\\",\\n                        \\\"epoch\\\": 2,\\n                        \\\"fixedInVersion\\\": \\\"2:8.1.2269-1ubuntu5.13\\\",\\n                        \\\"name\\\": \\\"vim\\\",\\n                        \\\"packageManager\\\": \\\"OS\\\",\\n                        \\\"release\\\": \\\"1ubuntu5.9\\\",\\n                        \\\"remediation\\\": \\\"apt update && apt install --only-upgrade vim\\\",\\n                        \\\"version\\\": \\\"8.1.2269\\\"\\n                    },\\n                    {\\n                        \\\"arch\\\": \\\"X86_64\\\",\\n                        \\\"epoch\\\": 2,\\n                        \\\"fixedInVersion\\\": \\\"2:8.1.2269-1ubuntu5.13\\\",\\n                        \\\"name\\\": \\\"vim-tiny\\\",\\n                        \\\"packageManager\\\": \\\"OS\\\",\\n                        \\\"release\\\": \\\"1ubuntu5.9\\\",\\n                        \\\"remediation\\\": \\\"apt update && apt install --only-upgrade vim-tiny\\\",\\n                        \\\"version\\\": \\\"8.1.2269\\\"\\n                    }\\n                ]\\n            },\\n            \\\"remediation\\\": {\\n                \\\"recommendation\\\": {\\n                    \\\"text\\\": \\\"None Provided\\\"\\n                }\\n            },\\n            \\\"resources\\\": [\\n                {\\n                    \\\"details\\\": {\\n                        \\\"awsEc2Instance\\\": {\\n                            \\\"iamInstanceProfileArn\\\": \\\"arn:aws:iam::814635504079:instance-profile/RunCommand\\\",\\n                            \\\"imageId\\\": \\\"ami-0e24bad02f0872194\\\",\\n                            \\\"ipV4Addresses\\\": [\\n                                \\\"172.30.4.98\\\"\\n                            ],\\n                            \\\"ipV6Addresses\\\": [],\\n                            \\\"keyName\\\": \\\"appmax-21-08-2018-0\\\",\\n                            \\\"launchedAt\\\": \\\"2023-05-04T14:15:42Z\\\",\\n                            \\\"platform\\\": \\\"UBUNTU_20_04\\\",\\n                            \\\"subnetId\\\": \\\"subnet-0aa87558d279ec9b4\\\",\\n                            \\\"type\\\": \\\"r5a.large\\\",\\n                            \\\"vpcId\\\": \\\"vpc-91831ff4\\\"\\n                        }\\n                    },\\n                    \\\"id\\\": \\\"i-06b2f79a29da7746b\\\",\\n                    \\\"partition\\\": \\\"aws\\\",\\n                    \\\"region\\\": \\\"sa-east-1\\\",\\n                    \\\"tags\\\": {\\n                        \\\"aws:autoscaling:groupName\\\": \\\"appmax-asg-php-7-queue\\\",\\n                        \\\"aws:ec2:fleet-id\\\": \\\"fleet-8f9d3e05-228d-ee3c-2412-0f28fed3ebd0\\\",\\n                        \\\"DevOpsRelatorioAmazonInspector\\\": \\\"1\\\",\\n                        \\\"Billing\\\": \\\"arquitetura\\\",\\n                        \\\"amb\\\": \\\"appmax-queue\\\",\\n                        \\\"Ambiente\\\": \\\"appmax-queue\\\",\\n                        \\\"aws:ec2launchtemplate:version\\\": \\\"35\\\",\\n                        \\\"aws:ec2launchtemplate:id\\\": \\\"lt-092969c05aca14fee\\\",\\n                        \\\"syncuser\\\": \\\"on\\\",\\n                        \\\"Name\\\": \\\"[AppMax] Auto-Scaling-QUEUE-Supervisor-PHP-7\\\"\\n                    },\\n                    \\\"type\\\": \\\"AWS_EC2_INSTANCE\\\"\\n                }\\n            ],\\n            \\\"severity\\\": \\\"MEDIUM\\\",\\n            \\\"status\\\": \\\"ACTIVE\\\",\\n            \\\"title\\\": \\\"CVE-2022-2304 - vim, vim-tiny\\\",\\n            \\\"type\\\": \\\"PACKAGE_VULNERABILITY\\\",\\n            \\\"updatedAt\\\": \\\"2023-05-04T14:17:08.924Z\\\"\\n        },\\n        {\\n            \\\"awsAccountId\\\": \\\"814635504079\\\",\\n            \\\"description\\\": \\\" A flaw was found in ImageMagick. The vulnerability occurs due to improper use of open functions and leads to a denial of service. This flaw allows an attacker to crash the system.\\\",\\n            \\\"exploitAvailable\\\": \\\"NO\\\",\\n            \\\"findingArn\\\": \\\"arn:aws:inspector2:sa-east-1:814635504079:finding/ffabf790e5ec1051b86a32c3a9b230d5\\\",\\n            \\\"firstObservedAt\\\": \\\"2023-05-04T14:22:20.468Z\\\",\\n            \\\"fixAvailable\\\": \\\"YES\\\",\\n            \\\"lastObservedAt\\\": \\\"2023-05-04T14:22:20.468Z\\\",\\n            \\\"packageVulnerabilityDetails\\\": {\\n                \\\"cvss\\\": [\\n                    {\\n                        \\\"baseScore\\\": 4.3,\\n                        \\\"scoringVector\\\": \\\"AV:N/AC:M/Au:N/C:N/I:N/A:P\\\",\\n                        \\\"source\\\": \\\"NVD\\\",\\n                        \\\"version\\\": \\\"2.0\\\"\\n                    },\\n                    {\\n                        \\\"baseScore\\\": 5.5,\\n                        \\\"scoringVector\\\": \\\"CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H\\\",\\n                        \\\"source\\\": \\\"NVD\\\",\\n                        \\\"version\\\": \\\"3.1\\\"\\n                    }\\n                ],\\n                \\\"referenceUrls\\\": [\\n                    \\\"https://ubuntu.com/security/notices/USN-5736-2\\\",\\n                    \\\"https://ubuntu.com/security/notices/USN-5736-1\\\",\\n                    \\\"https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-4219\\\"\\n                ],\\n                \\\"relatedVulnerabilities\\\": [],\\n                \\\"source\\\": \\\"UBUNTU_CVE\\\",\\n                \\\"sourceUrl\\\": \\\"https://people.canonical.com/~ubuntu-security/cve/2021/CVE-2021-4219.html\\\",\\n                \\\"vendorCreatedAt\\\": \\\"2022-03-23T20:15:00Z\\\",\\n                \\\"vendorSeverity\\\": \\\"low\\\",\\n                \\\"vulnerabilityId\\\": \\\"CVE-2021-4219\\\",\\n                \\\"vulnerablePackages\\\": [\\n                    {\\n                        \\\"arch\\\": \\\"X86_64\\\",\\n                        \\\"epoch\\\": 8,\\n                        \\\"fixedInVersion\\\": \\\"8:6.9.10.23+dfsg-2.1ubuntu11.4+esm1\\\",\\n                        \\\"name\\\": \\\"libmagickcore-6.q16-6\\\",\\n                        \\\"packageManager\\\": \\\"OS\\\",\\n                        \\\"release\\\": \\\"2.1ubuntu11.4\\\",\\n                        \\\"remediation\\\": \\\"apt update && apt install --only-upgrade libmagickcore-6.q16-6\\\",\\n                        \\\"version\\\": \\\"6.9.10.23+dfsg\\\"\\n                    },\\n                    {\\n                        \\\"arch\\\": \\\"X86_64\\\",\\n                        \\\"epoch\\\": 8,\\n                        \\\"fixedInVersion\\\": \\\"8:6.9.10.23+dfsg-2.1ubuntu11.4+esm1\\\",\\n                        \\\"name\\\": \\\"libmagickwand-6.q16-6\\\",\\n                        \\\"packageManager\\\": \\\"OS\\\",\\n                        \\\"release\\\": \\\"2.1ubuntu11.4\\\",\\n                        \\\"remediation\\\": \\\"apt update && apt install --only-upgrade libmagickwand-6.q16-6\\\",\\n                        \\\"version\\\": \\\"6.9.10.23+dfsg\\\"\\n                    },\\n                    {\\n                        \\\"arch\\\": \\\"X86_64\\\",\\n                        \\\"epoch\\\": 8,\\n                        \\\"fixedInVersion\\\": \\\"8:6.9.10.23+dfsg-2.1ubuntu11.4+esm1\\\",\\n                        \\\"name\\\": \\\"imagemagick-6.q16\\\",\\n                        \\\"packageManager\\\": \\\"OS\\\",\\n                        \\\"release\\\": \\\"2.1ubuntu11.4\\\",\\n                        \\\"remediation\\\": \\\"apt update && apt install --only-upgrade imagemagick-6.q16\\\",\\n                        \\\"version\\\": \\\"6.9.10.23+dfsg\\\"\\n                    },\\n                    {\\n                        \\\"arch\\\": \\\"X86_64\\\",\\n                        \\\"epoch\\\": 8,\\n                        \\\"fixedInVersion\\\": \\\"8:6.9.10.23+dfsg-2.1ubuntu11.4+esm1\\\",\\n                        \\\"name\\\": \\\"libmagickcore-6.q16-6-extra\\\",\\n                        \\\"packageManager\\\": \\\"OS\\\",\\n                        \\\"release\\\": \\\"2.1ubuntu11.4\\\",\\n                        \\\"remediation\\\": \\\"apt update && apt install --only-upgrade libmagickcore-6.q16-6-extra\\\",\\n                        \\\"version\\\": \\\"6.9.10.23+dfsg\\\"\\n                    },\\n                    {\\n                        \\\"arch\\\": \\\"X86_64\\\",\\n                        \\\"epoch\\\": 8,\\n                        \\\"fixedInVersion\\\": \\\"8:6.9.10.23+dfsg-2.1ubuntu11.4+esm1\\\",\\n                        \\\"name\\\": \\\"imagemagick\\\",\\n                        \\\"packageManager\\\": \\\"OS\\\",\\n                        \\\"release\\\": \\\"2.1ubuntu11.4\\\",\\n                        \\\"remediation\\\": \\\"apt update && apt install --only-upgrade imagemagick\\\",\\n                        \\\"version\\\": \\\"6.9.10.23+dfsg\\\"\\n                    }\\n                ]\\n            },\\n            \\\"remediation\\\": {\\n                \\\"recommendation\\\": {\\n                    \\\"text\\\": \\\"None Provided\\\"\\n                }\\n            },\\n            \\\"resources\\\": [\\n                {\\n                    \\\"details\\\": {\\n                        \\\"awsEc2Instance\\\": {\\n                            \\\"iamInstanceProfileArn\\\": \\\"arn:aws:iam::814635504079:instance-profile/RunCommand\\\",\\n                            \\\"imageId\\\": \\\"ami-0e24bad02f0872194\\\",\\n                            \\\"ipV4Addresses\\\": [\\n                                \\\"172.30.4.153\\\"\\n                            ],\\n                            \\\"ipV6Addresses\\\": [],\\n                            \\\"keyName\\\": \\\"appmax-21-08-2018-0\\\",\\n                            \\\"launchedAt\\\": \\\"2023-05-04T14:21:03Z\\\",\\n                            \\\"platform\\\": \\\"UBUNTU_20_04\\\",\\n                            \\\"subnetId\\\": \\\"subnet-0aa87558d279ec9b4\\\",\\n                            \\\"type\\\": \\\"m5a.xlarge\\\",\\n                            \\\"vpcId\\\": \\\"vpc-91831ff4\\\"\\n                        }\\n                    },\\n                    \\\"id\\\": \\\"i-04e668b1627742918\\\",\\n                    \\\"partition\\\": \\\"aws\\\",\\n                    \\\"region\\\": \\\"sa-east-1\\\",\\n                    \\\"tags\\\": {\\n                        \\\"aws:autoscaling:groupName\\\": \\\"appmax-asg-php-7-queue\\\",\\n                        \\\"aws:ec2:fleet-id\\\": \\\"fleet-399fa816-9527-468f-2698-092241c447ea\\\",\\n                        \\\"DevOpsRelatorioAmazonInspector\\\": \\\"1\\\",\\n                        \\\"Billing\\\": \\\"arquitetura\\\",\\n                        \\\"amb\\\": \\\"appmax-queue\\\",\\n                        \\\"Ambiente\\\": \\\"appmax-queue\\\",\\n                        \\\"aws:ec2launchtemplate:version\\\": \\\"35\\\",\\n                        \\\"aws:ec2launchtemplate:id\\\": \\\"lt-092969c05aca14fee\\\",\\n                        \\\"syncuser\\\": \\\"on\\\",\\n                        \\\"Name\\\": \\\"[AppMax] Auto-Scaling-QUEUE-Supervisor-PHP-7\\\"\\n                    },\\n                    \\\"type\\\": \\\"AWS_EC2_INSTANCE\\\"\\n                }\\n            ],\\n            \\\"severity\\\": \\\"LOW\\\",\\n            \\\"status\\\": \\\"ACTIVE\\\",\\n            \\\"title\\\": \\\"CVE-2021-4219 - libmagickcore-6.q16-6, libmagickwand-6.q16-6 and 3 more\\\",\\n            \\\"type\\\": \\\"PACKAGE_VULNERABILITY\\\",\\n            \\\"updatedAt\\\": \\\"2023-05-04T14:22:20.468Z\\\"\\n        }\\n    ]\\n}\"}"
}

~~~~






- Arquivo HTML que foi enviado ao S3, baixado:
file:///D:/OneDrive/Documents/Dev/Python/Lambdas/scan-interno-alternativa/reports-amazon-inspector/Python-testes/relatorio-final.html















# PENDENTE
- Instalar o "bs4 import BeautifulSoup" também, se necessário.
- Criar nova versão, fazendo com que o JSON convertido no HTML tenha sumários, resumo, melhor organização, etc. Separar por instance-id as findings???
- Separar por instance-id as findings???
- Usar o código do base8, fazer todo o processo com sumário+conversão-html.
- Stop/Start na EC2
- Devolver ip elástico da EC2.
- Desativar Amazon Inspector antes do fim do Trial.
- Terminate EC2.
- Deletar funções Lambda.
















Para adaptar a função json_to_html em Python para fazer um sumário contendo os totais de findings por severity e vendorSeverity, podemos fazer o seguinte:

    Converter o conteúdo JSON para um dicionário Python.
    Criar um dicionário vazio para armazenar o sumário dos findings por severity e vendorSeverity.
    Iterar sobre cada finding no JSON e incrementar o contador correspondente no dicionário de sumário.
    Adicionar uma tabela HTML ao corpo do documento que exibe o sumário.
    Atualizar a tabela principal para incluir um link para a tabela de sumário.

Segue abaixo o código atualizado da função:

~~~~python

def json_to_html(json_content):
    # Converte o conteúdo JSON para um dicionário Python
    data = json.loads(json_content)

    # Define o HTML completo, adicionando cabeçalho e rodapé
    html_content = """
    <html>
        <head>
            <title>Relatório JSON para HTML</title>
        </head>
        <body>
            <h1>Relatório JSON para HTML</h1>
            {}
            <hr>
            <h2>Sumário de Findings</h2>
            {}
            <p>Gerado automaticamente pela Lambda AWS</p>
        </body>
    </html>
    """

    # Cria um dicionário para armazenar o sumário
    summary = {"total": 0, "severity": {}, "vendorSeverity": {}}

    # Itera sobre cada finding no JSON e atualiza o sumário
    for finding in data["findings"]:
        summary["total"] += 1
        severity = finding["severity"]
        summary["severity"][severity] = summary["severity"].get(severity, 0) + 1
        vendor_severity = finding["packageVulnerabilityDetails"]["vendorSeverity"]
        summary["vendorSeverity"][vendor_severity] = summary["vendorSeverity"].get(vendor_severity, 0) + 1

    # Cria a tabela de sumário
    summary_table = "<table><tr><th></th><th>Total</th></tr>"
    for severity, count in summary["severity"].items():
        summary_table += "<tr><td>Severity {}</td><td>{}</td></tr>".format(severity, count)
    for vendor_severity, count in summary["vendorSeverity"].items():
        summary_table += "<tr><td>Vendor Severity {}</td><td>{}</td></tr>".format(vendor_severity, count)
    summary_table += "<tr><td>Total</td><td>{}</td></tr></table>".format(summary["total"])

    # Cria a tabela principal
    main_table = json2html.json2html.convert(json=data, table_attributes="id=\"findings_table\"")

    # Adiciona um link para a tabela de sumário
    main_table = main_table.replace("<body>", "<body><p><a href=\"#summary_table\">Ver Sumário de Findings</a></p>")

    # Insere as tabelas no HTML completo e retorna o resultado
    return html_content.format(main_table, summary_table)
~~~~

Agora, quando chamamos a função json_to_html com um JSON de findings, ela retorna um HTML que contém a tabela principal e um sumário de findings por severity e vendorSeverity. O sumário é exibido em uma tabela separada abaixo da tabela principal, e inclui o número









- Testando

- Trouxe

Sumário de Findings
	Total
Severity MEDIUM	2
Severity LOW	1
Vendor Severity medium	2
Vendor Severity low	1
Total	3

Gerado automaticamente pela Lambda AWS







## GPT

quero o mesmo código, só que sem os "Vendor Severity", além disto, preciso que verifique porque a tabela do HTML ficou sem bordas e formatação
ChatGPT

Claro, aqui está o código sem a coluna "Vendor Severity":

~~~~python

import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://nvd.nist.gov/vuln/search/results?adv_search=false&form_type=Basic&results_type=overview&query=cveId%3DCVE-2021-34527&search_type=all'

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

table = soup.find('table', {'data-testid': 'vuln-results-table'})
rows = table.find_all('tr')

data = []
for row in rows[1:]:
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    data.append(cols)

df = pd.DataFrame(data, columns=['CVE ID', 'Description', 'CVSS Score', 'Attack Vector', 'Attack Complexity', 'Privileges Required', 'User Interaction', 'Scope', 'Confidentiality', 'Integrity', 'Availability'])

print(df)

Quanto à tabela do HTML sem bordas e formatação, isso pode acontecer se as informações de estilo CSS não forem incluídas na resposta da solicitação. Você pode tentar usar a biblioteca lxml para analisar a resposta em vez do html.parser padrão do Python. Aqui está o código modificado que usa a biblioteca lxml:

python

import pandas as pd
import requests
from lxml import html

url = 'https://nvd.nist.gov/vuln/search/results?adv_search=false&form_type=Basic&results_type=overview&query=cveId%3DCVE-2021-34527&search_type=all'

html = requests.get(url).content
soup = html.fromstring(html)

table = soup.xpath('//table[@data-testid="vuln-results-table"]')[0]
rows = table.xpath('.//tr')

data = []
for row in rows[1:]:
    cols = row.xpath('.//td/text()')
    cols = [col.strip() for col in cols]
    data.append(cols)

df = pd.DataFrame(data, columns=['CVE ID', 'Description', 'CVSS Score', 'Attack Vector', 'Attack Complexity', 'Privileges Required', 'User Interaction', 'Scope', 'Confidentiality', 'Integrity', 'Availability'])

print(df)
~~~~

Este código usa o método xpath do objeto lxml.html.HtmlElement para procurar a tabela com o atributo data-testid específico e seus filhos tr. Em seguida, ele usa o método xpath novamente para procurar os filhos td de cada tr. O restante do código é idêntico ao código original.























## GPT

Claro! Aqui está a versão atualizada da função json_to_html que não inclui a coluna "Vendor Severity" e adiciona bordas à tabela:

~~~~python

def json_to_html(json_content):
    # Converte o conteúdo JSON para um dicionário Python
    data = json.loads(json_content)

    # Define o HTML completo, adicionando cabeçalho e rodapé
    html_content = """
    <html>
        <head>
            <title>Relatório JSON para HTML</title>
            <style>
                table, th, td {
                    border: 1px solid black;
                    border-collapse: collapse;
                    padding: 5px;
                }
            </style>
        </head>
        <body>
            <h1>Relatório JSON para HTML</h1>
            {}
            <hr>
            <h2>Sumário de Findings</h2>
            {}
            <p>Gerado automaticamente pela Lambda AWS</p>
        </body>
    </html>
    """

    # Cria um dicionário para armazenar o sumário
    summary = {"total": 0, "severity": {}}

    # Itera sobre cada finding no JSON e atualiza o sumário
    for finding in data["findings"]:
        summary["total"] += 1
        severity = finding["severity"]
        summary["severity"][severity] = summary["severity"].get(severity, 0) + 1

    # Cria a tabela de sumário
    summary_table = "<table><tr><th>Severity</th><th>Total</th></tr>"
    for severity, count in summary["severity"].items():
        summary_table += "<tr><td>{}</td><td>{}</td></tr>".format(severity, count)
    summary_table += "<tr><td>Total</td><td>{}</td></tr></table>".format(summary["total"])

    # Cria a tabela principal
    main_table = json2html.json2html.convert(json=data, table_attributes="id=\"findings_table\"")

    # Adiciona um link para a tabela de sumário
    main_table = main_table.replace("<body>", "<body><p><a href=\"#summary_table\">Ver Sumário de Findings</a></p>")

    # Insere as tabelas no HTML completo e retorna o resultado
    return html_content.format(main_table, summary_table)
~~~~

As alterações foram as seguintes:

    Removemos a linha summary = {"total": 0, "severity": {}, "vendorSeverity": {}} e atualizamos a linha 18 para summary = {"total": 0, "severity": {}}, já que não estamos mais rastreando a "Vendor Severity".
    Na linha 25, atualizamos summary_table = "<table><tr><th></th><th>Total</th></tr>" para summary_table = "<table><tr><th>Severity</th><th>Total</th></tr>" para refletir as mudanças na estrutura da tabela de resumo.
    Na linha 27, atualizamos for vendor_severity, count in summary["vendorSeverity"].items(): para for severity, count in summary["severity"].items(): para refletir as mudanças no dicionário "summary".
    Na linha 29, atualizamos summary_table += "<tr><td>Vendor Severity {}</td><td>{}</td></tr>".format(vendor_severity, count) para `summary_table += "<tr><td>{}</td><td>{








# PENDENTE
- Criar v26 e validar o ultimo GPT.
- Criar nova versão, fazendo com que o JSON convertido no HTML tenha sumários, resumo, melhor organização, etc. Separar por instance-id as findings???
- Separar por instance-id as findings???
- Instalar o "bs4 import BeautifulSoup" também, se necessário.
- Usar o código do base8, fazer todo o processo com sumário+conversão-html.
- Stop/Start na EC2
- Devolver ip elástico da EC2.
- Desativar Amazon Inspector antes do fim do Trial.
- Terminate EC2.
- Deletar funções Lambda.











# ###############################################################################################################################################################
# ###############################################################################################################################################################
# ###############################################################################################################################################################
# ###############################################################################################################################################################
# 
# Dia 15/05/2023



git status
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git add .
git commit -m "Lambda Labs - JSON 2 HTML, Lambda26"
git push
git status


- Novo teste
/home/fernando/cursos/lambdas-labs/json-to-html/python-lambdas/python-lambda26.py




- ERRO

~~~~bash
Test Event Name
teste1

Response
{
  "statusCode": 500,
  "body": "{\"error\": \"'\\\\n                    border'\"}"
}

Function Logs
START RequestId: 97bc6385-8889-46d5-9404-cd25bdd4568a Version: $LATEST
'\n                    border'
END RequestId: 97bc6385-8889-46d5-9404-cd25bdd4568a
REPORT RequestId: 97bc6385-8889-46d5-9404-cd25bdd4568a	Duration: 2763.12 ms	Billed Duration: 2764 ms	Memory Size: 128 MB	Max Memory Used: 79 MB	Init Duration: 312.07 ms

Request ID
97bc6385-8889-46d5-9404-cd25bdd4568a
~~~~









Peço desculpas pelo equívoco. Você está correto, o nome da função json_to_html está sendo referenciado corretamente no código.

O erro que você está enfrentando parece estar relacionado ao conteúdo JSON retornado do objeto S3. O trecho content = response['Body'].read() retorna os dados binários do objeto S3. No entanto, a função json_to_html espera receber uma string JSON como entrada.

Para corrigir esse problema, você precisa decodificar os dados binários em uma string antes de passá-los para a função json_to_html. Você pode fazer isso usando o método decode('utf-8').

Para corrigir o erro, modifique a linha 16 do código da seguinte forma:

python

content = response['Body'].read().decode('utf-8')

Dessa forma, os dados retornados do objeto S3 serão decodificados corretamente antes de serem passados para a função json_to_html. Isso deve resolver o problema e permitir que o código seja executado corretamente.



- Adicionando:
content = response['Body'].read().decode('utf-8')

no arquivo:
/home/fernando/cursos/lambdas-labs/json-to-html/python-lambdas/python-lambda26.py



- Segue com erro:

~~~~bash
Test Event Name
teste1

Response
{
  "statusCode": 500,
  "body": "{\"error\": \"'\\\\n                    border'\"}"
}

Function Logs
START RequestId: 213adaed-b4fe-425d-9a07-7dab4559484e Version: $LATEST
'\n                    border'
END RequestId: 213adaed-b4fe-425d-9a07-7dab4559484e
REPORT RequestId: 213adaed-b4fe-425d-9a07-7dab4559484e	Duration: 2776.88 ms	Billed Duration: 2777 ms	Memory Size: 128 MB	Max Memory Used: 78 MB	Init Duration: 334.17 ms

Request ID
213adaed-b4fe-425d-9a07-7dab4559484e
~~~~







# ###############################################################################################################################################################
# ###############################################################################################################################################################
# ###############################################################################################################################################################
# ###############################################################################################################################################################
# 
# Dia 16/05/2023


- Lambda26 não funciona, ocorre erro 500.


# PENDENTE
- V25 traz o sumário, mas consta ainda os "Vendor Severity" e as tabelas vieram sem bordas.
- Criar v26 e validar o ultimo GPT.
- Criar nova versão, fazendo com que o JSON convertido no HTML tenha sumários, resumo, melhor organização, etc. Separar por instance-id as findings???
- Separar por instance-id as findings???
- Instalar o "bs4 import BeautifulSoup" também, se necessário.
- Usar o código do base8, fazer todo o processo com sumário+conversão-html.
- Stop/Start na EC2
- Devolver ip elástico da EC2.
- Desativar Amazon Inspector antes do fim do Trial.
- Terminate EC2.
- Deletar funções Lambda.
- Documentar questões sobre Camadas para as Lambdas.










Peço desculpas pela confusão anterior, aqui está o código completo e corrigido com formatação de bordas e link para a tabela de sumário:

~~~~python

import json
import json2html

def json_to_html(json_content):
    # Converte o conteúdo JSON para um dicionário Python
    data = json.loads(json_content)

    # Define o HTML completo, adicionando cabeçalho e rodapé
    html_content = """
    <html>
        <head>
            <title>Relatório JSON para HTML</title>
            <style>
                table {
                    border-collapse: collapse;
                }
                table, th, td {
                    border: 1px solid black;
                }
            </style>
        </head>
        <body>
            <h1>Relatório JSON para HTML</h1>
            {}
            <hr>
            <h2 id="summary_table">Sumário de Findings</h2>
            {}
            <p>Gerado automaticamente pela Lambda AWS</p>
        </body>
    </html>
    """

    # Cria um dicionário para armazenar o sumário
    summary = {"total": 0, "severity": {}, "vendorSeverity": {}}

    # Itera sobre cada finding no JSON e atualiza o sumário
    for finding in data["findings"]:
        summary["total"] += 1
        severity = finding["severity"]
        summary["severity"][severity] = summary["severity"].get(severity, 0) + 1
        vendor_severity = finding["packageVulnerabilityDetails"]["vendorSeverity"]
        summary["vendorSeverity"][vendor_severity] = summary["vendorSeverity"].get(vendor_severity, 0) + 1

    # Cria a tabela de sumário
    summary_table = "<table><tr><th></th><th>Total</th></tr>"
    for severity, count in summary["severity"].items():
        summary_table += "<tr><td>Severity {}</td><td>{}</td></tr>".format(severity, count)
    for vendor_severity, count in summary["vendorSeverity"].items():
        summary_table += "<tr><td>Vendor Severity {}</td><td>{}</td></tr>".format(vendor_severity, count)
    summary_table += "<tr><td>Total</td><td>{}</td></tr></table>".format(summary["total"])

    # Cria a tabela principal
    main_table = json2html.json2html.convert(json=data, table_attributes="id=\"findings_table\"")

    # Adiciona um link para a tabela de sumário
    main_table = main_table.replace("<body>", "<body><p><a href=\"#summary_table\">Ver Sumário de Findings</a></p>")

    # Insere as tabelas no HTML completo e retorna o resultado
    return html_content.format(main_table, summary_table)
~~~~






- Criada v27
/home/fernando/cursos/lambdas-labs/json-to-html/python-lambdas/python-lambda27.py

- Testando
- ERRO

~~~~BASH
Test Event Name
teste1

Response
{
  "statusCode": 500,
  "body": "{\"error\": \"'\\\\n                    border-collapse'\"}"
}

Function Logs
START RequestId: 4ea4cdf8-69c6-4eb6-986d-f879c173eab4 Version: $LATEST
'\n                    border-collapse'
END RequestId: 4ea4cdf8-69c6-4eb6-986d-f879c173eab4
REPORT RequestId: 4ea4cdf8-69c6-4eb6-986d-f879c173eab4	Duration: 2779.09 ms	Billed Duration: 2780 ms	Memory Size: 128 MB	Max Memory Used: 78 MB	Init Duration: 323.90 ms

Request ID
4ea4cdf8-69c6-4eb6-986d-f879c173eab4
~~~~












# PENDENTE
- V24 funciona, sem trazer sumário.
- V25 traz o sumário, mas consta ainda os "Vendor Severity" e as tabelas vieram sem bordas.
- Criar nova versão, corrigindo bordas da tabela e trazendo o sumário.
- Criar nova versão, fazendo com que o JSON convertido no HTML tenha sumários, resumo, melhor organização, etc. Separar por instance-id as findings???
- Separar por instance-id as findings???
- Instalar o "bs4 import BeautifulSoup" também, se necessário.
- Usar o código do base8, fazer todo o processo com sumário+conversão-html.
- Stop/Start na EC2
- Devolver ip elástico da EC2.
- Desativar Amazon Inspector antes do fim do Trial.
- Terminate EC2.
- Deletar funções Lambda.
- Documentar questões sobre Camadas para as Lambdas.





Ocorre erro:

Test Event Name
teste1

Response
{
  "statusCode": 500,
  "body": "{\"error\": \"'\\\\n                    border-collapse'\"}"
}

Function Logs
START RequestId: 4ea4cdf8-69c6-4eb6-986d-f879c173eab4 Version: $LATEST
'\n                    border-collapse'
END RequestId: 4ea4cdf8-69c6-4eb6-986d-f879c173eab4
REPORT RequestId: 4ea4cdf8-69c6-4eb6-986d-f879c173eab4	Duration: 2779.09 ms	Billed Duration: 2780 ms	Memory Size: 128 MB	Max Memory Used: 78 MB	Init Duration: 323.90 ms

Request ID
4ea4cdf8-69c6-4eb6-986d-f879c173eab4
ChatGPT

Peço desculpas pelo erro. Parece que há um problema de escape de caracteres no código fornecido anteriormente. Aqui está a versão corrigida:

~~~~python

import json
import json2html

def json_to_html(json_content):
    # Converte o conteúdo JSON para um dicionário Python
    data = json.loads(json_content)

    # Define o HTML completo, adicionando cabeçalho e rodapé
    html_content = """
    <html>
        <head>
            <title>Relatório JSON para HTML</title>
            <style>
                table {{
                    border-collapse: collapse;
                }}
                table, th, td {{
                    border: 1px solid black;
                }}
            </style>
        </head>
        <body>
            <h1>Relatório JSON para HTML</h1>
            {}
            <hr>
            <h2 id="summary_table">Sumário de Findings</h2>
            {}
            <p>Gerado automaticamente pela Lambda AWS</p>
        </body>
    </html>
    """

    # Cria um dicionário para armazenar o sumário
    summary = {"total": 0, "severity": {}, "vendorSeverity": {}}

    # Itera sobre cada finding no JSON e atualiza o sumário
    for finding in data["findings"]:
        summary["total"] += 1
        severity = finding["severity"]
        summary["severity"][severity] = summary["severity"].get(severity, 0) + 1
        vendor_severity = finding["packageVulnerabilityDetails"]["vendorSeverity"]
        summary["vendorSeverity"][vendor_severity] = summary["vendorSeverity"].get(vendor_severity, 0) + 1

    # Cria a tabela de sumário
    summary_table = "<table><tr><th></th><th>Total</th></tr>"
    for severity, count in summary["severity"].items():
        summary_table += "<tr><td>Severity {}</td><td>{}</td></tr>".format(severity, count)
    for vendor_severity, count in summary["vendorSeverity"].items():
        summary_table += "<tr><td>Vendor Severity {}</td><td>{}</td></tr>".format(vendor_severity, count)
    summary_table += "<tr><td>Total</td><td>{}</td></tr></table>".format(summary["total"])

    # Cria a tabela principal
    main_table = json2html.json2html.convert(json=data, table_attributes="id=\"findings_table\"")

    # Adiciona um link para a tabela de sumário
    main_table = main_table.replace("<body>", "<body><p><a href=\"#summary_table\">Ver Sumário de Findings</a></p>")

    # Insere as tabelas no HTML completo e retorna o resultado
    return html_content.format(main_table, summary_table)
~~~~

Tente usar esse código corrigido e verifique se o problema persiste.





- Criada v28
/home/fernando/cursos/lambdas-labs/json-to-html/python-lambdas/python-lambda28.py

- Testando, OK

Test Event Name
teste1

Response
{
  "statusCode": 200,
  "body": "{\"content\": \"{\\n    \\\"findings\



- Relatório formatado corretamente

file:///D:/OneDrive/Documents/Dev/Python/Lambdas/scan-interno-alternativa/reports-amazon-inspector/Python-testes/relatorio-final-28.html





# PENDENTE
- V24 funciona, sem trazer sumário.
- V28 ok, traz sumário e formatado.
- Criar nova versão, fazendo com que o JSON convertido no HTML tenha sumários, resumo, melhor organização, etc. Separar por instance-id as findings???
- Utilizar Pandas para fazer versão melhorada??
- Separar por instance-id as findings???
- Instalar o "bs4 import BeautifulSoup" também, se necessário.
- Usar o código do base8, fazer todo o processo com sumário+conversão-html.
- Stop/Start na EC2
- Devolver ip elástico da EC2.
- Desativar Amazon Inspector antes do fim do Trial.
- Terminate EC2.
- Deletar funções Lambda.
- Documentar questões sobre Camadas para as Lambdas.







# ###############################################################################################################################################################
# ###############################################################################################################################################################
# ###############################################################################################################################################################
# ###############################################################################################################################################################
# 
# Dia 19/05/2023


- Criar nova versão, fazendo com que o JSON convertido no HTML tenha sumários, resumo, melhor organização, etc. Separar por instance-id as findings???
- Utilizar Pandas para fazer versão melhorada??





Para remover os trechos que tratam sobre "Vendor Severity" da função json_to_html, você precisa fazer as seguintes alterações no código:

    Remova a seguinte linha:

python

summary = {"total": 0, "severity": {}, "vendorSeverity": {}}

    Modifique a linha abaixo:

python

summary["vendorSeverity"][vendor_severity] = summary["vendorSeverity"].get(vendor_severity, 0) + 1

para:

python

# Não faz nada, apenas ignora o "vendorSeverity"
pass

    Remova o seguinte trecho de código:

python

for vendor_severity, count in summary["vendorSeverity"].items():
    summary_table += "<tr><td>Vendor Severity {}</td><td>{}</td></tr>".format(vendor_severity, count)

    Modifique a linha abaixo:

python

summary_table += "<tr><td>Total</td><td>{}</td></tr></table>".format(summary["total"])

para:

python

summary_table += "<tr><td>Total</td><td>{}</td></tr></table>".format(summary["total"] - len(data["findings"]))

Isso deve remover a lógica relacionada ao "Vendor Severity" e ajustar a contagem total no resumo, considerando apenas a severidade.






DE:

    summary_table += "<tr><td>Total</td><td>{}</td></tr></table>".format(summary["total"])
PARA:
summary_table += "<tr><td>Total</td><td>{}</td></tr></table>".format(summary["total"] - len(data["findings"]))








fernando-teste	
i-0db6e68a367e54c2b
	
Terminated

Elastic IP addresses released.
Elastic IP addresses 35.169.22.123







Peço desculpas pelo equívoco. Se você deseja calcular o total de severidades, em vez de subtrair, você precisa ajustar a linha da seguinte maneira:

python

summary_table += "<tr><td>Total</td><td>{}</td></tr></table>".format(summary["total"])

Ao fazer essa alteração, o código irá exibir o número total de severidades encontradas no resumo, incluindo todas as severidades presentes nos findings.




- Editado:

/home/fernando/cursos/lambdas-labs/json-to-html/python-lambdas/python-lambda29.py



- Teste OK
trouxe o sumário corretamente

Sumário de Findings
	Total
Severity MEDIUM	2
Severity LOW	1
Total	3








## id

Para adicionar um quadro com o sumário por "id" junto com o sumário por "severity", você precisa fazer as seguintes alterações no código da função json_to_html:

    Modifique a linha abaixo:

python

summary = {"total": 0, "severity": {}}

para:

python

summary = {"total": 0, "severity": {}, "id": {}}

    Modifique a linha abaixo:

python

summary["severity"][severity] = summary["severity"].get(severity, 0) + 1

para:

python

summary["severity"][severity] = summary["severity"].get(severity, 0) + 1
summary_id = finding["findingArn"]
summary["id"][summary_id] = summary["id"].get(summary_id, 0) + 1

    Crie a tabela de sumário por "id" antes da tabela de sumário por "severity". Adicione o seguinte código antes de summary_table:

python

summary_id_table = "<h2 id=\"id_summary_table\">Sumário por ID</h2><table><tr><th>ID</th><th>Total</th></tr>"
for summary_id, count in summary["id"].items():
    summary_id_table += "<tr><td>{}</td><td>{}</td></tr>".format(summary_id, count)
summary_id_table += "</table>"

    Modifique a linha abaixo:

python

return html_content.format(main_table, summary_table)

para:

python

return html_content.format(main_table, summary_table + summary_id_table)

Após essas alterações, a função json_to_html criará um quadro adicional com o sumário por "id" no HTML gerado.




- Editado
/home/fernando/cursos/lambdas-labs/json-to-html/python-lambdas/python-lambda30.py


- Testando















ele sumarizou por findingArn ao invés de id da instancia, no caso o instance id, que faz parte do campo "id" no JSON.
ChatGPT

Peço desculpas pelo equívoco. Para corrigir o sumário por ID usando o campo "id" que contém o ID da instância, você precisa fazer as seguintes alterações no código da função json_to_html:

    Modifique a linha abaixo:

python

summary = {"total": 0, "severity": {}, "id": {}}

para:

python

summary = {"total": 0, "severity": {}, "instance_id": {}}

    Modifique a linha abaixo:

python

summary["severity"][severity] = summary["severity"].get(severity, 0) + 1

para:

python

summary["severity"][severity] = summary["severity"].get(severity, 0) + 1
summary_id = finding["resources"][0]["id"]
summary["instance_id"][summary_id] = summary["instance_id"].get(summary_id, 0) + 1

    Crie a tabela de sumário por ID usando o campo "instance_id". Adicione o seguinte código antes de summary_table:

python

summary_id_table = "<h2 id=\"id_summary_table\">Sumário por ID</h2><table><tr><th>ID da Instância</th><th>Total</th></tr>"
for summary_id, count in summary["instance_id"].items():
    summary_id_table += "<tr><td>{}</td><td>{}</td></tr>".format(summary_id, count)
summary_id_table += "</table>"

    Modifique a linha abaixo:

python

return html_content.format(main_table, summary_table + summary_id_table)

para:

python

return html_content.format(main_table, summary_table + "<br>" + summary_id_table)

Após essas alterações, a função json_to_html criará um quadro adicional com o sumário por ID usando o campo "instance_id" no HTML gerado.







- Editado
/home/fernando/cursos/lambdas-labs/json-to-html/python-lambdas/python-lambda30.py

- Trouxe

Sumário de Findings
	Total
Severity MEDIUM	2
Severity LOW	1
Total	3

Sumário por ID
ID da Instância	Total
i-0415ee9c35d4406ef	1
i-06b2f79a29da7746b	1
i-04e668b1627742918	1






# PENDENTE
- Organizar posição dos sumários e avaliar sumários interessantes.
- Utilizar Pandas para fazer versão melhorada??
- Separar por instance-id as findings???
- Instalar o "bs4 import BeautifulSoup" também, se necessário.
- Usar o código do base8, fazer todo o processo com sumário+conversão-html.
- Stop/Start na EC2
- Devolver ip elástico da EC2.
- Desativar Amazon Inspector antes do fim do Trial.
- Terminate EC2.
- Deletar funções Lambda.
- Documentar questões sobre Camadas para as Lambdas.







# ###############################################################################################################################################################
# ###############################################################################################################################################################
# ###############################################################################################################################################################
# ###############################################################################################################################################################
# 
# Dia 20/05/2023


- Organizar posição dos sumários e avaliar sumários interessantes.
- Utilizar Pandas para fazer versão melhorada??



/home/fernando/cursos/lambdas-labs/json-to-html/python-lambdas/python-lambda31.py


Aqui está a função adaptada para incluir uma coluna com o endereço IP no sumário organizado por ID e mover os sumários para o início do arquivo HTML:

python

def json_to_html(json_content):
    # Converte o conteúdo JSON para um dicionário Python
    data = json.loads(json_content)

    # Cria um dicionário para armazenar o sumário
    summary = {"total": 0, "severity": {}, "instance_id": {}}

    # Itera sobre cada finding no JSON e atualiza o sumário
    for finding in data["findings"]:
        summary["total"] += 1
        severity = finding["severity"]
        summary["severity"][severity] = summary["severity"].get(severity, 0) + 1
        summary_id = finding["resources"][0]["id"]
        summary["instance_id"][summary_id] = {
            "count": summary["instance_id"].get(summary_id, {}).get("count", 0) + 1,
            "ip": finding["resources"][0]["details"]["awsEc2Instance"]["ipV4Addresses"][0]
        }

    # Cria a tabela de sumário por id com a coluna de endereço IP
    summary_id_table = "<h2 id=\"id_summary_table\">Sumário por ID</h2><table><tr><th>ID da Instância</th><th>Endereço IP</th><th>Total</th></tr>"
    for summary_id, values in summary["instance_id"].items():
        summary_id_table += "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(summary_id, values["ip"], values["count"])
    summary_id_table += "</table>"

    # Cria a tabela de sumário
    summary_table = "<table><tr><th></th><th>Total</th></tr>"
    for severity, count in summary["severity"].items():
        summary_table += "<tr><td>Severity {}</td><td>{}</td></tr>".format(severity, count)
    summary_table += "<tr><td>Total</td><td>{}</td></tr></table>".format(summary["total"])

    # Cria a tabela principal
    main_table = json2html.json2html.convert(json=data, table_attributes="id=\"findings_table\"")

    # Adiciona um link para a tabela de sumário
    main_table = main_table.replace("<body>", "<body><p><a href=\"#summary_table\">Ver Sumário de Findings</a></p>")

    # Define o HTML completo, adicionando cabeçalho e rodapé
    html_content = """
    <html>
        <head>
            <title>Relatório JSON para HTML</title>
            <style>
                table {{
                    border-collapse: collapse;
                }}
                table, th, td {{
                    border: 1px solid black;
                }}
            </style>
        </head>
        <body>
            <h1>Relatório JSON para HTML</h1>
            <h2 id="summary_table">Sumário de Findings</h2>
            {}
            <hr>
            <h2 id="id_summary_table">Sumário por ID</h2>
            {}
            {}
            <p>Gerado automaticamente pela Lambda AWS</p>
        </body>
    </html>
    """

    # Insere as tabelas no HTML completo e retorna o resultado
    return html_content.format(summary_table + "<br>" + summary_id_table, main_table, summary_table + "<br>" + summary_id_table)

Essa função atualizada inclui a coluna "Endereço IP" na tabela de sumário por ID, buscando o valor do campo "ipV4Addresses" no JSON. Os sumários foram movidos para o início do arquivo HTML, conforme solicitado.






Aqui está a função adaptada para incluir uma coluna com o endereço IP no sumário organizado por ID e mover os sumários para o início do arquivo HTML:

python

def json_to_html(json_content):
    # Converte o conteúdo JSON para um dicionário Python
    data = json.loads(json_content)

    # Cria um dicionário para armazenar o sumário
    summary = {"total": 0, "severity": {}, "instance_id": {}}

    # Itera sobre cada finding no JSON e atualiza o sumário
    for finding in data["findings"]:
        summary["total"] += 1
        severity = finding["severity"]
        summary["severity"][severity] = summary["severity"].get(severity, 0) + 1
        summary_id = finding["resources"][0]["id"]
        summary["instance_id"][summary_id] = {
            "count": summary["instance_id"].get(summary_id, {}).get("count", 0) + 1,
            "ip": finding["resources"][0]["details"]["awsEc2Instance"]["ipV4Addresses"][0]
        }

    # Cria a tabela de sumário por id com a coluna de endereço IP
    summary_id_table = "<h2 id=\"id_summary_table\">Sumário por ID</h2><table><tr><th>ID da Instância</th><th>Endereço IP</th><th>Total</th></tr>"
    for summary_id, values in summary["instance_id"].items():
        summary_id_table += "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(summary_id, values["ip"], values["count"])
    summary_id_table += "</table>"

    # Cria a tabela de sumário
    summary_table = "<table><tr><th></th><th>Total</th></tr>"
    for severity, count in summary["severity"].items():
        summary_table += "<tr><td>Severity {}</td><td>{}</td></tr>".format(severity, count)
    summary_table += "<tr><td>Total</td><td>{}</td></tr></table>".format(summary["total"])

    # Cria a tabela principal
    main_table = json2html.json2html.convert(json=data, table_attributes="id=\"findings_table\"")

    # Adiciona um link para a tabela de sumário
    main_table = main_table.replace("<body>", "<body><p><a href=\"#summary_table\">Ver Sumário de Findings</a></p>")

    # Define o HTML completo, adicionando cabeçalho e rodapé
    html_content = """
    <html>
        <head>
            <title>Relatório JSON para HTML</title>
            <style>
                table {{
                    border-collapse: collapse;
                }}
                table, th, td {{
                    border: 1px solid black;
                }}
            </style>
        </head>
        <body>
            <h1>Relatório JSON para HTML</h1>
            <h2 id="summary_table">Sumário de Findings</h2>
            {}
            <hr>
            <h2 id="id_summary_table">Sumário por ID</h2>
            {}
            {}
            <p>Gerado automaticamente pela Lambda AWS</p>
        </body>
    </html>
    """

    # Insere as tabelas no HTML completo e retorna o resultado
    return html_content.format(summary_table + "<br>" + summary_id_table, main_table, summary_table + "<br>" + summary_id_table)

Essa função atualizada inclui a coluna "Endereço IP" na tabela de sumário por ID, buscando o valor do campo "ipV4Addresses" no JSON. Os sumários foram movidos para o início do arquivo HTML, conforme solicitado.
User
com este código, os sumários vieram 2 vezes, uma antes da tabela principal e outra vez ao final.
ChatGPT

Peço desculpas pelo erro. Foi uma duplicação acidental. Aqui está o código corrigido, onde os sumários são exibidos apenas uma vez no início do arquivo HTML:

python

def json_to_html(json_content):
    # Converte o conteúdo JSON para um dicionário Python
    data = json.loads(json_content)

    # Cria um dicionário para armazenar o sumário
    summary = {"total": 0, "severity": {}, "instance_id": {}}

    # Itera sobre cada finding no JSON e atualiza o sumário
    for finding in data["findings"]:
        summary["total"] += 1
        severity = finding["severity"]
        summary["severity"][severity] = summary["severity"].get(severity, 0) + 1
        summary_id = finding["resources"][0]["id"]
        ip_address = finding["resources"][0]["details"]["awsEc2Instance"]["ipV4Addresses"][0]
        if summary_id in summary["instance_id"]:
            summary["instance_id"][summary_id]["count"] += 1
        else:
            summary["instance_id"][summary_id] = {"count": 1, "ip": ip_address}

    # Cria a tabela de sumário por id com a coluna de endereço IP
    summary_id_table = "<h2 id=\"id_summary_table\">Sumário por ID</h2><table><tr><th>ID da Instância</th><th>Endereço IP</th><th>Total</th></tr>"
    for summary_id, values in summary["instance_id"].items():
        summary_id_table += "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(summary_id, values["ip"], values["count"])
    summary_id_table += "</table>"

    # Cria a tabela de sumário
    summary_table = "<table><tr><th></th><th>Total</th></tr>"
    for severity, count in summary["severity"].items():
        summary_table += "<tr><td>Severity {}</td><td>{}</td></tr>".format(severity, count)
    summary_table += "<tr><td>Total</td><td>{}</td></tr></table>".format(summary["total"])

    # Cria a tabela principal
    main_table = json2html.json2html.convert(json=data, table_attributes="id=\"findings_table\"")

    # Adiciona um link para a tabela de sumário
    main_table = main_table.replace("<body>", "<body><p><a href=\"#summary_table\">Ver Sumário de Findings</a></p>")

    # Define o HTML completo, adicionando cabeçalho e rodapé
    html_content = """
    <html>
        <head>
            <title>Relatório JSON para HTML</title>
            <style>
                table {{
                    border-collapse: collapse;
                }}
                table, th, td {{
                    border: 1px solid black;
                }}
            </style>
        </head>
        <body>
            <h1>Relatório JSON para HTML</h1>
            <h2 id="summary_table">Sumário de Findings</h2>
            {}
            <hr>
            <h2 id="id_summary_table">Sumário por ID</h2>
            {}
            {}
            <p>Gerado automaticamente pela Lambda AWS</p>
        </body>
    </html>
    """

    # Insere as tabelas no HTML completo e retorna o resultado
    return html_content.format(summary_table, summary_id_table, main_table)

Dessa forma, os sumários serão exibidos apenas uma vez no início do arquivo HTML, antes da tabela principal.





- Editado:
/home/fernando/cursos/lambdas-labs/json-to-html/python-lambdas/python-lambda31.py

- Teste OK

~~~~JSON
Test Event Name
teste1

Response
{
  "statusCode": 200,
  "body": "{\"content\
~~~~


- Arquivo em HTML traz os sumários e formata corretamente:

Relatório JSON para HTML
Sumário de Findings
	Total
Severity MEDIUM	2
Severity LOW	1
Total	3
Sumário por ID
ID da Instância	Endereço IP	Total
i-0415ee9c35d4406ef	172.30.4.168	1
i-06b2f79a29da7746b	172.30.4.98	1
i-04e668b1627742918	172.30.4.153	1

Gerado automaticamente pela Lambda AWS











# PANDAS
- Utilizar Pandas para fazer versão melhorada??




Sim, é possível utilizar a biblioteca Pandas para manipular os dados e criar sumários, gráficos e converter o resultado para PDF. Vou fornecer um exemplo de como fazer isso, explicando o código passo a passo e abordando as melhores práticas.

Antes de começar, certifique-se de ter instalado as bibliotecas pandas, matplotlib e reportlab no seu ambiente Python.

Aqui está o código utilizando Pandas para converter o JSON em um relatório em PDF:

~~~~python

import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def json_to_pdf(json_content):
    # Converte o conteúdo JSON para um DataFrame do Pandas
    data = pd.json_normalize(json.loads(json_content), "findings")

    # Cria um DataFrame para armazenar o sumário por ID
    summary_id = data["resources.details.awsEc2Instance.ipV4Addresses"].explode().rename("IP")
    summary_id = summary_id.groupby(data["resources.id"]).count().reset_index()

    # Cria um DataFrame para armazenar o sumário por severidade
    summary_severity = data["severity"].value_counts().reset_index().rename(columns={"index": "Severity", "severity": "Count"})

    # Cria um gráfico de pizza com o sumário por severidade
    plt.figure(figsize=(6, 6))
    plt.pie(summary_severity["Count"], labels=summary_severity["Severity"], autopct="%1.1f%%")
    plt.title("Summary by Severity")

    # Cria o documento PDF
    pdf_filename = "report.pdf"
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

    # Cria os estilos para o documento PDF
    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    table_style = TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), "#CCCCCC"),
        ("TEXTCOLOR", (0, 0), (-1, 0), "#000000"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 12),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
        ("BACKGROUND", (0, 1), (-1, -1), "#FFFFFF"),
        ("TEXTCOLOR", (0, 1), (-1, -1), "#000000"),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 1), (-1, -1), 11),
        ("TOPPADDING", (0, 1), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 6),
        ("BOX", (0, 0), (-1, -1), 1, "#000000"),
        ("GRID", (0, 0), (-1, -1), 1, "#000000"),
    ])

    # Cria o conteúdo do documento PDF
    content = []

    # Adiciona o título do relatório
    content.append(Paragraph("JSON to PDF Report", title_style))

    # Adiciona o sumário por ID
    content.append(Paragraph("Summary by ID", styles["Heading2"]))
    summary_id_table = Table([summary_id.columns] + summary_id.values.tolist())
    summary_id_table.setStyle(table_style)
    content.append(summary_id_table)

    # Adiciona o sumário por severidade
    content.append(Paragraph("Summary by Severity", styles["Heading2"]))
    summary_severity_table = Table([summary_severity.columns] + summary_severity.values.tolist())
    summary_severity_table.setStyle(table_style)
    content.append(summary_severity_table)

    # Adiciona o gráfico de pizza
    plt.savefig("pie_chart.png")
    content.append(Paragraph("<img src='pie_chart.png'/>", styles["BodyText"]))

    # Adiciona o rodapé
    content.append(Paragraph("Generated automatically by Python", styles["Footer"]))

    # Adiciona o conteúdo ao documento PDF
    doc.build(content)

    return pdf_filename
~~~~

Aqui estão as explicações dos principais passos:

    Importamos as bibliotecas necessárias: pandas, matplotlib, reportlab.
    Definimos a função json_to_pdf que recebe o conteúdo JSON como entrada.
    Convertemos o conteúdo JSON para um DataFrame do Pandas usando pd.json_normalize.
    Criamos um DataFrame summary_id para armazenar o sumário por ID. Usamos o método explode para lidar com múltiplos endereços IP por ID e em seguida, agrupamos e contamos os endereços IP.
    Criamos um DataFrame summary_severity para armazenar o sumário por severidade. Usamos o método value_counts para obter a contagem de cada severidade.
    Criamos um gráfico de pizza usando plt.pie com base no DataFrame summary_severity.
    Criamos o documento PDF usando SimpleDocTemplate e especificamos o tamanho da página como letter.
    Criamos os estilos para o documento PDF usando getSampleStyleSheet.
    Criamos uma lista vazia content para armazenar o conteúdo do documento PDF.
    Adicionamos o título do relatório usando Paragraph e o estilo de título.
    Adicionamos o sumário por ID criando uma tabela com o DataFrame summary_id usando Table e aplicamos o estilo de tabela definido anteriormente.
    Adicionamos o sumário por severidade criando uma tabela com o DataFrame summary_severity usando Table e aplicamos o estilo de tabela.
    Salvamos o gráfico de pizza como uma imagem PNG usando plt.savefig.
    Adicionamos o gráfico de pizza ao conteúdo do documento PDF usando Paragraph com a tag <img> para exibir a imagem.
    Adicionamos um rodapé ao relatório.
    Construímos o documento PDF com o conteúdo criado usando doc.build.
    Retornamos o nome do arquivo PDF gerado.

Essas são apenas algumas práticas recomendadas:

    Utilize o Pandas para manipular e analisar dados estruturados.
    Use gráficos apropriados para visualizar informações relevantes.
    Utilize estilos consistentes para tabelas e outros elementos no documento PDF.
    Divida o código em funções e componentes reutilizáveis para melhor legibilidade e manutenibilidade.
    Adicione comentários para explicar a lógica do código e fornecer informações úteis.
    Teste e valide seu código com diferentes conjuntos de dados para garantir que ele funcione corretamente.

Lembre-se de ajustar o código de acordo com suas necessidades específicas.










- Adaptando

Para adaptar o código para ler um arquivo JSON da máquina local em vez de um bucket do S3, você pode utilizar a função open do Python para abrir e ler o arquivo JSON localmente. Aqui está o código adaptado:

~~~~python

def lambda_handler(event, context):
    file_path = 'base1.json'  # Caminho para o arquivo JSON local
    
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Chamar a função que converte o JSON para HTML
        html_content = json_to_html(content)
        
        # Chamar a função que envia o arquivo HTML para o bucket S3
        put_html_to_s3(html_content)
        
        return {
            'statusCode': 200,
            'body': json.dumps({'content': content})
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
~~~~

Nesse código, a variável file_path é definida como o caminho para o arquivo JSON local que você deseja ler. Em seguida, a função open é usada para abrir o arquivo no modo de leitura ('r'). O conteúdo do arquivo é lido usando o método read() e armazenado na variável content.

A partir desse ponto, você pode chamar a função json_to_html e passar o content como argumento, assim como antes. O restante do código permanece o mesmo.

Lembre-se de substituir 'base1.json' pelo caminho correto para o seu arquivo JSON local. Certifique-se de que o arquivo esteja no mesmo diretório do script Python ou forneça o caminho absoluto para o arquivo.











# PENDENTE
- Utilizar Pandas para fazer versão melhorada??
- Instalar o "bs4 import BeautifulSoup" também, se necessário.
- Usar o código do base8, fazer todo o processo com sumário+conversão-html.
- Stop/Start na EC2
- Devolver ip elástico da EC2.
- Desativar Amazon Inspector antes do fim do Trial.
- Terminate EC2.
- Deletar funções Lambda.
- Documentar questões sobre Camadas para as Lambdas.
