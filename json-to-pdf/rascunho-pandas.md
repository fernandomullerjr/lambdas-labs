
# ###############################################################################################################################################################
# ###############################################################################################################################################################
# ###############################################################################################################################################################
# ###############################################################################################################################################################
#  Git

git status
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git add .
git commit -m "Lambda Labs - JSON 2 PDF. Pandas"
git push
git status






# ###############################################################################################################################################################
# ###############################################################################################################################################################
# ###############################################################################################################################################################
# ###############################################################################################################################################################
#  
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













- Instalando

fernando@debian10x64:~$ sudo apt-get install python3-pandas
[sudo] password for fernando:
Reading package lists... Done
Building dependency tree
Reading state information... Done

The following additional packages will be installed:
  blt fonts-lyx libaec0 libblosc1 libhdf5-103 libjs-jquery-ui libsz2 python-matplotlib-data python-tables-data python3-bs4 python3-cycler
  python3-dateutil python3-decorator python3-html5lib python3-kiwisolver python3-lxml python3-matplotlib python3-numexpr python3-numpy
  python3-pandas-lib python3-pyparsing python3-scipy python3-soupsieve python3-tables python3-tables-lib python3-tk python3-tz
  python3-webencodings tk8.6-blt2.5 ttf-bitstream-vera
Suggested packages:
  blt-demo libjs-jquery-ui-docs python-cycler-doc python3-genshi python3-lxml-dbg python-lxml-doc dvipng ffmpeg inkscape ipython3
  python-matplotlib-doc python3-cairocffi python3-gobject python3-nose python3-pyqt4 python3-sip python3-tornado texlive-extra-utils
  texlive-latex-extra ttf-staypuft gfortran python-numpy-doc python3-pytest python3-numpy-dbg python-pandas-doc python-pyparsing-doc
  python-scipy-doc python-tables-doc python3-netcdf4 vitables python3-tk-dbg
The following NEW packages will be installed:
  blt fonts-lyx libaec0 libblosc1 libhdf5-103 libjs-jquery-ui libsz2 python-matplotlib-data python-tables-data python3-bs4 python3-cycler
  python3-dateutil python3-decorator python3-html5lib python3-kiwisolver python3-lxml python3-matplotlib python3-numexpr python3-numpy
  python3-pandas python3-pandas-lib python3-pyparsing python3-scipy python3-soupsieve python3-tables python3-tables-lib python3-tk python3-tz
  python3-webencodings tk8.6-blt2.5 ttf-bitstream-vera
0 upgraded, 31 newly installed, 0 to remove and 261 not upgraded.
Need to get 32.4 MB of archives.
After this operation, 132 MB of additional disk space will be used.
Do you want to continue? [Y/n] Y
Get:1 http://deb.debian.org/debian buster/main amd64 tk8.6-blt2.5 amd64 2.5.3+dfs




fernando@debian10x64:~$ sudo apt-get install python3-matplotlib
Reading package lists... Done
Building dependency tree
Reading state information... Done
python3-matplotlib is already the newest version (3.0.2-2).
python3-matplotlib set to manually installed.
The following packages were automatically installed and are no longer required:
  gyp libc-ares2 libjs-inherits libjs-is-typedarray libssl-dev libuv1 libuv1-dev no


fernando@debian10x64:~$ sudo apt-get install python3-reportlab
Reading package lists... Done
Building dependency tree
Reading state information... Done
python3-reportlab is already the newest version (3.5.13-1+deb10u1).
python3-reportlab set to manually installed.















Aqui está o código ajustado para ler um arquivo JSON local chamado "base1.json", fazer a conversão para PDF com base nesse arquivo e salvar o PDF na mesma pasta:

~~~~python

import pandas as pd
import matplotlib.pyplot as plt
import json
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        print(e)
        return None


def json_to_pdf(json_content, output_file):
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
    doc = SimpleDocTemplate(output_file, pagesize=letter)

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


def save_pdf_to_local(file_path, pdf_filename):
    try:
        with open(file_path, 'wb') as file:
            file.write(pdf_filename)
        print("PDF saved successfully!")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    json_file_path = "base1.json"
    output_pdf_file = "report.pdf"

    # Lê o arquivo JSON
    json_content = read_json_file(json_file_path)
    if json_content is not None:
        # Converte para PDF
        json_to_pdf(json_content, output_pdf_file)

        # Salva o PDF na mesma pasta do JSON local
        save_pdf_to_local(json_file_path, output_pdf_file)
~~~~

