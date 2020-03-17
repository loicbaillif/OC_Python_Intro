# .*. coding:utf8 .*.

print("Cours chapitre 11 : Utiliser les dictionnaires")

program = {"quotes": ["Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes!", 
"On doit pouvoir choisir entre s'écouter parler et se faire entendre."], 
"characters": ["alvin et les Chipmunks", "Babar", "betty boop", "calimero", "casper", "le chat potté", "Kirikou"]}

print(program["characters"])
print(program["quotes"])

# Accéder aux éléments d'une liste, elle-même dans un dictionnaire:
print(program["characters"][0])
# Parcourir toute la liste "characters" dans le dictionnaire:
def enumerate(input_list):
    # Will enumerate all elements insite input_list:
    for element in input_list:
        print(element)
    return "List entirely enumerated"

def enumerate_bis(input_list):
    # Will enumerate all elements inside input_list
    nb_elements = len(input_list)
    actual_element = 0
    while actual_element < nb_elements:
        print(input_list[actual_element])
        actual_element += 1
    return "List entirely enumerated"

enumerate(program["characters"])
enumerate_bis(program["characters"])

# Replace or add a value:
program["characters"] = "Simba"
print("Un personnage ajouté")
enumerate(program["characters"])

# Update one or multiple values:
program.update({"characters": ["Tom", "Jerry"], "quotes": ["There is nothing either good or bad..."]})
print("***** characters list:")
enumerate(program["characters"])
print("***** quotes list")
enumerate(program["quotes"])
print(program)