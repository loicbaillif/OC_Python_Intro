# -*- coding:utf8 -*-

# Install library:
import json 
import random 

import os 
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
character_file = os.path.join(THIS_FOLDER, 'characters.json')
quote_file = os.path.join(THIS_FOLDER, 'quotes.json')

# Receive a JSON file and return a Python list from it:
def read_values_from_json(path, key):
  values = []
  with open(path) as f:
    data = json.load(f)
    for entry in data:
      values.append(entry[key])
  return values 

# Give a json and return a list:
def clean_strings(sentences):
  cleaned = []
  # Store quotes on a list. Create an empty list and add each sentence one by one.
  for sentence in sentences:
    # Clean quotes from whitespaces and so on
    clean_sentence = sentence.strip()
    # Don't use extend as it adds each letter one by one!
    cleaned.append(clean_sentence)
  return cleaned

# Return a random item in a list:
def random_item_in(object_list):
  rand_numb = random.randint(0, len(object_list) - 1)
  return object_list[rand_numb]

# Return a random value from a JSON file:
def random_value(source_path, key):
  all_values = read_values_from_json(source_path, key)
  clean_values = clean_strings(all_values)
  return random_item_in(clean_values)

####################
##     QUOTES     ##
####################

# Gather quotes from San Antonio:

def random_quote():
  return random_value(quote_file, 'quote') 

####################
##   CHARACTERS   ##
####################

# Gather characters list from Wikipedia

def random_character():
  return random_value(character_file, 'character')

####################
##  INTERACTION   ## 
####################

# Print a random sentence:

def print_random_sentence():
  rand_quote = random_quote()
  rand_character = random_character() 
  print(">>>>> {} a dit: {}".format(rand_character, rand_quote))

def main_loop():
  while True:
    print_random_sentence()
    message = ("Voulez-vous voir une autre citation?"
      "Pour sortir du programme, tapez [B]")
    choice = input(message).upper()
    if choice == 'B': 
      break 
      # stops the loop

if __name__ == '__main__':
  main_loop()