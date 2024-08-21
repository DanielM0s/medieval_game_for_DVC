from turtle import Screen, Turtle

FONT = ('Arial', 30, 'normal')

def countdown(time):
    screen.onclick(None)  # disable click until countdown completes
    turtle.clear()

    turtle.penup()
    turtle.goto(-500, 250)
    turtle.pendown()

    if time > 0:
        turtle.write(time, align='center', font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        turtle.write("Click Screen", align='center', font=FONT)
        screen.onclick(lambda x, y: countdown(30))

turtle = Turtle()
turtle.hideturtle()

screen = Screen()
countdown(30)
screen.mainloop()

