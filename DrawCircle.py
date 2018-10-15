import turtle  # this is used to drawstuff

# I can draw triangle circland aother shapes too
def drawRect():
	#first let make our window where i willdraw my circle
	window=turtle.Screen()
	#make it red color
	window.bgcolor("red")
	#Turtle is a class inside our turtle module
	# below step call the init method of this calss which create the instance of out turtle class
	brad=turtle.Turtle() 
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)
	#other thing that i can add are
	#brad.color("yellow")
	#brad.speed(2)
	#brad.shape("turtle")

	window.exitonclick()


drawRect()