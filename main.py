"""
Jules Buonassera
403
TP2 : jeu de devinette
"""

import random

essaie = 0
borne_minimale = 0
borne_maximale = 100
playing = True

while playing:
    nombre_aleatoire = random.randint(borne_minimale, borne_maximale)
    essaie = 0
    nb_essai = 0

    print("J’ai choisi un nombre au hasard entre " + str(borne_minimale) + " et " + str(
        borne_maximale) + ".\nÀ vous de le deviner...")

    while essaie != nombre_aleatoire:
        print("Entrez votre essai :")
        essaie = int(input())
        nb_essai += 1
        if essaie > nombre_aleatoire:
            print("Mauvais choix, le nombre est plus petit que " + str(essaie) + "\n")

        elif essaie < nombre_aleatoire:
            print("Mauvaise réponse, le nombre est plus grand que " + str(essaie) + "\n")

        else:
            print("Bravo! Bonne réponse")
            print("Vous avez réussi en : " + str(nb_essai) + " coups")
            recomencer = input("Voulez-vous faire une autre partie (o/n)?\n")
            if recomencer == "n":
                print("Merci et au revoir…")
                playing = False