Nesse código, foram adicionadas duas novas funções:

    A função read_json_file(file_path) recebe o caminho do arquivo JSON local e lê o conteúdo do arquivo. Ela retorna o conteúdo do JSON ou None em caso de erro na leitura.
    A função save_pdf_to_local(file_path, pdf_filename) recebe o caminho do arquivo JSON local e o nome do arquivo PDF a ser salvo. Ela salva o conteúdo do PDF em um arquivo na mesma pasta do arquivo JSON.

No bloco if __name__ == "__main__":, você pode definir o caminho do arquivo JSON (json_file_path) e o nome do arquivo PDF de saída (output_pdf_file). O código irá ler o arquivo JSON, convertê-lo para PDF e salvar o PDF na mesma pasta do arquivo JSON local.

Para executar o código, salve-o em um arquivo Python (por exemplo, main.py) e certifique-se de ter o arquivo JSON (base1.json) no mesmo diretório do script. Em seguida, execute o script usando o interpretador Python 3. O PDF resultante será salvo na mesma pasta do arquivo JSON.

No terminal, você pode executar o script da seguinte maneira:

css

python3 main.py

Isso executará o script e mostrará a mensagem "PDF saved successfully!" se o PDF for salvo com êxito. Verifique a pasta para encontrar o arquivo PDF resultante.



Se você deseja utilizar um arquivo com um nome diferente de main.py, você precisa ajustar duas coisas:

    Renomeie o arquivo para o novo nome desejado. Por exemplo, se você deseja nomeá-lo como script.py, basta renomear o arquivo main.py para script.py.

    Certifique-se de executar o novo arquivo com o novo nome. No terminal, execute o novo arquivo da seguinte maneira:

    python3 script.py

    Substitua script.py pelo novo nome do arquivo que você escolheu.

Com essas duas alterações, você poderá utilizar um arquivo com um nome diferente do main.py e executá-lo normalmente. Certifique-se de que o restante do código permaneça o mesmo, incluindo as funções e a lógica necessárias para a conversão de JSON para PDF.





- ERRO

~~~~bash
fernando@debian10x64:~/cursos/lambdas-labs/json-to-pdf$ python3 /home/fernando/cursos/lambdas-labs/json-to-pdf/pandas2.py
Traceback (most recent call last):
  File "/home/fernando/cursos/lambdas-labs/json-to-pdf/pandas2.py", line 103, in <module>
    json_to_pdf(json_content, output_pdf_file)
  File "/home/fernando/cursos/lambdas-labs/json-to-pdf/pandas2.py", line 21, in json_to_pdf
    data = pd.json_normalize(json.loads(json_content), "findings")
AttributeError: module 'pandas' has no attribute 'json_normalize'
fernando@debian10x64:~/cursos/lambdas-labs/json-to-pdf$
~~~~







O erro que você está enfrentando indica que o módulo pandas não possui o atributo json_normalize. Isso pode acontecer se você estiver usando uma versão mais antiga do Pandas que não suporta essa função.

Certifique-se de que você está usando a versão correta do Pandas (1.0.0 ou superior) que inclui o método json_normalize. Você pode verificar a versão do Pandas instalada usando o seguinte código:

~~~~python

import pandas as pd
print(pd.__version__)
~~~~

Se a versão for anterior a 1.0.0, você precisará atualizar o Pandas para uma versão mais recente. Você pode fazer isso usando o gerenciador de pacotes pip. Execute o seguinte comando para atualizar o Pandas:

css

pip install --upgrade pandas

Depois de atualizar o Pandas, tente executar o código novamente e verifique se o erro foi resolvido.





~~~~bash
fernando@debian10x64:~/cursos/lambdas-labs/json-to-pdf$ python3 /home/fernando/cursos/lambdas-labs/json-to-pdf/teste-valida-versao-panda.py
0.23.3
fernando@debian10x64:~/cursos/lambdas-labs/json-to-pdf$
 



fernando@debian10x64:~/cursos/lambdas-labs/json-to-pdf$
fernando@debian10x64:~/cursos/lambdas-labs/json-to-pdf$ pip3 install pandas --no-build-isolation --upgrade
Collecting pandas
  Using cached https://files.pythonhosted.org/packages/99/f0/f99700ef327e51d291efdf4a6de29e685c4d198cbf8531541fc84d169e0e/pandas-1.3.5.tar.gz
    Complete output from command python setup.py egg_info:
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "/tmp/pip-install-wef2t_ki/pandas/setup.py", line 650, in <module>
        ext_modules=maybe_cythonize(extensions, compiler_directives=directives),
      File "/tmp/pip-install-wef2t_ki/pandas/setup.py", line 414, in maybe_cythonize
        raise RuntimeError("Cannot cythonize without Cython installed.")
    RuntimeError: Cannot cythonize without Cython installed.

    ----------------------------------------
Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-install-wef2t_ki/pandas/
fernando@debian10x64:~/cursos/lambdas-labs/json-to-pdf$
~~~~










