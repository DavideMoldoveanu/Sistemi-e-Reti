"""
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
"""

"""
from turtle import *
#nLati = 6
nlati = int(input("Scrivi un numero "))
ang=360/nlati   
color('red', 'yellow')
begin_fill()
while True:
    forward(300)
    left(ang)
    if abs(pos()) < 1:
        break
end_fill()
done()  
"""

from turtle import Turtle, Screen

wind = Screen()
wind.bgcolor("lightgreen")

larg = 1000;
alt = 1000;
passo = 50; 

point = Turtle()
point.color("red")

wind.title("Paint")
wind.setup(width=larg, height=alt)
wind.listen() #mette la finestra in ascolto di eventi (es: pressione tasti)


def right():
    point.right(90)

def left():
    point.left(90)

def forward():
    if((point.xcor()+50<=larg//2 and point.xcor()-50>=-larg//2) and (point.ycor()+50<=alt//2 and point.ycor()-50>=-alt//2)):
        point.forward(50)
    else:
        point.goto(0,0)
def backward():
    if((point.xcor()+50<=larg//2 and point.xcor()-50>=-larg//2) and (point.ycor()+50<=alt//2 and point.ycor()-50>=-alt//2)):
        point.backward(50)
    else:
        point.goto(0,0)


wind.onkey(forward, "Up")
wind.onkey(backward, "Down")
wind.onkey(right, "Right")
wind.onkey(left, "Left")

wind.mainloop()
