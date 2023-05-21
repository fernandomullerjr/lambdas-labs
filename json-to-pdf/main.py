def process_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return {'content': content}
    except Exception as e:
        print(e)
        return {'error': str(e)}

if __name__ == "__main__":
    file_path = 'base1.json'  # Caminho para o arquivo JSON local
    result = process_json_file(file_path)
    print(result)