https://pypi.org/











# PENDENTE
- Utilizar Pandas para fazer versão melhorada?? 
- Instalar numa Layer o seguinte: pandas, matplotlib, reportlab
    Seguir tutorial: https://sease.io/2022/11/how-to-import-pandas-in-aws-lambda.html
    <https://sease.io/2022/11/how-to-import-pandas-in-aws-lambda.html>
    https://pypi.org/project/pandas/#files
    https://towardsdatascience.com/how-to-create-pdf-reports-with-python-the-essential-guide-c08dd3ebf2ee
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
#  Dia 21/05/2023


- Utilizar Pandas para fazer versão melhorada?? 
- Instalar numa Layer o seguinte: pandas, matplotlib, reportlab
    Seguir tutorial: https://sease.io/2022/11/how-to-import-pandas-in-aws-lambda.html
    <https://sease.io/2022/11/how-to-import-pandas-in-aws-lambda.html>
    https://pypi.org/project/pandas/#files
    https://towardsdatascience.com/how-to-create-pdf-reports-with-python-the-essential-guide-c08dd3ebf2ee


https://sease.io/2022/11/how-to-import-pandas-in-aws-lambda.html

Create Layer Contents (locally)
Step 1: Download files from Python Package Index (PyPI)

The Python Package Index, abbreviated as PyPI, is the primary software repository for Python. We used it to download the Linux distributions of the necessary dependencies.

Since we created the lambda function using the Python 3.9 runtime and the default architecture, we need to make sure we download the wheels files with the right built distribution type; in particular, we need to look at:

    Python version –> cp39
    architecture –> x86_64

For operating ‘pandas’, you need to install two more required dependencies: ‘NumPy’ and ‘pytz’; so, for our purpose, we downloaded from PyPI these 3 files:

    pandas: pandas-1.4.3-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
    NumPy: numpy-1.23.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
    pytz: pytz-2022.2.1-py2.py3-none-any.whl





- Baixando

pandas-2.0.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (12.2 MB ver hashes)

Uploaded 24 de abr. de 2023 cp311

matplotlib-3.7.1-pp39-pypy39_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (7.5 MB ver hashes)

Uploaded 4 de mar. de 2023 pp39

reportlab-4.0.0-py3-none-any.whl (1.9 MB ver hashes)

Uploaded 4 de mai. de 2023 py3








- Criando Layer
pandas-matplotlib-reportlab-camadas
Layers contendo o Pandas - Matplotlib - ReportLab - 21-05-2023

pandas-matplotlib-reportlab-camadas
Create version

    Successfully created layer pandas-matplotlib-reportlab-camadas version 1.

All versions
Version
	
Version ARN
	
Description
1	arn:aws:lambda:us-east-1:261106957109:layer:pandas-matplotlib-reportlab-camadas:1	Layers contendo o Pandas - Matplotlib - ReportLab - 21-05-2023




- Adicionando a layer
Successfully updated the function json2pdf.










Aqui está o código adaptado com as alterações solicitadas:

~~~~python

import json
import boto3
import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

s3 = boto3.client('s3')
bucket_name = 'devops-luxor'
object_name = 'base1.json'

def lambda_handler(event, context):
    try:
        # Ler o JSON a partir do bucket do S3
        json_content = read_json_from_s3(bucket_name, object_name)
        
        # Converter para PDF
        pdf_content = json_to_pdf(json_content)
        
        # Salvar o PDF no bucket do S3
        put_pdf_to_s3(pdf_content)
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'PDF file generated and saved successfully.'})
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

def read_json_from_s3(bucket_name, object_name):
    response = s3.get_object(Bucket=bucket_name, Key=object_name)
    content = response['Body'].read().decode('utf-8')
    return content

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
    output_file = '/tmp/report.pdf'  # Path temporário para salvar o PDF
    doc = SimpleDocTemplate(output_file, pagesize=letter)

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
    plt.savefig("/tmp/pie_chart.png")  # Salva o gráfico em um path temporário
    content.append(Paragraph("<img src='/tmp/pie_chart.png'/>", styles["BodyText"]))

    # Adiciona o rodapé
    content.append(Paragraph("Generated automatically by Python", styles["Footer"]))

    # Adiciona o conteúdo ao documento PDF
    doc.build(content)

    # Lê o conteúdo do PDF
    with open(output_file, 'rb') as file:
        pdf_content = file.read()

    return pdf_content

