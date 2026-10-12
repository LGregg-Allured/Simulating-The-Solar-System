#This is the second version of the code in the process to creating the final simulation of the solar system.
#Most of the code is taken from the first attempt "(2.1)Gravity.py"
#Leo Gregg-Allured
#leogreggallured@gmail.com
#Oct 12th 2026

##### Imports #####

import pygame as pyg

##### initialising pygame #####

screen_y = 720
screen_x =1280
pyg.init()
screen = pyg.display.set_mode((screen_x, screen_y))
clock = pyg.time.Clock()
running = True
Framerate = 60
current_frame = 0

#Positions of the red and blue circles/objects
Pos_red_x = screen_x / 2 + 150
Pos_red_y = screen_y / 2 + 400
Pos_blue_x = screen_x / 2 - 150
Pos_blue_y = screen_y / 2 

##### Initaliasing the Physics #####

Red_mass = 5000
Blue_mass = 2000

Initialvelocity_red_x = 0
Initialvelocity_red_y = 0 

Initialvelocity_blue_x = 0
Initialvelocity_blue_y = 0 

time = 1 / Framerate

#Scientific constants

pi = 3.14159
G = 2000 #this can be any constant and will later be set to the big G constant for gravity we know in real units for the solar system simulation

def Force_x():
    
    return

def Force_y():
    return