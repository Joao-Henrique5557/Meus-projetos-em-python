vogais = ["a", "e", "i", "o", "u"]

risada = input()
risadaSemConsoante = ""
risadaSemConsoanteInvertida = ""
isFun = None

for letra in risada:
    if letra in vogais:
        risadaSemConsoante += letra

tamanhoRisada = len(risadaSemConsoante)
i = 0

while i < tamanhoRisada:
    risadaSemConsoanteInvertida += risadaSemConsoante[tamanhoRisada - 1]
    tamanhoRisada -= 1

if risadaSemConsoante == risadaSemConsoanteInvertida:
    isFun = "S"
else:
    isFun = "N"

print(isFun)