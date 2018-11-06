#!/bin/python3.6
# Trier les noms d'utilisateurs par ordre alphabétique
#04/11/2018
#Florian Lys

def addDic():
name_dic={}
i=0

while 1:
print("Entrez le nom à ajouter")
saisie=input()

if saisie == "Q"
	print("fin de la saisie")
	break

else:
	name_dic[str(i)}=saisie
	i=i+1

name_dic=sorted(name_dic.values())
print(name_dic)

addDic()  
