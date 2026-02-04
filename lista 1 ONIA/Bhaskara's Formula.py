entrada = input()
valores = entrada.split()

A = float(valores[0])
B = float(valores[1])
C = float(valores[2])

if A == 0:
    print("Impossivel calcular")
else:
    delta = B ** 2 - 4 * A * C

    if delta < 0:
        print("Impossivel calcular")
    else:
        R1 = (-B + delta ** 0.5)/(2 * A)
        R2 = (-B - delta ** 0.5)/(2 * A)

        print(f"R1 = {R1:.5f}")
        print(f"R2 = {R2:.5f}")