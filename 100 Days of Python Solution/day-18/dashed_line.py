from turtle import Turtle, Screen

tt_turtle = Turtle()
#timmy_the_turtle.shape("turtle")

tt_turtle.shape("classic")
tt_turtle.color("black")

for _ in range(10):
    tt_turtle.forward(5)
    tt_turtle.color("white")
    tt_turtle.forward(5)
    tt_turtle.color("black")


screen = Screen()
screen.exitonclick()