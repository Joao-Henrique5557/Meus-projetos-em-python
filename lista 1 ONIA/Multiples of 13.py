X = int(input())
Y = int(input())
soma = 0

if X < Y:
    while X != Y + 1:
        if not X % 13 == 0:
            soma += X
        X += 1
else:
    while Y != X + 1:
        if not Y % 13 == 0:
            soma += Y
        Y += 1
print(soma)