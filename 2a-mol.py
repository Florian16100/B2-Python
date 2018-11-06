
#DESCRIPTION : ieu du plus ou moins dialoguant avec un fichier externe
#Date : 23/10/2018
#AUTEURS : Guillaume Le Coq

import sys
import signal
from time import sleep
import random


compteur = 0

randomInt = random.randint(1,101)

file = open('talkiewalkie.txt' 'w').write("Bienvenue dans le fichier de communication du Plus ou Moins")



def exitscript():
    print("Au revoir, la solution était {}.".format(randomInt))
    sys.exit(0)

print("Jeux du plus ou moins")
print("La valeur est comprise en 0 et 100 \n ")

while 1:

    userInt = open('talkiewalkie.txt', 'rt').readline(3)

    userLea = open('talkiewalkie.txt', 'rt').readline(1)
    if userLea == "q":
        exitscript()
    try:
        #transforme l'entrée de l'utilisateur en int
        userValue = int(userInt)
        #Si nombre inconnu est plus grand écrit plus grand dans le fichier
        if userValue < randomInt:
            file = open('talkiewalkie.txt', 'w').write("Plus grand !")
            compteur = compteur + 1
        #Si nombre inconnu est plus petit écrit plus petit dans le fichier
        elif userValue > randomInt:
            file = open('talkiewalkie.txt', 'w').write("Plus petit !")
            compteur = compteur + 1
        #Si nombre inconnu est trouvé affiche le nombre (randomInt) et le nombre de coups (compteur)
        elif userValue == randomInt:
            compteur = compteur + 1
            print("Bravo, la valeur était {}. Vous avez réussi en {} coups.".format(randomInt, compteur))
            sys.exit(0)
        #Si user entre autre que int l'ignore
    except ValueError:
            sleep(1)

