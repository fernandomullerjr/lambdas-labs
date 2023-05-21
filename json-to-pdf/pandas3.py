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
