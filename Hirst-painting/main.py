# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
#from turtle import Turtle, Screen, colormode
import turtle as t
import random

t.colormode(255)
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102),
              (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


# here we created turtle object
tim =t.Turtle()
tim.penup()
tim.setheading(225)
tim.forward(350)
tim.setheading(0)
tim.pendown()
# here we set turtle's speed 
tim.speed("fastest")
posun_radku=0

while posun_radku<10:
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        # here we moved the turtle forward
        tim.penup()
        tim.forward(50)
        tim.pendown()
    posun_radku += 1
    #print(f"{posun_radku}")
    if (posun_radku < 10):
        tim.penup()
        tim.backward(500)
        tim.setheading(90)
        tim.forward(50)
        tim.right(90)
        tim.pendown()


screen = t.Screen()
screen.exitonclick()