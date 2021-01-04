"""
Implementare il videogioco snake tramite il modulo turtle.
"""

import turtle 
import time
import random

delay = 0.1
punteggio = 0


#setto lo schermo
schermo = turtle.Screen()
schermo.title("Snake")
schermo.bgcolor("green")
schermo.setup(width=1000, height=1000)
schermo.tracer(0)

#creo la testa del serpente
testa = turtle.Turtle()
testa.speed(0)
testa.shape("square")
testa.color("red")
testa.penup()           #setta la "penna" su PENUP ovvero il puntatore si muoverà ma non disegnerà nulla
testa.goto(0,0)
testa.direction = "Stop"

#creo il cibo per lo snake
cibo = turtle.Turtle()
colore = random.choice(["yellow", "blue", "purple"])
forma = random.choice(["circle", "triangle"])
cibo.shape(forma)
cibo.speed(0)
cibo.color(colore)
cibo.penup()
cibo.goto(50,200)

#creo la "penna" per poter scrivere il punteggio
serpente = []
penna = turtle.Turtle()     #la penna corrisponde alla scritta che apparirà
penna.speed(0)
penna.shape("square")
penna.color("light blue")
penna.penup()
penna.hideturtle()              #nasconde il puntatore che disegna
penna.goto(0,400)
penna.write("Score: 0", align="center", font=("arial",32,"bold"))

#funzione per andare su
def goUp():
    if(testa.direction != "down"):
        testa.direction = "up"

#funzione per andare giù
def goDown():
    if(testa.direction != "up"):
        testa.direction = "down"

#funzione per andare sinistra
def goLeft():
    if(testa.direction != "right"):
        testa.direction = "left"

#funzione per andare destra
def goRight():
    if(testa.direction != "left"):
        testa.direction = "right"

#funzione per muovere
def move():
    if(testa.direction == "up"):
        y = testa.ycor()
        testa.sety(y+20)

    if(testa.direction == "down"):
        y = testa.ycor()
        testa.sety(y-20)

    if(testa.direction == "left"):
        x = testa.xcor()
        testa.setx(x-20)

    if(testa.direction == "right"):
        x = testa.xcor()
        testa.setx(x+20)

#creo l'attesa dei pulsanti per muovere il serpente
schermo.listen()
schermo.onkeypress(goUp,"w")
schermo.onkeypress(goLeft,"a")
schermo.onkeypress(goDown,"s")
schermo.onkeypress(goRight,"d")


#creo l'efettivo gioco (infinito dato che metto come condizione del "while" solo "true")
while True:
    schermo.update()
    if (testa.xcor() > 490 or testa.xcor() < -490 or testa.ycor() > 490 or testa.ycor() < -490):          #controllo se si verificano collisioni tra i bordi e il serpente
        time.sleep(1)
        testa.goto(0,0)
        testa.direction = "Stop"
        colore = random.choice(["yellow", "blue", "purple"])
        forma = random.choice(["circle", "triangle"])
        for partSerpe in serpente:                                          #nascondo il serpente
            partSerpe.goto(2000,2000)
        serpente.clear()

        punteggio = 0
        delay = 0.1
        penna.clear()
        penna.write("Score: {}".format(punteggio), align="center", font=("arial",32,"bold"))
    
    if(testa.distance(cibo) < 20):          #controllo se ci sono "collisioni" con il cibo, così so se far aumentare la lunghezza
        x = random.randint(-470,470)
        y = random.randint(-470,470)
        cibo.goto(x,y)

        #allungo il serpente
        nSerpente = turtle.Turtle()
        nSerpente.speed(0)
        nSerpente.shape("circle")
        nSerpente.color("white")
        nSerpente.penup()
        serpente.append(nSerpente)
        delay -= 0.001
        punteggio += 10

        penna.clear()
        penna.write("Score: {}".format(punteggio), align="center", font=("arial",32,"bold"))
    
    for lung in range(len(serpente)-1,0,-1):      
        x = serpente[lung - 1].xcor()
        y = serpente[lung - 1].ycor()
        serpente[lung].goto(x,y)
    
    if(len(serpente) > 0):
        x = testa.xcor()
        y = testa.ycor()
        serpente[0].goto(x,y)
    
    move()
    
    for partSerpe in serpente:    #controllo se si verificano collisioni tra la testa e il corpo del serpente
        if (partSerpe.distance(testa) < 20):
            time.sleep(1)
            testa.goto(0,0)
            testa.direction = "Stop"
            colore = random.choice(["yellow", "blue", "purple"])
            forma = random.choice(["circle", "triangle"])
            for partSerpe in serpente:                                          #nascondo il serpente
                partSerpe.goto(2000,2000)
            serpente.clear()

            punteggio = 0
            delay = 0.1
            penna.clear()
            penna.write("Score: {}".format(punteggio), align="center", font=("arial",32,"bold"))    
    time.sleep(delay)


schermo.mainloop()