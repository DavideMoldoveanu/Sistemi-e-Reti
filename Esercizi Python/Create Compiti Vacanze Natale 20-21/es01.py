"""
Scrivi una funzione generatrice di password. La funzione deve generare una stringa alfanumerica di 8 caratteri qualora l'utente voglia una password semplice, 
o di 20 caratteri ascii qualora desideri una password più complicata.
"""

import string
import random

def genPass(num):
    passSempl = string.digits + string.ascii_letters                             #caratteri alfanumerici (contiene lettere e numeri)
    passCompl = string.digits + string.ascii_letters + string.punctuation        #caratteri ascii (contiene lettere, numeri e punteggiatura)

    if (num == 0):
        lung = 8
        tipo = passSempl
    else:
        lung = 20
        tipo = passCompl
    
    pas = ""

    for cnt in range(lung):
        car = random.choice(tipo)
        pas += car

    print(pas)

k = int(input("0 - Password semplice\n1 - Password complessa\nInserisci la tipologia: "))
genPass(k)