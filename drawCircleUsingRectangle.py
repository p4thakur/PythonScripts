import turtle


def drawSquare(some_turtle):
	for i in range(0,4):
		some_turtle.forward(100)
		some_turtle.right(90)


def drawRect():
	window=turtle.Screen()
	window.bgcolor("red")

	brad=turtle.Turtle()
	brad.shape("turtle") # this mean my drawing tool will lokk like a turtle
	brad.color("green")
	brad.speed(2)

	for i in range(0,36):
		#drwaw a square and let rotate it by 10 degree
		drawSquare(brad)
		brad.right(10)
     
    #window.exitonclick()


drawRect()

