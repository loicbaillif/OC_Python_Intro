# -*- coding: utf8 -*-
print("Cours du chapitre 5")

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes!",
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
    "Alvin et les Chipmunks",
    "Babar","Betty Boop",
    "Calimero",
    "Casper",
    "Le chat potté",
    "Kirikou"
]

user_answer = "B"

# Algorithm to display random quote:

# Show random quote 

if user_answer == "B": 
  # - Exit the program 
  print("OK, on ferme")
  pass
elif user_answer == "C":
  print("C pas la bonne réponse! Et G pas d'humour, je C...")
else: 
  # - Show another quote 
  print("Une autre! Une autre!")