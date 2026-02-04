ano = 365
mes = 30

try:
    dias = int(input())

    inYears = dias/ano
    inMonths = (dias % ano)/mes
    inDays = (dias % ano) % mes

    if inMonths > 12: 
        inMonths = inMonths -12
    else:
        inMonths = int(inMonths)

    print(f"{int(inYears)} ano(s)")
    print(f"{int(inMonths)} mes(es)")
    print(f"{inDays} dia(s)")
except ValueError:
    print("Por favor, insira um número válido de dias.")