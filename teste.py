import json

# Abra o arquivo JSON para leitura
with open('seuarquivo.json', 'r') as arquivo:
    # Carregue o conteúdo do arquivo JSON
    dados = json.load(arquivo)

# Especifique o atributo e o valor pelos quais você deseja filtrar
atributo_alvo = 'nome'
valor_alvo = 'Alice'

# Função para buscar o atributo em estruturas aninhadas
def buscar_em_json(obj, target):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == target:
                yield value
            if isinstance(value, (dict, list)):
                yield from buscar_em_json(value, target)
    elif isinstance(obj, list):
        for item in obj:
            yield from buscar_em_json(item, target)

# Realize a busca pelo atributo
resultados_filtrados = list(buscar_em_json(dados, atributo_alvo))

# Agora, resultados_filtrados contém os valores do atributo 'nome' em todas as estruturas aninhadas
print(resultados_filtrados)