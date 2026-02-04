# Debugar no vscode
# - criar um break point
# f5 - iniciar debug. selecionar arquivo atual
# f10 - pular linha
# f11 - entrar dentro do método
# shift f11 - sair do bloco atual



def chamarNome(nome):
    print(f"Ola, {nome}")

isOn = True

while isOn == True:
    nome = input("Qual o nome: ")
    chamarNome(nome)
    res = input("Continuar? ")
    if res == "s":
        continue
    elif res == "n":
        isOn = False