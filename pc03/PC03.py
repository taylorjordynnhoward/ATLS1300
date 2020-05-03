#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
#========
#PC02- Animating with Turtles
#Howard
#DATE(200131)
#
#This code is designed to create animated art work using turtles
#========
from turtle import *
money = Screen()

money.bgcolor('white')
#money.bgpic("mountainrange.gif")

money.bgcolor('white')
money.bgpic("mountain.gif")

money.screensize(600,400)
money.update()

taylor = Turtle()
turtleImage = "skier.gif"
taylor.turtlesize(2)
money.register_shape(turtleImage)
taylor.shape(turtleImage)
taylor.left(90)
taylor.forward(100)
taylor.right(145)
taylor.forward(100)

monkey = Turtle()
turtleImage = "SNOW.gif"
money.register_shape(turtleImage)
monkey.hideturtle()
monkey.goto(0,260)
monkey.showturtle()
monkey.shape(turtleImage)
#got image off google then converted to gif

tricks = Turtle()
turtleImage = "2SNOW.gif"
money.register_shape(turtleImage)
tricks.shape(turtleImage)
tricks.hideturtle()
tricks.goto(-150,260)
tricks.showturtle()
#got image off google then converted to gif

sebastian = Turtle()
turtleImage = "nieve.gif"
money.register_shape(turtleImage)
sebastian.shape(turtleImage)
sebastian.hideturtle()
sebastian.goto(150,260)
sebastian.showturtle()
#got image off google then converted to gif




monkey.right(90)
monkey.forward(35)
tricks.right(90)
tricks.forward(35)
sebastian.right(90)
sebastian.forward(35)
