"""
Il nostro amico Bob dopo alcune commissioni in giro per la città di Flatland deve rientrare a casa. Purtroppo Bob soffre di momentanee perdite di memoria!
Questa volta la sua amnesia dura ben 60 minuti e durante questi 60 minuti Bob adotta la seguente strategia per tentare di rientrare a casa. Ogni minuto decide a caso tra:
    procedere 10 m verso Nord
    procedere 10 m verso Sud
    procedere 10 m verso Est
    procedere 10 m verso Ovest
Simulare l’intero percorso compiuto da Bob, supponendo che il punto di partenza abbia coordinate (0,0) e salvarlo all’interno di un dizionario opportunamente strutturato.
Disegnare il percorso compiuto da Bob dentro una schermata di pygame.
Infine salvare il percorso di Bob dentro un file .csv opportunamente strutturato.

BONUS: ogni volta in cui Bob passa in un punto della città di Flatland in cui è già passato, stampare a schermo le coordinate del punto.
"""

import pygame
import sys
import random
import csv

BIANCO = (255, 255, 255)
NERO = (0,0,0)

minuti = 60
metri = 30
DIMENSIONE = (minuti*metri, minuti*metri)   #così è universale, se aumento i minuti o i metri alla volta, ci starà sempre nello schermo
coord = [DIMENSIONE[0]/2,DIMENSIONE[1]/2]

def creaDict():
    retDict = {}
    x = coord[0]
    y = coord[1]
    
    for k in range(60):
        rand = random.randint(0, 3)
        if rand == 0:
            x += metri  #EST
        elif rand == 1:
            x -= metri  #OVEST
        elif rand == 2:
            y += metri  #SUD
        elif rand == 3:
            y -= metri  #NORD
        
        retDict[k] = [x,y]
    
    #print(retDict)
    
    return retDict


def disegnaPercorso(dizionario):
    global screen
    pygame.init()  #parte pygame
    screen = pygame.display.set_mode(DIMENSIONE)  #dimensioni schermo
    screen.fill(NERO)

    while True:
        for i in range(60):
            if i == 0:
                pygame.draw.line(screen,BIANCO,[DIMENSIONE[0]/2,DIMENSIONE[1]/2],dizionario[i],10)
            else:
                pygame.draw.line(screen,BIANCO,dizionario[i-1],dizionario[i],10)
        for event in pygame.event.get():        #ascolta eventi (mouse, tastiera ecc)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
     
        pygame.display.update()


def caricoPercorso(dizionario):
    with open('C:\\Users\\david\\OneDrive\\Materie ITIS - Sync\\anno 20-21\sistemi e reti\\teoria\esercizi\\Percorso.csv', mode='w', newline='') as csv_file:
        colonne = ['Minuto', 'CoordinataX', 'CoordinataY']
        writer = csv.DictWriter(csv_file, fieldnames=colonne)

        writer.writeheader()
        for k in range(60):
            writer.writerow({'Minuto': dizionario[k], 'CoordinataX': dizionario[k], 'CoordinataY': dizionario[k]})


def main():
    
    dizionario = creaDict()

    caricoPercorso(dizionario)

    disegnaPercorso(dizionario)

    


if __name__ == "__main__":
    main()