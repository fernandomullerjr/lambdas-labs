import json
from json2html import json2html
from bs4 import BeautifulSoup

# Ler o arquivo JSON
with open('base1.json', 'r') as f:
    input_data = json.load(f)

# Converter o JSON para HTML
html_output = json2html.convert(json=input_data)

# Formatando o HTML com BeautifulSoup
soup = BeautifulSoup(html_output, 'html.parser')
html_output = soup.prettify()

# Salvar o resultado em um arquivo HTML
with open('base2-python.html', 'w') as f:
    f.write(html_output)