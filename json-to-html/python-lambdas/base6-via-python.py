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

# Criar o HTML sumarizado
summary_html = ''
for severity, data in summary.items():
    findings = data['findings']
    summary_html += f'<h2>Summary for severity {severity}:</h2>\n'
    summary_html += f'<p>Total findings: {len(findings)}</p>\n'
    for finding in findings:
        summary_html += f'<p>Finding: {finding["title"]}</p>\n'

# Converter o JSON para HTML
html_output = json2html.convert(json=input_data)

# Formatando o HTML com BeautifulSoup
soup = BeautifulSoup(html_output, 'html.parser')
html_output = soup.prettify()

# Adicionar o HTML sumarizado ao início do documento
summary_tag = soup.new_tag('div', **{'class': 'summary'})
summary_tag.append(BeautifulSoup(summary_html, 'html.parser'))
soup.insert(0, summary_tag)

# Salvar o resultado em um arquivo HTML
with open('base6-python.html', 'w') as f:
    f.write(html_output)
