"""
for elemento in [3,4,1,8]:
    print(elemento)

lista = [3,4,1,8]
for i in range (0,len(lista),1):
    print(lista[i])

for i, elemento in enumerate(lista):                    #contatore automatico 
    print(f"indice: {i} - elemento: {elemento}")

contatore = 0
while(contatore < len(lista)):
    print(lista[contatore])
    contatore += 1

lista = [1,"c","ciao",3.1415]
"""
"""
playlist = [[1,"titolo1","autore1"],
            [2,"titolo2","autore2"],
            [3,"titolo3","autore3"]]
"""
"""
#print(playlist[1][1])

for elemento in playlist:
    print(elemento[1])

"""
#DIZIONARIO
#I dizionari sono elenchi, non ordinati, di copie (chiave, valore)
"""
canzone = {"numero":1, "titolo": "20 anni", "autore": "Maneskin"}
# "numero", "titolo" e "autore" sono le chiavi del dizionario
# 1, "20 anni" e "Maneskin" sono i valori del dizionario
print(canzone["autore"])
"""
"""
elenco_classe = {1:"Alladio", 2: "Alpigiano", 3:"Bertoglio", 4:"Bongiovanni"}
print(elenco_classe[3])
"""

#IMPORTANTE PER I FILE JSON PER I DATABASE NOSQL

"""
playlist = [{"numero":1, "titolo": "20 anni", "autore": "Maneskin"},
            {"numero":2, "titolo": "titolo2 bla bla", "autore": "Mario Rossi"},
            {"numero":3, "titolo": "titolo3 bla bla bla", "autore": "Paolo Bianchi"}]

print(playlist[0]["titolo"])

for canzone in playlist:            #printa tutti i titoli
    print(canzone["titolo"])    

"""
"""
elenco_classe = {1:"Alladio", 2: "Alpigiano", 3:"Bertoglio", 4:"Bongiovanni"}
voti_sistemi = {1:[8,9.5,7], 2:[8,9], 3:[10,7.5,8], 4:[9,9,7,6]}

#print(f"I voti di {elenco_classe[2]} sono {voti_sistemi[2]}")

for k in range(1,len(elenco_classe)+1):
    print(f"I voti di {elenco_classe[k]} sono {voti_sistemi[k]}")
"""
"""
lista = ["3","4","5","8","1","5"]
print(" ".join(lista))

lista_numeri = (3,4,5,8,1,5)

lista_stringhe = []

for numero in lista_numeri:
    lista_stringhe.append(str(numero))

print(lista_stringhe)
print(" ".join(lista_stringhe))
"""

def converti(lista_numeri):
    lista_stringhe = []
    for numero in lista_numeri:
        lista_stringhe.append(str(numero))
    return " ".join(lista_stringhe)
    

elenco_classe = {1:"Alladio", 2: "Alpigiano", 3:"Bertoglio", 4:"Bongiovanni"}
voti_sistemi = {1:[8,9.5,7], 2:[8,9], 3:[10,7.5,8], 4:[9,9,7,6]}

for k in range(1,len(elenco_classe)+1):
    print(f"I voti di {elenco_classe[k]} sono {converti(voti_sistemi[k])}")