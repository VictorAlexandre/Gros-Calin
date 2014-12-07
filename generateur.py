# -*- coding: utf-8 -*-  # Définition l'encodage des caractères
try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *
from random import *
from difflib import *
 
#On ouvre d'abord les fichiers de titres

#Cinema
fichiercine = open("titrescinema.txt", "r")
titrescine = fichiercine.readlines()
fichiercine.close()
#Litterature
fichierlitt = open("titreslitterature.txt", "r")
titreslitt = fichierlitt.readlines()[0].replace('"','').split(",")
fichierlitt.close()
#Chansons
fichierchan = open("titreschansons.txt", "r")
titreschan = fichierchan.readlines()[0].replace('"','').split(",")
fichierchan.close()
#Expressions
fichierexpr = open("listeexpressions.txt", "r")
titresexpr = fichierexpr.readlines()[0].replace('"','').split(",")
fichierexpr.close()
#Autres
fichierautres = open("autres.txt", "r")
titresautre = fichierautres.readlines()[0].replace('"','').split(",")
fichierautres.close()

#Ensuite, on les regroupe dans une seule liste
listedetitres=titrescine+titreslitt+titresexpr+titreschan+titresautre
resultatstitres=[]
nouveauxtitres=[]
#Les mots clés sont séparés par des virgules

def recherchedetitre():
	#Etape 2: On teste le mot clé
	global entree_motcle, nouveauxtitres, resultatstitres
	motcle = entree_motcle.get()
	motcle=motcle.lower()
	if len(motcle)<4:
		resultats['text'] = "Le mot est trop court"
	if len(motcle)>=4:
		resultats['text'] = "Cliquer sur Afficher les titres."
	if len(motcle)>=30:
		resultats['text'] = "Le mot clé est trop long et donc un peu suspect. Désolé"
		sys.exit(0)
	resultatstitres=[]
	nouveauxtitres=[]
	for titre in listedetitres:
		#Separation de chaque mot au sein de chaque titre
		mots_du_titre = titre.split()
		#Comptage du nombre de lettres de chaque mot de chaque titre
		for j in range(len(mots_du_titre)):
			mot_courant = mots_du_titre[j]
			if len(mot_courant) > 4:
				Test = 1
	#Test HQ pour les 4 dernieres lettres
				for i in range(1,5):
					if motcle<4:
						Test = 0
					elif motcle[-1*i] != mot_courant[-1*i]:
						Test = 0
				if Test == 1:
					resultatstitres.append(titre)
					titretemp = ''
					for i in range(len(mots_du_titre)):
						if i<>j:
							titretemp = titretemp+mots_du_titre[i]+' '
						else:	
							titretemp = titretemp + motcle+' ' 
					nouveauxtitres.append(titretemp)
	#Test HQ pour les 4 premieres lettres
	for titre in listedetitres:
		mots_du_titre = titre.split()
		for j in range(len(mots_du_titre)):
			mot_courant = mots_du_titre[j]
			if len(mot_courant) > 4:
				Test = 1
				for i in range(0,4):
					if motcle<4:
						Test = 0
					elif motcle[i] != mot_courant[i]:
						Test = 0
				if Test == 1:
					resultatstitres.append(titre)
					titretemp = ''
					for i in range(len(mots_du_titre)):
						if i<>j:
							titretemp = titretemp+mots_du_titre[i]+' '
						else:
							titretemp = titretemp + motcle+' ' 
					nouveauxtitres.append(titretemp)
	
	#Test de similarite entre deux mots
	for titre in listedetitres:
		mots_du_titre = titre.split()
		for j in range(len(mots_du_titre)):
			mot_courant = mots_du_titre[j]
			if len(mot_courant) > 4:
				Test = 1
				if SequenceMatcher(a=motcle, b=mot_courant).ratio() < 0.75:
					Test=0
				else:
					Test=1
				if Test == 1:
					resultatstitres.append(titre)
					titretemp = ''
					for i in range(len(mots_du_titre)):
						if i<>j:
							titretemp = titretemp+mots_du_titre[i]+' '
						else:
							titretemp = titretemp + motcle+' ' 
					nouveauxtitres.append(titretemp)						
				
			
				
def repondre():
	global resultatsdroit, resultatsgauche, nouveauxtitres, resultatstitres, indexselectionnes, longueurtotale
	resultatsdroit = ''
	resultatsgauche = ''
	#On selectionne les listes qui depassent 30 resultats et on propose 29 resultats maximum sur la page
	if len(nouveauxtitres)>30:
		longueurtotale=len(nouveauxtitres)
		new=nouveauxtitres
		old=resultatstitres
		indexselectionnes=[]
		indexselectionnes=sample(xrange(longueurtotale), 29)
		
		for i in indexselectionnes:
			resultatsdroit = resultatsdroit + new[i] + '\n'
			resultatsgauche = resultatsgauche + old[i] + '\n'

	else: 	
		for i in range(len(nouveauxtitres)):
			resultatsdroit = resultatsdroit + nouveauxtitres[i] + '\n'
			resultatsgauche = resultatsgauche + resultatstitres[i] + '\n'
 	affichagedroit['text'] = resultatsdroit
	affichagegauche['text'] = resultatsgauche

def init():
	global entree_motcle
	entree_motcle.delete (0, END)
	affichagedroit.config(text = "")
	affichagegauche.config(text = "")
	resultats.config(text = "")
	

Fenetre = Tk()
Fenetre.title('Gros Câlin : Générateur de titre')

Hautcentre=Frame(Fenetre)
Hautcentre.grid(row=1,column=1)
Ligneboutonsa=Frame(Fenetre)
Ligneboutonsa.grid(row=2, column=1, sticky=W)
Ligneboutonsb=Frame(Fenetre)
Ligneboutonsb.grid(row=2, column=1,sticky=N)
Ligneboutonsc=Frame(Fenetre)
Ligneboutonsc.grid(row=2, column=1,sticky=E)
Middle=Frame(Fenetre)
Middle.grid(row=3, column=1)
Cadregauche=Frame(Middle)
Cadregauche.grid(row=1,column=1)
Cadredroite = Frame(Middle)
Cadredroite.grid(row=1,column=2)
Bottom=Frame(Fenetre)
Bottom.grid(row=4, column=1)
presentation = Label(Hautcentre, text= "Tapez un mot cle de 4 lettres minimum, sans majuscule ni accent: ")
entree_motcle = Entry(Hautcentre)
valeur = Button(Ligneboutonsa, text ='Valider', command=recherchedetitre)
valeur2 = Button(Ligneboutonsb, text ='Afficher les titres/En afficher plus', command=repondre)
valeur3 = Button(Ligneboutonsc, text ='Recommencer', command=init)
affichagedroit = Label(Cadredroite,wraplength=400,fg="black",font=("Helvetica",12))
affichagegauche = Label(Cadregauche,wraplength=400,fg="black",font=("Helvetica",12))
resultats=Label(Hautcentre, fg="red", width=50)
credits=Label(Bottom, text='Programme développé par Victor Alexandre, 2014, github.com/VictorAlexandre')
presentation.pack()
entree_motcle.pack()
valeur.pack()
valeur2.pack()
valeur3.pack()
resultats.pack()
affichagedroit.pack()
affichagegauche.pack()
credits.pack(side=BOTTOM)
Fenetre.mainloop()
