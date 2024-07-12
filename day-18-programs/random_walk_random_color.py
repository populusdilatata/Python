import turtle as t
import random

timmy_the_turtle = t.Turtle()
t.colormode(255)
#timmy_the_turtle.shape("turtle")

timmy_the_turtle.shape("classic")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "wheat"]
length = 30
angle = [0, 90, 180, 270]
timmy_the_turtle.pensize(15)
timmy_the_turtle.speed("fastest")

for _ in range(200):
    timmy_the_turtle.forward(length)
    timmy_the_turtle.right(random.choice(angle))
    timmy_the_turtle.color(random_color())

screen = Screen()
screen.exitonclick()