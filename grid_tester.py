# import package and making objects
import turtle


sc=turtle.Screen()
sc.setup(1000,1000) # bigger grid
trtl=turtle.Turtle()

# method to draw y-axis lines
def drawy(val):
	
	# line
	trtl.forward(500)
	
	# set position
	trtl.up()
	trtl.setpos(val,500)
	trtl.down()
	
	# another line
	trtl.backward(500)
	
	# set position again
	trtl.up()
	trtl.setpos(val+20,0)
	trtl.down()
	
# method to draw y-axis lines
def drawx(val):
	
	# line
	trtl.forward(500)
	
	# set position
	trtl.up()
	trtl.setpos(500,val)
	trtl.down()
	
	# another line
	trtl.backward(500)
	
	# set position again
	trtl.up()
	trtl.setpos(0,val+20)
	trtl.down()
	
# method to label the graph grid
def lab():
	
	# set position
	trtl.penup()
	trtl.setpos(250,250)
	trtl.pendown()
	
	# write 0
	trtl.write(0,font=("Verdana", 20, "bold"))
	
	# set position again
	trtl.penup()
	trtl.setpos(500,250)
	trtl.pendown()
	
	# write x
	trtl.write("x",font=("Verdana", 20, "bold"))
	
	# set position again
	trtl.penup()
	trtl.setpos(250,500)
	trtl.pendown()
	
	# write y
	trtl.write("y",font=("Verdana", 20, "bold"))
	

# Main Section
# set screen
sc.setup(1000,1000) 

# set turtle features
trtl.speed(100)
trtl.left(90) 
trtl.color('lightgreen')

# y lines
for i in range(50):
	drawy(20*(i+1))

# set position for x lines
trtl.right(90)
trtl.up()
trtl.setpos(0,0)
trtl.down()

# x lines
for i in range(50):
	drawx(20*(i+1))

# axis 
trtl.color('green')

# set position for x axis
trtl.up()
trtl.setpos(0,250)
trtl.down()

# x-axis
trtl.forward(500)

# set position for y axis
trtl.left(90)
trtl.up()
trtl.setpos(250,0)
trtl.down()

# y-axis
trtl.forward(500)

# labeling
lab()

# hide the turtle
trtl.hideturtle()

