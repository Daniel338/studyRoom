"""
Alejo Marca Daniel 19/06/2022
Implement the function unique_in_order which takes as argument a sequence 
and returns a list of items without any elements with the same value next 
to each other and preserving the original order of elements.
"""

from os import system

system("cls")


def unique_in_order(iterable):

    list_orden = []
    for item in iterable:
        if item not in list_orden:
            list_orden.append(item)

    return list_orden

def unique_in_order_1(iterable):

    list_orden = []
    for item in iterable:
        if item not in list_orden:
            list_orden.append(item)
        elif item != list_orden[-1]:
            list_orden.append(item)
    return list_orden

def unique_in_order_with_prev(iterable):
    result = []
    prev = None

    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result

print(unique_in_order_with_prev("AAAABBBCCDAABBB"))
print(unique_in_order_with_prev("ABBCcAD"))
print(unique_in_order_with_prev([1,2,2,3,3]))
