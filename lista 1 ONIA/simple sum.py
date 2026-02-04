try:
    A = int(input())
    B = int(input())
    
except ValueError:
    print("Por favor, insira números inteiros válidos.")
else:
    SOMA = A + B
    print(f"SOMA = {SOMA}")