
import random

def rolar_dados(n):
    dados = []
    for i in range(n):
        dados.append(random.randint(1, 6))
    return dados