from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
#timmy_the_turtle.shape("turtle")

timmy_the_turtle.shape("classic")
timmy_the_turtle.color("black")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "wheat"]
length = 100
angle = 120
iterator = 0
number_of_sides = 3


while number_of_sides<11:
    while iterator < number_of_sides:
        timmy_the_turtle.forward(length)
        timmy_the_turtle.right(angle)
        print(iterator)
        iterator += 1
    iterator = 0
    number_of_sides +=1
    angle = 360/number_of_sides
    timmy_the_turtle.color(random.choice(colours))




screen = Screen()
screen.exitonclick()