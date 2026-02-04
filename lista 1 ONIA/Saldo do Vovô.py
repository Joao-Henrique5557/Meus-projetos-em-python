# Variaveis
entrada = input()
valores = entrada.split()
movimentacoes = []

numeroDias = int(valores[0])
saldoDaConta = int(valores[1])

for i in range(numeroDias):
    # salvar as movimentações
    movimentacao = int(input()) # pega cada uma das movimentações
    movimentacoes.append(movimentacao) # inicia a lista de movimentações

menorValor = saldoDaConta

for i in range(numeroDias):
    saldoDaConta += movimentacoes[i]

    if saldoDaConta < menorValor:
        menorValor = saldoDaConta

# 800
# 900 -> continue
# 700 -> menorValor = 700
# 500 -> menorValor = 500
# 700 -> continue

print(menorValor)