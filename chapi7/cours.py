# -*- coding: utf8 -*-
print("Cours du chapitre 7")

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes!",
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = ["alvin et les Chimpunk", "Babar", "betty boop", "calimero", "casper", "le chat potté", "kirikou"]

user_answer = 1

# Algorithm to display random quote:

# Show random item from a list 
def get_random_item_in(my_list):
  # get a random number
  item = my_list[0] # get a quote from the list, so far just the first one
  return item

while user_answer != 3:
  # - Show another quote 
  print("Une autre! Une autre!")
  print(get_random_item_in(quotes))
  user_answer = user_answer + 1

for character in characters:
  nouveau_character = character.capitalize()
  print(nouveau_character)