#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#========
#PC04- Interactive Robot
#Howard_Bond
#DATE(20200214)
#
#This code is designed to create an interactive robot that moves on command
#========
import pygame
from random import *

pygame.init() #initializes all pygame functions
money = pygame.display.set_mode((400,600)) #create window


#original color RGB
revert = (200,200,250)

Run = True
x = 50
y = 50
speed = 5
scale = 1
color = (200,200,250)
width = 50
height = 40
vel = 5

#GAME LOOP
Run = True
while Run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            Run = False
#below (lines 37-45 from class)   
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

#change robot color      
    if keys[pygame.K_SPACE]:
         color = (252, 193, 171)

#to revert robot back to original color, press return key
    if keys[pygame.K_RETURN]:
        color = (revert)
            
         
#from class
    money.fill((244, 227, 255))
    pygame.draw.rect(money, color,(x,y,width,height))
    pygame.display.update()
    
