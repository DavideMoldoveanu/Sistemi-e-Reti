"""
Un indirizzo MAC (Media Access Control address) è un indirizzo univoco associato dal produttore, a una NIC, composto da 6 coppie di cifre esadecimali separate da due punti.
Un esempio di MAC è 02:FF:A5:F2:55:12.
Scrivi una funzione genera_mac che generi degli indirizzi MAC pseudo casuali.
"""

import string
import random

def genera_mac():
    tipo = string.digits + "ABCDEF" #a "string.digits" (ovvero 0123456789) "aggiungo ABCDEF"
   
    mac = ""

    for k in range (6):                         #for generale che racchiude le 6 coppie
        if (k < 5):                             #faccio questa if così alla quinta coppia va nell'else e non mette più i ":" alla fine
            for j in range (2):                 #forma le coppie
                copp = random.choice(tipo)
                mac += copp
            
            mac += ":"
        else:
            for j in range (2):                 #forma le coppie
                copp = random.choice(tipo)
                mac += copp
    
    print(mac)


genera_mac()