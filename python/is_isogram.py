"""
An isogram is a word that has no repeating letters, consecutive or 
non-consecutive. Implement a function that determines whether a string that 
contains only letters is an isogram. Assume the empty string is an isogram. 
Ignore letter case.
"""

from os import system

system("cls")

def is_isogram(string):
    word = string.lower()

    for character in word:
        character_count = word.count(character)

        if character_count > 1:
            print(f"El caracter {character} aparece {character_count} veces")
            return False
    return True

def is_isogram_with_set(string):
    return len(string) == len(set(string.lower()))

print(is_isogram("Dermatoglyphics"))
print(is_isogram("isIsogram"))
print(is_isogram_with_set("isIsogram"))
print(is_isogram_with_set("Dermatoglyphics"))
