import json
from json2html import json2html
from bs4 import BeautifulSoup

# Carregando o JSON
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

# Criando o sumário em HTML
summary_html = '<h2>Summary:</h2>'
for severity, data in summary.items():
    findings = data['findings']
    summary_html += f'<h3>Severity: {severity}</h3>'
    summary_html += f'Total findings: {len(findings)}<br>'
    for finding in findings:
        summary_html += f'Finding: {finding["title"]}<br>'

# Criando o HTML dos findings
findings_html = json2html.convert(json = data)

# Criando o objeto BeautifulSoup
soup = BeautifulSoup('', 'html.parser')

# Adicionando o sumário e os findings ao objeto BeautifulSoup
soup.body.append(BeautifulSoup(summary_html, 'html.parser'))
soup.body.append(BeautifulSoup(findings_html, 'html.parser'))

# Salvando o HTML em um arquivo
with open('base4.html', 'w') as f:
    f.write(str(soup))
