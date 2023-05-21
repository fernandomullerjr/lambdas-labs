
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