def put_pdf_to_s3(pdf_content):
    object_name = 'relatorio-final.pdf'  # Nome do arquivo PDF no bucket do S3

    try:
        s3.put_object(Body=pdf_content, Bucket=bucket_name, Key=object_name)
        print("PDF file saved successfully!")
    except Exception as e:
        print(e)
~~~~

Este código divide as funcionalidades em três funções principais: read_json_from_s3 para ler o conteúdo JSON do bucket do S3, json_to_pdf para converter o JSON para PDF com o gráfico de pizza e os sumários, e put_pdf_to_s3 para salvar o arquivo PDF gerado no bucket do S3.

Certifique-se de substituir bucket_name pelo nome correto do seu bucket do S3. Além disso, note que utilizei caminhos temporários /tmp/ para salvar o arquivo PDF e a imagem do gráfico de pizza. Você pode ajustar esses caminhos conforme necessário.





- Testando:
/home/fernando/cursos/lambdas-labs/json-to-pdf/pandas3.py

- Erro

/home/fernando/cursos/lambdas-labs/json-to-pdf/pandas3.py

~~~~bash
Test Event Name
teste-pandas

Response
{
  "errorMessage": "Unable to import module 'pandas3': Unable to import required dependencies:\nnumpy: No module named 'numpy'\npytz: No module named 'pytz'",
  "errorType": "Runtime.ImportModuleError",
  "requestId": "e7e29706-f7cb-407c-bc1e-2507876389af",
  "stackTrace": []
}
~~~~






git status
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git add .
git commit -m "Lambda Labs - JSON 2 PDF - Pandas3, testando versão inicial. TSHOOT erro Unable to import required dependencies nnumpy No module named numpy"
git push
git status









- Baixando

https://pypi.org/project/numpy/#files

numpy-1.24.3-pp38-pypy38_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.7 MB ver hashes)

Uploaded 22 de abr. de 2023 pp38 





- Layer
criando version
Adicionando o NumPy

pandas-matplotlib-reportlab-camadas
Create version

    Successfully created layer pandas-matplotlib-reportlab-camadas version 2.
All versions
Version
	
Version ARN
	
Description
2	arn:aws:lambda:us-east-1:261106957109:layer:pandas-matplotlib-reportlab-camadas:2	Adicionando o NumPy
1	arn:aws:lambda:us-east-1:261106957109:layer:pandas-matplotlib-reportlab-camadas:1	Layers contendo o Pandas - Matplotlib - ReportLab - 21-05-2023



Successfully updated the function json2pdf.







- ERRO

~~~~BASH
Test Event Name
teste-pandas

Response
{
  "errorMessage": "Unable to import module 'pandas3': Unable to import required dependencies:\nnumpy: \n\nIMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!\n\nImporting the numpy C-extensions failed. This error can happen for\nmany reasons, often due to issues with your setup or how NumPy was\ninstalled.\n\nWe have compiled some common reasons and troubleshooting tips at:\n\n    https://numpy.org/devdocs/user/troubleshooting-importerror.html\n\nPlease note and check the following:\n\n  * The Python version is: Python3.8 from \"/var/lang/bin/python3.8\"\n  * The NumPy version is: \"1.24.3\"\n\nand make sure that they are the versions you expect.\nPlease carefully study the documentation linked above for further help.\n\nOriginal error was: No module named 'numpy.core._multiarray_umath'\n\npytz: No module named 'pytz'",
  "errorType": "Runtime.ImportModuleError",
  "stackTrace": []
}

Function Logs
START RequestId: 4e8f290f-9dbd-44af-908f-39183707d636 Version: $LATEST
[ERROR] Runtime.ImportModuleError: Unable to import module 'pandas3': Unable to import required dependencies:
numpy: 

IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the numpy C-extensions failed. This error can happen for
many reasons, often due to issues with your setup or how NumPy was
installed.

We have compiled some common reasons and troubleshooting tips at:

    https://numpy.org/devdocs/user/troubleshooting-importerror.html

Please note and check the following:

  * The Python version is: Python3.8 from "/var/lang/bin/python3.8"
  * The NumPy version is: "1.24.3"

and make sure that they are the versions you expect.
Please carefully study the documentation linked above for further help.

Original error was: No module named 'numpy.core._multiarray_umath'

pytz: No module named 'pytz'
Traceback (most recent call last):END RequestId: 4e8f290f-9dbd-44af-908f-39183707d636
REPORT RequestId: 4e8f290f-9dbd-44af-908f-39183707d636	Duration: 1.74 ms	Billed Duration: 2 ms	Memory Size: 128 MB	Max Memory Used: 54 MB	Init Duration: 294.23 ms

Request ID
4e8f290f-9dbd-44af-908f-39183707d636
~~~~








