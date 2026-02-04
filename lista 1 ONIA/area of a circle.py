pi = 3.14159
continuar = True

while continuar:
    try:
        raio = float(input())
    except ValueError:
        print("Por favor, insira um número válido para o raio.")
        print("--------------------------------")
    else:
        A = pi * (raio ** 2.0)
        print(f"A={A:.4f}")
        continuar = False