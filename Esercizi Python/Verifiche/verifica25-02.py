"""
Author: Moldoveanu Davide
Es: Verifica QR Code
"""

import csv
import pygame
import sys

NERO = (0,0,0) #RGB
BIANCO = (255,255,255)

diz={"a": [0,0,0,0,0], "b": [0,0,0,0,1], "c": [0,0,0,1,0],"d":[0,0,0,1,1], "e": [0,0,1,0,0], "f": [0,0,1,0,1], "g": [0,0,1,1,0],  "h": [0,0,1,1,1], "i": [0,1,0,0,0], "l": [0,1,0,0,1], "m": [0,1,0,1,0],
    "n":[0,1,0,1,1], "o": [0,1,1,0,0], "p": [0,1,1,0,1], "q": [0,1,1,1,0], "r": [0,1,1,1,1], "s": [1,0,0,0,0], "t": [1,0,0,0,1], "u": [1,0,0,1,0], "v": [1,0,0,1,1], "z": [1,0,1,0,0], "0": [1,0,1,0,1],
    "1": [1,0,1,1,0], "2": [1,0,1,1,1], "3": [1,1,0,0,0], "4": [1,1,0,0,1], "5": [1,1,0,1,0], "6": [1,1,0,1,1], "7": [1,1,1,0,0], "8": [1,1,1,0,1], "9":[1,1,1,1,0], " ": [1,1,1,1,1]}


def condificaFrase(f):
    fApp = []
    for cnt in range (len(f)):      #ciclo tutto la frase
        for car in diz.keys():      #ciclo tutto il dizionario 
            if(f[cnt] == car):      #verifico se il carattere analizzato della frase è presente nel dizionario
                fApp.append(diz[car])   #assegno a una lista d'appoggio il valore della chiave corrispondente
    
    return fApp


def disegnaQRCode(f):
    #faccio una griglia tutta nera
    dimQuad = 50      
    for x in range(0, DIMENSIONI[0], dimQuad):
        for y in range(0, DIMENSIONI[1], dimQuad):
            piastrella = pygame.Rect(x, y, dimQuad, dimQuad)  #vertice alto-sinsitra, max lato
            pygame.draw.rect(screen, BIANCO, piastrella, 1)  #dove disegnare, colore, cosa, bordo (se nn metto niente o 0 fa disegno pieno)
    
    #nei punti in cui trovo il bit 0 disegno un quadrato bianco

    dimensione = 50
    
    for contY in range(0, len(f)):
            for contX in range(0, len(f[contY])):
                

                if f[contY][contX] == 0:            #verifico se trovo un bit bianco
                    contX = contX * dimensione
                    contY = contY * dimensione 

                    ostacolo = pygame.Rect(contX, contY, dimensione, dimensione)
                    pygame.draw.rect(screen, BIANCO, ostacolo)

                    contX = int(contX / dimensione)          
                    contY = int(contY / dimensione) 


def caricaCSV(f):
    with open('C:\\Users\\david\\OneDrive\\Materie ITIS - Sync\\anno 20-21\\sistemi e reti\\teoria\\esercizi\\FraseCodificata.csv', mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)   #inizializza la colonna

        writer.writerow(["Lettere"])            #stampo l'intestazione della colonna
        for k in range (len(f)):                    #ciclo tutte le lettere
            writer.writerows([f[k]])      #stampo una riga alla volta 


def main():

    frase = input("Inserisci frase da convertire in QR Code: ")

    while True:                     #controllo che la frase non abbia più di 12 caratteri
        if len(frase) > 12:
            frase = input("Inserisci un'altra frase da convertire in QR Code: ")
        else:
            break
    

    frase = condificaFrase(frase)   #mi returna la lista di liste codificato in bit

    print(frase)


    caricaCSV(frase)

    global screen           # da qui in avanti ho creato variabili globali per poter fare il pygame anche in funzioni senza passare parametri
    global DIMENSIONI

    ySchermo = (len(frase))*50  #dichiato fuori le variabili perché in caso io voglia cambiare le dimensioni posso farlo cambiando solo le variabili

    xSchermo = 5*50

    DIMENSIONI = (xSchermo,ySchermo)

    pygame.init()
    screen = pygame.display.set_mode(DIMENSIONI)
    screen.fill(NERO)
    while True:                    
        disegnaQRCode(frase)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:        #per chiudere il pygame si può fare prememendo "solo esc"
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    break                           #così esce dal while True


        pygame.display.update()             #aggiorna il display di pygame
    

    


if __name__ == "__main__":
    main()