- GPT
O erro ocorre porque a biblioteca pandas requer a biblioteca numpy e a biblioteca pytz para funcionar corretamente. Parece que essas bibliotecas não estão instaladas no ambiente onde o código está sendo executado.

Uma possível solução para esse problema é empacotar todas as dependências necessárias, incluindo o numpy e o pytz, juntamente com o código da função Lambda e enviá-los como um pacote. Dessa forma, todas as dependências estarão disponíveis durante a execução da função.

Aqui estão os passos para criar um pacote com todas as dependências:

    Crie um diretório vazio para o projeto.
    No diretório do projeto, crie um ambiente virtual usando o comando python3 -m venv venv.
    Ative o ambiente virtual executando o comando source venv/bin/activate (Linux/macOS) ou venv\Scripts\activate (Windows).
    Instale as dependências necessárias executando o comando pip install pandas numpy pytz.
    Crie um arquivo vazio chamado __init__.py no diretório do projeto. Esse arquivo é necessário para indicar que o diretório é um pacote Python.
    Copie o código da função Lambda para um arquivo chamado lambda_function.py no diretório do projeto.
    Compacte todo o conteúdo do diretório do projeto, incluindo o ambiente virtual, em um arquivo zip. Certifique-se de que o arquivo zip não tenha um nível de diretório extra. Por exemplo, quando você extrair o arquivo zip, deve ver diretamente o ambiente virtual e o arquivo lambda_function.py na raiz do diretório extraído.
    Faça o upload do arquivo zip para a função Lambda.

Essas etapas garantem que todas as dependências necessárias estejam incluídas no pacote e disponíveis durante a execução da função Lambda.
User
ADICIONAR apenas o pytz a layer da Lambda, já que o numpy já está na Layer, resolveria?
ChatGPT

Sim, se o pacote numpy já estiver em uma camada (Layer) separada e você adicionar apenas a camada do pytz à sua função Lambda, isso resolveria o problema.

As camadas da AWS Lambda são uma forma de fornecer e gerenciar bibliotecas e dependências externas para suas funções sem incluí-las diretamente no pacote da função. Ao adicionar a camada do pytz, você estará fornecendo a biblioteca necessária para sua função Lambda.

Certifique-se de seguir as etapas a seguir:

    Crie uma camada Lambda separada contendo a biblioteca pytz.
    Abra a console da AWS e acesse o serviço AWS Lambda.
    Navegue até a página da sua função Lambda.
    Na seção "Configuração da função", role para baixo até a seção "Camadas".
    Clique em "Adicionar uma camada" e selecione a camada do pytz que você criou.
    Salve as alterações na função Lambda.
    Teste novamente sua função Lambda para verificar se o erro relacionado ao pytz foi resolvido.

Ao adicionar a camada separada do pytz, você garante que todas as dependências necessárias estejam disponíveis para a função Lambda durante a execução, resolvendo o erro que mencionou anteriormente.







- Criando nova version para Layer
https://pypi.org/project/pytz/#files

pytz-2023.3-py2.py3-none-any.whl (502.3 kB ver hashes)

Uploaded 29 de mar. de 2023 py2 py3


pandas-matplotlib-reportlab-camadas
Create version

    Successfully created layer pandas-matplotlib-reportlab-camadas version 3.
All versions
Version
	
Version ARN
	
Description
3	arn:aws:lambda:us-east-1:261106957109:layer:pandas-matplotlib-reportlab-camadas:3	Adicionando Pytz 













- ERRO

/home/fernando/cursos/lambdas-labs/json-to-pdf/pandas3.py

~~~~BASH
Test Event Name
teste-pandas

Response
{
  "errorMessage": "Unable to import module 'pandas3': Unable to import required dependencies:\nnumpy: \n\nIMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!\n\nImporting the numpy C-extensions failed. This error can happen for\nmany reasons, often due to issues with your setup or how NumPy was\ninstalled.\n\nWe have compiled some common reasons and troubleshooting tips at:\n\n    https://numpy.org/devdocs/user/troubleshooting-importerror.html\n\nPlease note and check the following:\n\n  * The Python version is: Python3.8 from \"/var/lang/bin/python3.8\"\n  * The NumPy version is: \"1.24.3\"\n\nand make sure that they are the versions you expect.\nPlease carefully study the documentation linked above for further help.\n\nOriginal error was: No module named 'numpy.core._multiarray_umath'\n",
  "errorType": "Runtime.ImportModuleError",
  "stackTrace": []
}

Function Logs
START RequestId: 91db972a-81e6-406b-a27a-e4ecad2523c1 Version: $LATEST
[ERROR] Runtime.ImportModuleError: Unable to import module 'pandas3': Unable to import required dependencies:
numpy: 

IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the numpy C-extensions failed. This error can happen for
many reasons, often due to issues with your setup or how NumPy was
installed.

We have compiled some common reasons and troubleshooting tips at:

    https://numpy.org/devdocs/user/troubleshooting-importerror.html

Please note and check the following:

  * The Python version is: Python3.8 from "/var/lang/bin/python3.8"
  * The NumPy version is: "1.24.3"

and make sure that they are the versions you expect.
Please carefully study the documentation linked above for further help.

Original error was: No module named 'numpy.core._multiarray_umath'

Traceback (most recent call last):END RequestId: 91db972a-81e6-406b-a27a-e4ecad2523c1
REPORT RequestId: 91db972a-81e6-406b-a27a-e4ecad2523c1	Duration: 1.65 ms	Billed Duration: 2 ms	Memory Size: 128 MB	Max Memory Used: 55 MB	Init Duration: 289.45 ms

Request ID
91db972a-81e6-406b-a27a-e4ecad2523c1
~~~~






- GPT

Adicionar apenas a camada do pytz não resolverá o problema, pois o erro menciona que a biblioteca numpy não pode ser importada corretamente.

Para corrigir esse problema, você precisa adicionar a camada que contém o numpy à sua função Lambda, juntamente com a camada do pytz. Certifique-se de que ambas as camadas estejam adicionadas corretamente na configuração da função Lambda.

Siga as etapas abaixo para adicionar ambas as camadas:

    Certifique-se de ter uma camada separada que contenha o numpy.
    Abra a console da AWS e acesse o serviço AWS Lambda.
    Navegue até a página da sua função Lambda.
    Na seção "Configuração da função", role para baixo até a seção "Camadas".
    Clique em "Adicionar uma camada" e selecione a camada do pytz que você criou.
    Clique em "Adicionar uma camada" novamente e selecione a camada que contém o numpy.
    Salve as alterações na função Lambda.
    Teste novamente sua função Lambda para verificar se o erro foi resolvido.

Ao adicionar ambas as camadas, você garantirá que tanto o numpy quanto o pytz estejam disponíveis para a função Lambda durante a execução, permitindo que o código seja executado corretamente.
User
como fazer o import do numpy e pytz no código?
ChatGPT

Para importar as bibliotecas numpy e pytz no seu código, você pode usar a seguinte sintaxe:

~~~~python

import numpy as np
import pytz
~~~~

Isso importará o numpy com o alias np, permitindo que você use suas funções e objetos prefixados com np. Por exemplo, você pode usar np.array() para criar um array do numpy.

O pytz pode ser importado diretamente sem um alias. Você pode usar suas funções e objetos diretamente pelo nome, como pytz.timezone() para obter um objeto de fuso horário.

Aqui está um exemplo de código que importa o numpy e o pytz:

~~~~python

import numpy as np
import pytz

# Usando o numpy
arr = np.array([1, 2, 3])
print(arr)

# Usando o pytz
timezone = pytz.timezone('America/New_York')
print(timezone)
~~~~

Certifique-se de ter instalado as bibliotecas numpy e pytz em seu ambiente Python antes de executar o código. Você pode instalá-las usando o pip. Por exemplo:

pip install numpy
pip install pytz

Lembre-se de que, ao usar as camadas do AWS Lambda, você não precisa se preocupar com a instalação das bibliotecas, pois elas já estão incluídas na camada.
















- Teste
/home/fernando/cursos/lambdas-labs/json-to-pdf/pandas4.py


- ERRO

~~~~BASH
Test Event Name
teste-pandas

Response
{
  "errorMessage": "Unable to import module 'pandas4': Unable to import required dependencies:\nnumpy: \n\nIMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!\n\nImporting the numpy C-extensions failed. This error can happen for\nmany reasons, often due to issues with your setup or how NumPy was\ninstalled.\n\nWe have compiled some common reasons and troubleshooting tips at:\n\n    https://numpy.org/devdocs/user/troubleshooting-importerror.html\n\nPlease note and check the following:\n\n  * The Python version is: Python3.8 from \"/var/lang/bin/python3.8\"\n  * The NumPy version is: \"1.24.3\"\n\nand make sure that they are the versions you expect.\nPlease carefully study the documentation linked above for further help.\n\nOriginal error was: No module named 'numpy.core._multiarray_umath'\n",
  "errorType": "Runtime.ImportModuleError",
  "stackTrace": []
}

Function Logs
START RequestId: cc85d947-22dd-46c8-a39c-087d965e481c Version: $LATEST
[ERROR] Runtime.ImportModuleError: Unable to import module 'pandas4': Unable to import required dependencies:
numpy: 

IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the numpy C-extensions failed. This error can happen for
many reasons, often due to issues with your setup or how NumPy was
installed.

We have compiled some common reasons and troubleshooting tips at:

    https://numpy.org/devdocs/user/troubleshooting-importerror.html

Please note and check the following:

  * The Python version is: Python3.8 from "/var/lang/bin/python3.8"
  * The NumPy version is: "1.24.3"

and make sure that they are the versions you expect.
Please carefully study the documentation linked above for further help.

Original error was: No module named 'numpy.core._multiarray_umath'

Traceback (most recent call last):END RequestId: cc85d947-22dd-46c8-a39c-087d965e481c
REPORT RequestId: cc85d947-22dd-46c8-a39c-087d965e481c	Duration: 1.50 ms	Billed Duration: 2 ms	Memory Size: 128 MB	Max Memory Used: 55 MB	Init Duration: 287.71 ms

Request ID
cc85d947-22dd-46c8-a39c-087d965e481c

~~~~














- GPT
ERRO


Original error was: No module named 'numpy.core._multiarray_umath'
ChatGPT

Esse erro geralmente ocorre quando há uma incompatibilidade entre as versões do numpy e do pandas que estão sendo usadas. Para resolver esse problema, você pode tentar algumas soluções:

    Certifique-se de que a versão do numpy que está sendo usada é compatível com a versão do pandas. Você pode verificar a versão do numpy instalada usando o comando np.__version__ após importar o numpy. Certifique-se de usar uma versão do numpy que seja compatível com o pandas. Se você estiver usando uma versão mais recente do numpy, pode tentar instalar uma versão mais antiga para resolver a incompatibilidade.

    Verifique se o pacote numpy está instalado corretamente em seu ambiente Python. Você pode usar o comando pip show numpy para verificar se o pacote está instalado e qual é a versão instalada. Se não estiver instalado, você pode instalá-lo usando o comando pip install numpy.

    Limpe o cache do AWS Lambda para garantir que as alterações feitas na camada estejam sendo aplicadas corretamente. Você pode fazer isso excluindo a camada existente e adicionando-a novamente à sua função Lambda.

    Se você estiver usando um ambiente virtual (por exemplo, virtualenv), verifique se o numpy está instalado corretamente dentro do ambiente virtual. Certifique-se de ativar o ambiente virtual antes de executar sua função Lambda.

    Se nenhuma das soluções acima resolver o problema, pode ser necessário recriar sua camada do Lambda, garantindo que as dependências corretas estejam incluídas na camada.

Tente aplicar essas soluções e veja se o erro persiste.





# PENDENTE
- TSHOOT erro no import Numpy. Ver versões PANDA vs NUMPY.
- Testar código para converter em PDF.

- Stop/Start na EC2
- Devolver ip elástico da EC2.
- Desativar Amazon Inspector antes do fim do Trial.
- Terminate EC2.
- Deletar funções Lambda.
- Documentar questões sobre Camadas para as Lambdas.












# DIA 03/06/2023

pandas-matplotlib-reportlab-camadas
Create version

    Successfully created layer pandas-matplotlib-reportlab-camadas version 4.


- Usando esta estrutura dentro do python.zip, deu erro:

matplotlib-3.7.1-cp38-cp38-manylinux_2_12_x86_64.manylinux2010_x86_64
numpy-1.24.3-pp38-pypy38_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64
pandas-2.0.2-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64
pytz-2023.3-py2.py3-none-any

- ERRO:

~~~~BASH
Test Event Name
teste-pandas

Response
{
  "errorMessage": "Unable to import module 'pandas4': No module named 'pandas'",
  "errorType": "Runtime.ImportModuleError",
  "stackTrace": []
}
~~~~







- TSHOOT
https://korniichuk.medium.com/lambda-with-pandas-fd81aa2ff25e


Baixando novamente os arquivos do pypi org - Baixando na versao 3-8 do python - Ajustando estrutura de pastas - 


pandas-matplotlib-reportlab-camadas
Create version

    Successfully created layer pandas-matplotlib-reportlab-camadas version 5.

- ERRO:

~~~~BASH
Test Event Name
teste-pandas

Response
{
  "errorMessage": "Unable to import module 'pandas4': Unable to import required dependencies:\nnumpy: \n\nIMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!\n\nImporting the numpy C-extensions failed. This error can happen for\nmany reasons, often due to issues with your setup or how NumPy was\ninstalled.\n\nWe have compiled some common reasons and troubleshooting tips at:\n\n    https://numpy.org/devdocs/user/troubleshooting-importerror.html\n\nPlease note and check the following:\n\n  * The Python version is: Python3.8 from \"/var/lang/bin/python3.8\"\n  * The NumPy version is: \"1.24.3\"\n\nand make sure that they are the versions you expect.\nPlease carefully study the documentation linked above for further help.\n\nOriginal error was: No module named 'numpy.core._multiarray_umath'\n",
  "errorType": "Runtime.ImportModuleError",
  "stackTrace": []
}

