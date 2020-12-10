"""
Authors: Moldoveanu Davide

Scrivere un programma in python3 che legge il file .csv delle canzoni e carichi le canzoni una 
oppportuna lista di dizionari. (facoltativo: usare i dizionario di dizionari)
- dizionari (decidere i nomi delle chiavi)
- lettura file
- split di stringhe
- metodo join
"""

file = open("canzoni.csv","r")

playlist = []
dizionario = {}     #dizionario vuoto

for riga in file:
    rigaTemp = riga[0:-1].split(",")    #dove c'è una virgola lo divide         #mettendo fino a -1 cancella l'ultimo carattere dell'ultima riga perché non ha l'INVIO
    dizionario["indice"]=rigaTemp[0]    #parte dall'inizio e va fino alla prima virgola
    dizionario["titolo"]=rigaTemp[1]    #parte dalla prima virgola e va fino alla seconda virgola
    dizionario["autore"]=rigaTemp[2]    #parte dalla seconda virgola e va fino alla fine (\n non compreso)
    dizT = dizionario.copy()            #uso dizT perché se no tutti i valori che leggo li perdo e alla fine avrò solo l'ultima canzone
    playlist.append(dizT)               #le canzoni troppo lunghe non riesce a leggerle..

for element in (playlist):
    print(element["indice"], element["titolo"], element["autore"])
    
file.close()
