from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
#timmy_the_turtle.shape("turtle")

timmy_the_turtle.shape("classic")
timmy_the_turtle.color("black")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "wheat"]
length = 30
angle = [0, 90, 180, 270]
timmy_the_turtle.pensize(15)
timmy_the_turtle.speed("fastest")

for _ in range(200):
    timmy_the_turtle.forward(length)
    timmy_the_turtle.right(random.choice(angle))
    timmy_the_turtle.color(random.choice(colours))

screen = Screen()
screen.exitonclick()