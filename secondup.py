import turtle
import time
def all():
        col=['yellow','red','green','blue','red']
        t=turtle.Turtle()
        screen=turtle.Screen()
        screen.bgcolor('black')
        t.speed(30)
        for i in range(300): 
                  t.color(col[i%4])
                  t.forward(i*4)
                  t.left(150)
                  t.width(2)

def rouge(): 
        col=['red']
        t=turtle.Turtle()
        screen=turtle.Screen()
        screen.bgcolor('black')
        t.speed(30)
        for i in range(300): 
                 t.color(col[i%4])
                 t.forward(i*4)
                 t.left(150)
                 t.width(2)
        
while (True):
        all() 
        
        
         



        

    