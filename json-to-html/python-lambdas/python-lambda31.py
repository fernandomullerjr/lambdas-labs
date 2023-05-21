# OK, trazendo sumario, tabelas com bordas OK, 
import json
import boto3
import json2html

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

def put_html_to_s3(html_content):
    s3 = boto3.resource('s3')
    bucket_name = 'devops-luxor'
    object_name = 'relatorio-final.html'
    
    try:
        s3.Bucket(bucket_name).put_object(Key=object_name, Body=html_content)
        print("Arquivo HTML salvo com sucesso!")
    except Exception as e:
        print(e)