import json

# Abra o arquivo JSON para leitura
with open('seuarquivo.json', 'r') as arquivo:
    # Carregue o conteúdo do arquivo JSON
    dados = json.load(arquivo)

# Especifique o atributo e o valor pelos quais você deseja filtrar
atributo_alvo = 'nome'
valor_alvo = 'Alice'

# Função para buscar o valor do atributo em estruturas aninhadas
def buscar_em_json(obj, target_attribute, target_value):
    resultados = []
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == target_attribute and value == target_value:
                resultados.append(obj)
            if isinstance(value, (dict, list)):
                resultados.extend(buscar_em_json(value, target_attribute, target_value))
    elif isinstance(obj, list):
        for item in obj:
            resultados.extend(buscar_em_json(item, target_attribute, target_value))
    return resultados

# Realize a busca pelo atributo com valor específico
resultados_filtrados = buscar_em_json(dados, atributo_alvo, valor_alvo)

# Agora, resultados_filtrados contém os objetos que atendem ao critério especificado
print(resultados_filtrados)