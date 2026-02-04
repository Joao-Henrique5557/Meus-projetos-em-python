DDD = int(input())
listaDDD = {
    61: "Brasilia", 
    71: "Salvador",
    11: "Sao Paulo",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    19: "Campinas",
    27: "Vitoria",
    31: "Belo Horizonte"
}

for ddd in listaDDD:
    if ddd == DDD:
        print(listaDDD[ddd])
        break
else:
    print("DDD nao cadastrado")