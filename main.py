import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
loc = [(238, 246, 240), (201, 112, 164), (239, 241, 246), (152, 50, 75), (221, 138, 201), (57, 126, 95), (170, 44, 152),
       (138, 20, 31), (135, 183, 163), (196, 75, 94), (49, 88, 121), (143, 149, 177), (95, 77, 75), (76, 32, 39),
       (164, 157, 146), (16, 71, 98), (232, 165, 176), (54, 48, 46), (32, 76, 61), (22, 89, 83), (182, 176, 204),
       (141, 25, 22), (86, 127, 147), (45, 85, 66), (8, 53, 68), (177, 97, 94), (222, 182, 177), (109, 151, 128)]
tim = Turtle()
tim.penup()
tim.speed("fastest")
tim.hideturtle()
init_pos= tim.setpos(-250,-250)
for j in range(10):
    for i in range(10):

        tim.dot(20, random.choice(loc))
        tim.forward(50)

    tim.setpos(-250,-250 + 50*(j+1))
screen = Screen()
screen.exitonclick()
