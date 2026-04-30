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


def organiza_tags(texto):
    tags = texto.split(',')
    tags_limpas = []
    for tag in tags:
        tag = tag.strip()         
        tag = tag.lower()              
        if tag == '':
            continue
        if tag[0] == '#':
            tag = tag[1:]
        tag = tag.replace(' ', '-')
        if tag == '':
            continue
        tags_limpas.append(tag)
    return ';'.join(tags_limpas)


def processa_dna(lista):
    contagem = {"A": 0, "T": 0, "C": 0, "G": 0}
    for sequencia in lista:
        if sequencia.find('*') != -1:
            continue
        numero_str = ""
        for c in sequencia:
            if c in '0123456789':
                numero_str = numero_str + c
            else:
                if numero_str == "":
                    quantidade = 1
                else:
                    quantidade = int(numero_str)
                if c in contagem:
                    contagem[c] += quantidade
                numero_str = ""
    return contagem


def calcula_pontos_full_house(dados):
    contagens = []
    for face in range(1, 7):
        contagens.append(dados.count(face))
    if 3 in contagens and 2 in contagens:
        soma = 0
        for d in dados:
            soma = soma + d
        return soma
    else:
        return 0
    
def calcula_pontos_quadra(dados):
    for valor in dados:
        if dados.count(valor) >= 4:
            soma = 0
            for d in dados:
                soma +=  d
            return soma
    return 0

def calcula_pontos_quina(dados):
    for valor in dados:
        contador = 0
        for d in dados:
            if d == valor:
                contador += 1
        if contador >= 5:
            return 50
    return 0

def calcula_pontos_regra_avancada(dados):
    return {
        'cinco_iguais': calcula_pontos_quina(dados),
        'full_house': calcula_pontos_full_house(dados),
        'quadra': calcula_pontos_quadra(dados),
        'sem_combinacao': calcula_pontos_soma(dados),
        'sequencia_alta': calcula_pontos_sequencia_alta(dados),
        'sequencia_baixa': calcula_pontos_sequencia_baixa(dados),
    }





