# -*- coding: utf8 -*-
print("Cours du chapitre 6")

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes!",
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

user_answer = "B"

# Algorithm to display random quote:

# Show random quote 
def get_random_quote(my_list):
  # get a random number
  quote = my_list[0] # get a quote from the list, so far just the first one
  # show the quote in the interpreter
  return quote


if user_answer == "A": 
  # - Exit the program 
  print("OK, on ferme")
  pass
elif user_answer == "C":
  print("C pas la bonne réponse! Et G pas d'humour, je C...")
else: 
  # - Show another quote 
  print("Une autre! Une autre!")
  print(get_random_quote(quotes))