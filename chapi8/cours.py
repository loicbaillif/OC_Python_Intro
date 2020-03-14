# -*- coding: utf8 -*-
print("Cours du chapitre 8")

# Modify strings #

first_string = "hElLo WoRlD!"
second_string = "{character} a dit: {quote}"
third_string = "{} a dit: {}"
print(first_string)

# capitalize: Upper case for the first letter of the  first word. Everything else lower case
print(first_string.capitalize())

# upper: All letters in upper case
print(first_string.upper())

# lower: All letters in lower case
print(first_string.lower())

# split: Separate "words" into an array
print(first_string.split())

# strip: Remove all white spaces at the beginning AND the end of a string:
print("   How you doin'?     ".strip())

# format: To replace variables inside a string with values:
print(second_string.format(
  character="Babar", quote="Tout n'est pas cirrhose dans la vie, dit l'alcoolique"))

# format can also be used with anonymized variables: just respect the order
print(third_string.format("Babar", "Tout n'est pas cirrhose dans la vie, dit l'alcoolique."))

# End of chapter 8