~~~~







- TSHOOT
https://stackoverflow.com/questions/54665842/when-importing-tensorflow-i-get-the-following-error-no-module-named-numpy-cor


- Novo teste
efetuando downgrade

DE:
numpy-1.24.3-pp38-pypy38_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64

PARA:
numpy-1.21.0-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64


- Criando nova layer
Baixando novamente os arquivos do pypi org - Baixando na versao 3-8 do python - Ajustando estrutura de pastas - Downgrade do numpy para 1-21

pandas-matplotlib-reportlab-camadas
Create version

    Successfully created layer pandas-matplotlib-reportlab-camadas version 6.



- ERRO, novo erro:

~~~~BASH
Test Event Name
teste-pandas

Response
{
  "errorMessage": "Unable to import module 'pandas4': No module named 'packaging'",
  "errorType": "Runtime.ImportModuleError",
  "stackTrace": []
}
~~~~





- Ajustando:
/home/fernando/cursos/lambdas-labs/json-to-pdf/pandas4.py

- Adicionando:
import packaging

- Criando nova version da Layer:
Baixando novamente os arquivos do pypi org - Baixando na versao 3-8 do python - Ajustando estrutura de pastas - Downgrade do numpy para 1-21 - add packaging

pandas-matplotlib-reportlab-camadas
Create version

    Successfully created layer pandas-matplotlib-reportlab-camadas version 7.


- Novo erro:

~~~~BASH
Test Event Name
teste-pandas

Response
{
  "errorMessage": "Unable to import module 'pandas4': No module named 'PIL'",
  "errorType": "Runtime.ImportModuleError",
  "stackTrace": []
}

~~~~









preciso de um código em Python para AWS Lambda, contendo 4 funções
1 função que vai ler um arquivo JSON a partir de um bucket do S3.
1 Função que vai converter o JSON para PDF utilizando o pandas.
1 função que vai enviar o PDF convertido para o bucket do S3 com um nome relatorio-final-pdf.pdf
1 função que vai ser o lambda_handler, chamando as funções que foram criadas.

Preciso que o código seja simples e não tenha muitas dependencias e bibliotecas adicionais.
ChatGPT

Aqui está um exemplo de código em Python para AWS Lambda que atende aos requisitos mencionados:

python

import boto3
import json
import pandas as pd
import pdfkit

s3 = boto3.client('s3')

def read_json_from_s3(bucket, key):
    response = s3.get_object(Bucket=bucket, Key=key)
    json_data = response['Body'].read().decode('utf-8')
    return json.loads(json_data)

def convert_json_to_pdf(json_data):
    df = pd.DataFrame(json_data)
    html = df.to_html()
    pdfkit.from_string(html, '/tmp/relatorio.pdf')

def upload_pdf_to_s3(bucket, key):
    s3.upload_file('/tmp/relatorio.pdf', bucket, key)

def lambda_handler(event, context):
    # Define o bucket do S3 e o caminho do arquivo JSON
    bucket = 'seu-bucket'
    json_key = 'caminho/do/arquivo.json'

    # Lê o arquivo JSON do S3
    json_data = read_json_from_s3(bucket, json_key)

    # Converte o JSON para PDF utilizando o pandas
    convert_json_to_pdf(json_data)

    # Define o nome do arquivo PDF convertido
    pdf_key = 'relatorio-final-pdf.pdf'

    # Envia o PDF convertido para o S3
    upload_pdf_to_s3(bucket, pdf_key)

Este código utiliza as bibliotecas boto3, json, pandas e pdfkit. Certifique-se de ter instalado o pandas e o pdfkit no ambiente em que você está executando o código.

Além disso, é importante configurar corretamente as permissões e credenciais no ambiente em que você está executando o código para permitir acesso ao S3 e às operações de leitura, gravação e upload de arquivos.

Lembre-se de substituir 'seu-bucket' pelo nome do seu bucket S3 e 'caminho/do/arquivo.json' pelo caminho correto do arquivo JSON dentro do seu bucket.






# PENDENTE
- Testar código para converter em PDF.

- Stop/Start na EC2
- Devolver ip elástico da EC2.
- Desativar Amazon Inspector antes do fim do Trial.
- Terminate EC2.
- Deletar funções Lambda.
- Documentar questões sobre Camadas para as Lambdas.



