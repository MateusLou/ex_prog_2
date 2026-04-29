
import random

def rolar_dados(n):
    dados = []
    for i in range(n):
        dados.append(random.randint(1, 6))
    return dados

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    valor = dados_rolados.pop(dado_para_guardar)
    dados_no_estoque.append(valor)
    return [dados_rolados, dados_no_estoque]