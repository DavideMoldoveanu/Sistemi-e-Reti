"""
Il file annual.csv (allegato) contiene la anomalia della temperatura globale del pianeta Terra dal 1880 ad oggi, proveniente da varie fonti (colonna “Source”). 
Scrivere un programma che generi un dizionario che abbia come chiave l’anno (“Year”) e valore la media aritmetica delle anomalie registrate dalle varie fonti durante quell’anno.
Inoltre scrivere una funzione che dati in input due anni diversi (anno_1 e anno_2) trovi la anomalia massima e minima nel periodo compreso tra anno_1 e anno_2.
"""

def maxTemperatura(anno1, anno2):
    file = open("annual.csv","r")
    tMax = 0.0
    tMin = 0.0
    if(anno1 < anno2):                          #metto sempre che anno1 sia quello più grande e più vicino a noi
        anno1,anno2 = anno2,anno1
    for k,riga in enumerate(file):
        if(k > 0):
            rigaTemp = riga[0:-1].split(",")
            fonte = rigaTemp[0]                           #non userò la fonte nell'esercizio, perciò potrei mettere "_" perché così su python non viene memorizzato la variabile
            anno = int(rigaTemp[1])                   #salvo anno
            temperatura = float(rigaTemp[2])                 #salvo la temperatura
            if(anno >= anno2 and anno <= anno1):        #verifico che anno si trovi nel periodo compreso tra i due anni dati
                if(anno == anno1):                      #
                    tMax = temperatura
                    tMin = temperatura
                else:
                    if(temperatura > tMax):
                        tMax = temperatura
                    if(temperatura < tMin):
                        tMin = temperatura
    return tMax,tMin



f = open("annual.csv", "r")
dizionario = {}
for k, riga in enumerate (f):       #k --> contine il numero della riga e riga --> contiene la riga puntata da k
    if(k > 0):
        rigaT = riga[0:-1].split(",")
        fonte = rigaT[0]                        #salvo fonte
        anno = rigaT[1]                  #salvo anno
        temperatura = rigaT[2]          #salvo la temperatura 
        if(k%2 != 0):
            dizionario[anno] += float(temperatura)   
            dizionario[anno] = float((dizionario[anno])/2)
        else:
            dizionario[anno] = float(temperatura)

anno_1 = int(input("Inserisci un anno dal 1880 al 2016: "))
anno_2 = int(input("Inserisci un anno dal 1880 al 2016: "))


print(dizionario[anno_1], "|",dizionario[anno_2])

print(maxTemperatura(anno_1, anno_2))