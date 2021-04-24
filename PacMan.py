import random
import turtle
import freegames
from freegames import floor, vector
from turtle import *

print("Hello")
state = {'score': 0}
path = Turtle(visible=False)
writer = Turtle(visible=False)
aim = vector(5,0)
pacman = vector(-40,-80)
ghosts = [
    [vector(-180,160), vector(5,0)]
    [vector(-180,-160), vector(0,5)]
    [vector(100,160), vector(0,-5)]
    [vector(100,-160), vector(-5,0)]
]

tiles = [

    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,


]
s = turtle.getscreen()
t = turtle.Turtle()

t.right(90)
t.forward(100)
t.left(90)
t.backward(100)

