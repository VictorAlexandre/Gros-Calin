Generateur de titres / Title generator
===================
## English version here (french version down)

A French python program to generate titles from a keyword.

Separate files are found in this repo: the *.py and 5 *.txt. In each of these, there is a list of expressions between " " and separated by a comma. 

Th program will browse each of these and see if the keyword typed into the *.py share some properties with one or several words of each expression.

Quatre tests are implemented: 
- does the keyword have 4 letters or more ?
- does the keyword share its first 4 letters with a word inside the expression ?
- does the keyword share its last 4 letters with a word inside the expression ?
- does the keyword share 75% of its letters with a word inside the expression ?

*Note: This is my first (and only) Python program. It was written during an initiation to programming course in ENS, Paris, with the help of the two tutors.*
***
## French version here

Ce programme en Python permet de générer des titres à partir d'un mot clé.

Plusieurs fichiers composent ces dossier: un fichier python et 5 fichiers texte. Chacun contient une liste de titres de chansons, de livres, de films, d'expressions diverses. Chaque élément de la liste est entouré de guillemets et séparé par une virgule.

Le programme reçoit le mot clé et parcourt l'ensemble des mots composant chacune des expressions contenues entre guillemets à la recherche d'un mot qui partagerait une ou plusieurs propriétés avec le mot clé.

Quatre tests sont (pour l'instant) proposés:
- le mot clé a-t-il 4 lettres ou plus ?
- le mot clé partage-t-il ses 4 premières lettres avec un mot au sein de l'expression ?
- le mot clé partage-t-il ses 4 dernières lettres avec un mot au sein de l'expression ?
- le mot clé partage-t-il 75% de lettres avec un mot au sein de l'expression ?

*Note: Ceci est mon premier (et pour l'instant le seul) programme codé en Python. Il a été écrit à l'ENS, avec l'aide des deux professeurs d'initiation à la programmation.*
