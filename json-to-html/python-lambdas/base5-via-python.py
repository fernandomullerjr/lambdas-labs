
import json
from json2html import json2html
from bs4 import BeautifulSoup

# Ler o arquivo JSON
with open('base1.json', 'r') as f:
    data = json.load(f)

# Dicionário para manter o controle dos findings por severity
summary = {}

# Loop pelos findings
for finding in data['findings']:
    # Obtendo a severity
    severity = finding['severity']
    # Adicionando o finding ao dicionário
    if severity in summary:
        summary[severity]['findings'].append(finding)
    else:
        summary[severity] = {'findings': [finding]}

# Converter o JSON para HTML
html_output = json2html.convert(json=data)

# Formatando o HTML com BeautifulSoup
soup = BeautifulSoup(html_output, 'html.parser')

# Adicionando o sumário no começo do HTML
summary_html = '<h1>Summary</h1>'
for severity, data in summary.items():
    findings = data['findings']
    summary_html += f'<h2>Summary for severity {severity}:</h2>'
    summary_html += f'<p>Total findings: {len(findings)}</p>'
    summary_html += '<ul>'
    for finding in findings:
        summary_html += f'<li>{finding["title"]}</li>'
    summary_html += '</ul>'
summary_html = BeautifulSoup(summary_html, 'html.parser')
soup.body.insert(0, summary_html)

# Salvando o resultado em um arquivo HTML
with open('base5.html', 'w') as f:
    f.write(str(soup))