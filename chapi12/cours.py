# .*. coding:utf8 .*.

print("Cours chap12: Installer un module")
print("Premiers essais avec Turtle")

characters = ["alvin et les Chipmunks", "Babar", "betty boop", "calimero", "casper", "le chat potté", "kirikou"]
quotes = [
  "Écoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes!", 
  "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

import turtle

# PREMIER ESSAI TURTLE
# turtle.forward(123)
# turtle.right(270)
# turtle.forward(123)
# turtle.circle(55.3, 270)
# turtle.done()


# SECOND ESSAI TURTLE

# turtle.color('red', 'yellow')
# turtle.begin_fill()
# while True:
#   turtle.forward(200)
#   turtle.left(75)
#   if abs(turtle.pos()) < 1:
#     break
# turtle.end_fill()
# turtle.done()

import random

def get_random_item(my_list):
  rand_numb = random.randint(0, len(my_list) - 1)
  item = my_list[rand_numb] # get a quote from the list
  return item 

def message(character, quote):
  cap_character = character.capitalize()
  cap_quote = quote.capitalize()
  return "{} a dit: {}".format(cap_character,cap_quote)

user_answer = input("Tapez Entrée pour connaître une autre citation ou B pour quitter le programme")

while user_answer != "B":
  print(message(get_random_item(characters), get_random_item(quotes)))
  user_answer = input("Tapez Entrée pour connaître une autre citation ou B pour quitter le programme")