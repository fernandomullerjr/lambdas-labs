
# ###############################################################################################################################################################
# ###############################################################################################################################################################
# ###############################################################################################################################################################
# ###############################################################################################################################################################
#  Git

git status
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git add .
git commit -m "Lambda Labs - JSON 2 PDF"
git push
git status


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

python

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


fernando@debian10x64:~/cursos/lambdas-labs/json-to-pdf$ python3 /home/fernando/cursos/lambdas-labs/json-to-pdf/pandas2.py
Traceback (most recent call last):
  File "/home/fernando/cursos/lambdas-labs/json-to-pdf/pandas2.py", line 103, in <module>
    json_to_pdf(json_content, output_pdf_file)
  File "/home/fernando/cursos/lambdas-labs/json-to-pdf/pandas2.py", line 21, in json_to_pdf
    data = pd.json_normalize(json.loads(json_content), "findings")
AttributeError: module 'pandas' has no attribute 'json_normalize'
fernando@debian10x64:~/cursos/lambdas-labs/json-to-pdf$








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
