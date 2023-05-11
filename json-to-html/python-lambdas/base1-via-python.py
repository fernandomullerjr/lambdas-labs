import json
from json2html import *

# Ler o arquivo JSON
with open('base1.json') as f:
    input_data = json.load(f)

# Converter para HTML
html_output = json2html.convert(json=input_data)

# Salvar o resultado em um arquivo HTML
with open('base1-python.html', 'w') as f:
    f.write(html_output)
