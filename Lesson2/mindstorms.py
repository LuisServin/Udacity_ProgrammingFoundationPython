# !usr/bin/env python

# import the graphic library to draw with the help of a turtle
import turtle

def draw_square(some_turtle):
	for i in range(0,4):
		some_turtle.forward(100)
		some_turtle.right(90)	

def draw_art():
	# create a window to draw on it
	window = turtle.Screen()
	# set the background color
	window.bgcolor("cyan")

	# create the turtle and customize it
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("blue")
	brad.speed(2)
	for i in range(0,36):
		# draw a square
		draw_square(brad)
		brad.right(10)

	# create a turtle angie a draw a circle
	#angie = turtle.Turtle()
	#angie.shape("arrow")
	#angie.color("red")
	#angie.circle(100)

	window.exitonclick()

draw_art()