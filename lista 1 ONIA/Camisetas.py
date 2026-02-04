def corTamanho():
    resposta = input()
    valores = resposta.split()
    return valores
def saida(estudantes):
    ordem_tamanho = {"P": 0, "M": 1, "G": 2}
    estudantes.sort(key=lambda x: (x[0], ordem_tamanho[x[1]], x[2]))
    for cor, tamanho, nomeEstudante in estudantes:
        print(f"{cor} {tamanho} {nomeEstudante}")

primeiro = True

while True:    
    quantidadeCamisas = int(input()) # (1 ≤ N ≤ 60)
    if quantidadeCamisas == 0:
        break
    else:
        if primeiro == False:
            print()

        estudantes = []

        for i in range(quantidadeCamisas):
            nomeEstudante = input()
            resposta = corTamanho()
            cor = resposta[0] # branco / vermelho
            tamanho = resposta[1] # P / M / G
            estudantes.append((cor, tamanho, nomeEstudante))    
        saida(estudantes)
        primeiro = False