import json

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

# Exibindo o sumário por severity
for severity, data in summary.items():
    findings = data['findings']
    print(f'Summary for severity {severity}:')
    print(f'Total findings: {len(findings)}')
    for finding in findings:
        print(f'Finding: {finding["title"]}')