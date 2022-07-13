# import colorgram
#
# hirst_colors = colorgram.extract("spot_painting.jpg", 50)
#
# colors = [tuple(hirst_colors[n].rgb) for n in range(len(hirst_colors))]
#
# print(colors)

import turtle as t
import random

color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56), (106, 140, 124), (153, 202, 227), (48, 69, 71), (131, 128, 121)]

turtle = t.Turtle()
t.colormode(255)
turtle.speed("fastest")
turtle.pensize(2)
turtle.pu()


def draw_dots():
    for n in range(10):
        turtle.dot(20, random.choice(color_list))
        turtle.fd(50)


def reposition(pos):
    y = pos[1] + 50
    turtle.setx(0)
    turtle.sety(y)


for x in range(10):
    draw_dots()
    reposition(turtle.pos())

screen = t.Screen()
screen.exitonclick()
