# -*- coding: utf8 -*-
print("Cours du chapitre 10 : Utiliser les listes")

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes!",
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = ["alvin et les Chipmunk", "Babar", "betty boop", "calimero", "casper", "le chat potté", "kirikou"]

# RAPPEL : Le premier index d'une liste est TOUJOURS 0

# Accéder à l'élément n d'une liste
print("index 0: " + characters[0])
print("index 3: " + characters[3])

# Connaître l'index d'une valeur
print("index de Babar: " + str(characters.index("Babar")))
print("index de casper: " + str(characters.index("casper")))

# Ajouter un élément à la fin de la liste:
print(characters)
characters.append("Mowgli")
print(characters)

# Modifier un élément: Y accéder avec son index et lui donner une nouvelle valeur
characters[2] = "La Fée Clochette"
print(characters)

# Supprimer un élément de la liste et renvoyer sa valeur:
test = characters.pop() #Sans argument, supprimera le dernier élément de la liste
print(characters)
print(test)
test = characters.pop(2)
print(characters)
print(test)

# Supprimer un élément d'une liste SANS renvoyer sa valeur:
characters.remove("casper")
print(characters)

# Connaître le nombre d'éléments dans une liste:
print("characters est une liste de " + str(len(characters)) + " éléments")

# Accéder au dernier élément d'une liste:
print(characters[-1])