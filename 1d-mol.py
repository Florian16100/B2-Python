#!/bin/python3.6
#1d-mol.py
#Jeu du plus ou moins
#05/11/2018
#Florian Lys

import os
import signal
from random import randrange
 
nombre = 0
 
nombreMystere = randrange(1, 100)
 
def aurevoir():
 return print('le nombre était',str(nombreMystere))
 exit()

def ctrl(sig, frame):
 print('Pas cool de CTRL+C')
 exit()

signal.signal(signal.SIGINT, ctrl) 

while nombre != nombreMystere:
     
 print("Quel est le nombre ?")
 
 nombre = input()
 nombre = int(nombre)
 
 if nombre < nombreMystere:
  print("trop petit !\n")

 elif nombre > nombreMystere:
  print("trop grand !\n")
 

else:
  print("Félicitations, vous avez trouvé le nombre mystère !!!\n") 
  aurevoir()
          
