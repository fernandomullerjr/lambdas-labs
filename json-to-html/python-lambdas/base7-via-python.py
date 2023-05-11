import json
from json2html import json2html
from bs4 import BeautifulSoup

# Ler o arquivo JSON
with open('base1.json', 'r') as f:
    input_data = json.load(f)

# Dicionário para manter o controle dos findings por severity
summary = {}

# Loop pelos findings
for finding in input_data['findings']:
    # Obtendo a severity
    severity = finding['severity']
    # Adicionando o finding ao dicionário
    if severity in summary:
        summary[severity]['findings'].append(finding)
    else:
        summary[severity] = {'findings': [finding]}

# Converter o JSON para HTML
html_output = json2html.convert(json=input_data)

# Adicionar o sumário ao HTML
summary_html = '<h1>Summary</h1>'
for severity, data in summary.items():
    findings = data['findings']
    summary_html += f'<h2>Summary for severity {severity}</h2>'
    summary_html += f'<p>Total findings: {len(findings)}</p>'
    summary_html += '<ul>'
    for finding in findings:
        summary_html += f'<li>{finding["title"]}</li>'
    summary_html += '</ul>'

# Concatenar o sumário e o conteúdo do JSON em um só HTML
html_output = summary_html + html_output

# Formatando o HTML com BeautifulSoup
soup = BeautifulSoup(html_output, 'html.parser')
html_output = soup.prettify()

# Salvar o resultado em um arquivo HTML
with open('base7-python.html', 'w') as f:
    f.write(html_output)

# Salvar o resultado em um arquivo HTML
with open('resultado.html', 'w') as f:
    f.write(str(soup))