from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
#timmy_the_turtle.shape("turtle")

timmy_the_turtle.shape("classic")
timmy_the_turtle.color("black")

length = 100
angle = 90
iterator = 0

while iterator < 4:
    timmy_the_turtle.forward(length)
    timmy_the_turtle.right(angle)
    print(iterator)
    iterator += 1




screen = Screen()
screen.exitonclick()