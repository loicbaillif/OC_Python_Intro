# -*- coding:utf8 -*-

print("Chapitre 13: Utiliser le module JSON")
# RAPPEL : JSON = JavaScript Object Notation

import json
import random

import os 
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
character_file = os.path.join(THIS_FOLDER, 'characters.json')
quote_file = os.path.join(THIS_FOLDER, 'quotes.json')

def read_values_from_json(file, key):
  # We want to "import" characters.json and turn it into a Python list :
  values = []
  with open(file) as f:
    data = json.load(f)
    for entry in data:
      values.append(entry[key])
  return values

def message(character, quote):
  cap_character = character.capitalize()
  cap_quote = quote.capitalize()
  return "{} a dit: {}".format(cap_character, cap_quote)

def get_random_item_in(my_list):
  rand_key = random.randint(0, len(my_list) - 1)
  item = my_list[rand_key]
  return item

def get_random_character():
  all_characters = read_values_from_json(character_file, 'character')
  return get_random_item_in(all_characters)

def get_random_quote():
  all_quotes = read_values_from_json(quote_file, 'quote')
  return get_random_item_in(all_quotes)

# PROGRAM :
user_answer = input("Tapez ENTREE pour une autre citation ou B pour quitter le programme")

while user_answer != "B":
  print(message(get_random_character(), get_random_quote()))
  user_answer = input("Tapez ENTREE pour une autre citation ou B pour quitter le programme")