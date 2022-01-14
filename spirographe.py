import turtle 
import time 
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(3)
for i in range (10) :
    for coulours in ["red", "magenta","blue","cyan","green","yellow","white"]:
        turtle.color(coulours)
        turtle.circle(100)
        turtle.left(10)

turtle.hideturtle()
