from funcoes import (
    rolar_dados,
    guardar_dado,
    remover_dado,
    faz_jogada,
    imprime_cartela,
)


def jogar():
    # ------------------------------------------------------------------
    # Estado inicial da cartela.
    # Convenção: -1 significa "linha ainda não preenchida".
    # A ordem das chaves de 'regra_avancada' define a ordem em que
    # imprime_cartela vai exibi-las (dicts em Python 3.7+ mantêm ordem).
    # ------------------------------------------------------------------
    cartela = {
        'regra_simples': {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1},
        'regra_avancada': {
            'sem_combinacao': -1,
            'quadra': -1,
            'full_house': -1,
            'sequencia_baixa': -1,
            'sequencia_alta': -1,
            'cinco_iguais': -1,
        },
    }

    # Conjuntos para validar rapidamente o nome da combinação.
    combinacoes_simples_validas = {'1', '2', '3', '4', '5', '6'}
    combinacoes_avancadas_validas = set(cartela['regra_avancada'].keys())

    # Mostra a cartela vazia no início, igual ao exemplo de execução.
    imprime_cartela(cartela)

    # ------------------------------------------------------------------
    # Loop externo: 12 rodadas.
    # ------------------------------------------------------------------
    for _ in range(12):
        # Estado inicial da rodada.
        dados_rolados = rolar_dados(5)
        dados_guardados = []
        rerolagens_usadas = 0
        rodada_terminou = False

        # --------------------------------------------------------------
        # Loop da rodada: roda até o jogador marcar pontuação com sucesso.
        # --------------------------------------------------------------
        while not rodada_terminou:
            # Reimprime o estado antes de pedir uma nova ação.
            print(f"Dados rolados: {dados_rolados}")
            print(f"Dados guardados: {dados_guardados}")
            print(
                "Digite 1 para guardar um dado, 2 para remover um dado, "
                "3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:"
            )

            # Lê a opção até receber uma válida.
            # Importante: NÃO reimprimimos o estado aqui — apenas relemos.
            while True:
                opcao = input()
                if opcao in {'0', '1', '2', '3', '4'}:
                    break
                print("Opção inválida. Tente novamente.")

            # ----------------------------------------------------------
            # Opção 1: Guardar um dado
            # ----------------------------------------------------------
            if opcao == '1':
                print("Digite o índice do dado a ser guardado (0 a 4):")
                indice = int(input())
                dados_rolados, dados_guardados = guardar_dado(
                    dados_rolados, dados_guardados, indice
                )

            # ----------------------------------------------------------
            # Opção 2: Remover um dado guardado (volta para "rolados")
            # ----------------------------------------------------------
            elif opcao == '2':
                print("Digite o índice do dado a ser removido (0 a 4):")
                indice = int(input())
                dados_rolados, dados_guardados = remover_dado(
                    dados_rolados, dados_guardados, indice
                )

            # ----------------------------------------------------------
            # Opção 3: Rerrolar (no máximo 2 vezes por rodada)
            # Apenas os dados não guardados são re-sorteados.
            # ----------------------------------------------------------
            elif opcao == '3':
                if rerolagens_usadas >= 2:
                    print("Você já usou todas as rerrolagens.")
                else:
                    dados_rolados = rolar_dados(len(dados_rolados))
                    rerolagens_usadas += 1

            # ----------------------------------------------------------
            # Opção 4: Mostrar a cartela atual
            # ----------------------------------------------------------
            elif opcao == '4':
                imprime_cartela(cartela)

            # ----------------------------------------------------------
            # Opção 0: Marcar pontuação (encerra a rodada se válida)
            # ----------------------------------------------------------
            else:  # opcao == '0'
                print("Digite a combinação desejada:")

                # Loop até receber uma combinação válida e ainda não usada.
                while True:
                    combinacao = input()

                    eh_avancada = combinacao in combinacoes_avancadas_validas
                    eh_simples = combinacao in combinacoes_simples_validas

                    # Caso 1: nome não corresponde a nenhuma combinação.
                    if not eh_avancada and not eh_simples:
                        print("Combinação inválida. Tente novamente.")
                        continue

                    # Caso 2: combinação válida, mas linha já preenchida.
                    if eh_avancada:
                        ja_preenchida = cartela['regra_avancada'][combinacao] != -1
                    else:
                        ja_preenchida = cartela['regra_simples'][int(combinacao)] != -1

                    if ja_preenchida:
                        print("Essa combinação já foi utilizada.")
                        continue

                    # Caso 3: tudo certo — calcula e marca a pontuação.
                    # Os 5 dados (rolados + guardados) entram no cálculo.
                    todos_os_dados = dados_rolados + dados_guardados
                    cartela = faz_jogada(todos_os_dados, combinacao, cartela)
                    rodada_terminou = True
                    break

    # ------------------------------------------------------------------
    # Fim do jogo: cálculo da pontuação final.
    # ------------------------------------------------------------------
    soma_simples = 0
    for face in range(1, 7):
        if cartela['regra_simples'][face] != -1:
            soma_simples += cartela['regra_simples'][face]

    # Bônus: 35 pontos extras se a soma das regras simples for >= 63.
    bonus = 35 if soma_simples >= 63 else 0

    soma_avancada = 0
    for chave in cartela['regra_avancada']:
        if cartela['regra_avancada'][chave] != -1:
            soma_avancada += cartela['regra_avancada'][chave]

    pontuacao_total = soma_simples + bonus + soma_avancada

    imprime_cartela(cartela)
    print(f"Pontuação total: {pontuacao_total}")


jogar()