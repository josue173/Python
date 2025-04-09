import random

numero_aleatorio = random.randint(0,10)
print(numero_aleatorio)

while True:
    adivinar_numero = input("Dame un número de 1 a 10: ")
    if int(adivinar_numero) == numero_aleatorio:
        print("¡Adivinaste el número!")
        break
    else:
        print(':( Sigue intentando)')

