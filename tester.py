import turtle
from turtle import *

turtle.title("rainbow spiral")
speed(0)
bgcolor("black")
r,g,b=255,0,0

for i in range(360*1000):
    colormode(255)
    if i<255//3:
        g+=3
    elif i<255*2//3:
        r-=3
    elif i<255:
        b+=3
    elif i<255*4//3:
        g-=3
    elif i<255*5//3:
        r+=3
    elif i<255*6//3:
        b-=3
    elif i<255*7//3:
        g+=3
    elif i<255*8//3:
        r-=3
    elif i<255*9//3:
        b+=3
    elif i<255*97//3:
        g-=3
    elif i<255*193//3:
        r+=3
    elif i<255*290//3:
        b-=3
    elif i<255*386//3:
        g+=3
    elif i<255*482//3:
        r-=3
    elif i<255*578//3:
        b+=3
    else:
        break
    fd(50+i)
    rt(91)
    pencolor(r,g,b)
done()

