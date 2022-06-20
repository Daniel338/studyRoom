"""
Implement a function that adds two numbers together and returns their sum 
in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.
"""

from os import system

system("cls")


def add_binary(a, b):
    suma = a + b
    return format(suma, "b")


def add_binary_2(a, b):
    return bin(a+b)[2:]


def add_binary_3(a, b):
    return '{0:b}'.format(a + b)


def add_binary_4(a, b):
    return f"{a + b:b}"


print(add_binary(1, 1))
print(add_binary_2(1, 2))
print(add_binary_3(1, 3))
print(add_binary_4(2, 2))
