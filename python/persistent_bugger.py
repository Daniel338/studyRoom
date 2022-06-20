"""
Write a function, persitence, that takes in a positive parameter num and
returns its multiplicative persistence, which is the number of times you must
multiply the digits in num until you reach a single digit.
"""

from os import system

system("cls")


def persitence(num):
    persistencia_multiplicativa = 0

    multiplicacion = 1
    numeros = str(num)
    while len(numeros) > 1:
        for digito in numeros:
            multiplicacion = multiplicacion * int(digito)
        numeros = str(multiplicacion)
        multiplicacion = 1
        print(numeros)
        persistencia_multiplicativa += 1

    return persistencia_multiplicativa


print(persitence(7793))
