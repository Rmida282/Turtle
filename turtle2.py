from turtle import *


speed(5)

bgcolor('black')

x = 1
r,g,b = 255,0,0
while x < 600:
    
    colormode(255) 
    if(x<255//3):
        g+=3
    elif(x<255*2//3):
        r-=3
    elif(x<255):
        b+=3
    elif(x<255*4//3):
        g-=3
    elif(x<255*5//3):
        r+=3
    else:
        b-=3
    fd(50+x)
    rt(91)
    pencolor(r,g,b)
                    

    fd(50 + x)
    rt(90.911)


    x = x+1 

exitonclick() 

