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



def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    valor = dados_no_estoque.pop(dado_para_remover)
    dados_rolados.append(valor)
    return [dados_rolados, dados_no_estoque]


def calcula_pontos_regra_simples(dados):
    pontos = {}
    for face in range(1, 7):
        soma = 0
        for d in dados:
            if d == face:
                soma += d
        pontos[face] = soma
    return pontos




def calcula_pontos_soma(dados):
    soma = 0
    for d in dados:
        soma += d
    return soma

def calcula_pontos_sequencia_baixa(dados):
    sequencias = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
    for seq in sequencias:
        encontrou = True
        for valor in seq:
            if valor not in dados:
                encontrou = False
                break
        if encontrou:
            return 15
    return 0

def calcula_pontos_sequencia_alta(dados):
    sequencias = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
    for seq in sequencias:
        encontrou = True
        for valor in seq:
            if valor not in dados:
                encontrou = False
                break
        if encontrou:
            return 30
    return 0





