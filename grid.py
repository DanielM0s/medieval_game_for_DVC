import turtle
import time

starting_time = time.time()
time_limit = 10


# Set up the screen
screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor("white")
screen.title("Figure Movement")
turtle.speed(0)
# Set up the grid
grid_size = 40
grid_spacing = 20
max_distance = 10

# Draw the grid
for i in range(grid_size):
    x = -grid_size * grid_spacing // 2 + i * grid_spacing
    turtle.penup()
    turtle.goto(x, grid_size * grid_spacing // 2)
    turtle.pendown()
    turtle.goto(x, -grid_size * grid_spacing // 2)
    turtle.penup()
    turtle.goto(-grid_size * grid_spacing // 2, x)
    turtle.pendown()
    turtle.goto(grid_size * grid_spacing // 2, x)

# Set up the figure
figure = turtle.Turtle()
figure.shape("circle")
figure.color("blue")
figure.penup()
figure.goto(0, 0)

# Set up the other figure
other_figure = turtle.Turtle()
other_figure.shape("circle")
other_figure.color("red")
other_figure.penup()
other_figure.goto(200, 200)

# Set up the input function
def get_coordinates():
    while True:
        x = screen.textinput("Enter X Coordinate", "X:")
        y = screen.textinput("Enter Y Coordinate", "Y:")
        if x and y:
            try:
                x = int(x)
                y = int(y)
                if -grid_size // 2 <= x < grid_size // 2 and -grid_size // 2 <= y < grid_size // 2:
                    distance = ((x - figure.xcor()) ** 2 + (y - figure.ycor()) ** 2) ** 0.5
                    if distance <= max_distance:
                        figure.goto(x * grid_spacing, y * grid_spacing)
                        time.sleep()
                        turtle.Screen().bye()
                        # Exit the loop if the coordinates are valid
                        break    
                    else:
                        print("Invalid coordinates. Please enter coordinates within the maximum distance.")
                else:
                    print("Invalid coordinates. Please enter coordinates within the grid.")
            except ValueError:
                print("Invalid input. Please enter integers.")
        else:
            print("Invalid input. Please enter both X and Y coordinates.")

# Set up the key bindings
screen.onkeypress(get_coordinates, "space")
screen.listen()
# Start the main loop
while (time.time() - starting_time) < time_limit:
    turtle.mainloop()




