#This is a simple python project to simulate gravity between two bodys as a simple force
#Leo Gregg-Allured
#leogreggallured@gmail.com
#july 7th 2026

import pygame as pyg
import os

#initliasing the folder to save the simulation frames in for the lab book
output_folder = "simulation frames"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#initliase pyg
screen_y = 720
screen_x =1280
pyg.init()
screen = pyg.display.set_mode((screen_x, screen_y))
clock = pyg.time.Clock()
running = True
Framerate = 60
current_frame = 0

#initliase the physcics

time = 1 / Framerate

pi = 3.14159
G = 2000 #this can be any constant and will later be set to the big G constant for gravity we know irl for the solar system simulation

Pos_red_x = screen_x / 2 + 150
Pos_red_y = screen_y / 2 + 400
Pos_blue_x = screen_x / 2 - 150
Pos_blue_y = screen_y / 2 

Red_mass = 5000
Blue_mass = 2000

Initialvelocity_red_x = 0
Initialvelocity_red_y = 0 
Initialvelocity_blue_x = 0
Initialvelocity_blue_y = 0 

#this body of code is the functions used to determine the x and y positions of the next frame

def Get_pos_red_x(): #this is where we will update the position of the red circle dependant on the forces acting on it

    global Pos_red_x
    global time
    global Initialvelocity_red_x

    #can use suvat to determine the next position of the object as a function of the acceloration due to the forces acting on it
    #needs to update every t = 1/framerate seconds

    #Calculate the force acting on red from blue

    difference_x = abs( Pos_blue_x - Pos_red_x)
    print(difference_x)
    if difference_x != 0:
        force_on_red_x = -( G * Blue_mass * Red_mass ) / ( (difference_x)**2 ) #Newtons law of gravitation without direction
    else:
        force_on_red_x = 0
    print(force_on_red_x)

    #Calculate the new position of the object in x after one step in time

    Pos_red_x_OLD = Pos_red_x

    Pos_red_x += Initialvelocity_red_x * time + (1/2) * (force_on_red_x / Red_mass) * ( time**2 )

    #calculate the new initial velocity for the next calculation

    Initialvelocity_red_x = ( Pos_red_x - Pos_red_x_OLD ) / time

    return (Pos_red_x)

def Get_pos_red_y(): #this is where we will update the position of the red circle dependant on the forces acting on it
    
    global Pos_red_y
    global time
    global Initialvelocity_red_y

    difference_y = abs( Pos_blue_y - Pos_red_y)
    print(difference_y)
    if difference_y != 0:
        force_on_red_y = - ( G * Blue_mass * Red_mass ) / ( (difference_y)**2 ) #Newtons law of gravitation without direction
    else:
        force_on_red_y = 0
    print(force_on_red_y)

    #Calculate the new position of the object in x after one step in time

    Pos_red_y_OLD = Pos_red_y

    Pos_red_y += Initialvelocity_red_y * time + (1/2) * (force_on_red_y / Red_mass) * ( time**2 )

    #calculate the new initial velocity for the next calculation

    Initialvelocity_red_y = ( Pos_red_y - Pos_red_y_OLD ) / time

    return (Pos_red_y)



while running:

    # poll for events
    # pyg.QUIT event means the user clicked X to close your window
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False

    screen.fill("white") # fills the screen with the colour white

    #This body of code is where each frame is drawn out and rendered

    pyg.draw.circle( #Render the first circle "red"
        screen,
        "red",
        (Get_pos_red_x(), Get_pos_red_y()),
        40
    )

    pyg.draw.circle( #Render the second circle "blue"
        screen,
        "blue",
        (Pos_blue_x, Pos_blue_y),
        40
    )

    pyg.display.flip()

    current_frame += 1
    print(current_frame)

    frame_filename = os.path.join(output_folder, f"frame_{current_frame:04d}.png")
    pyg.image.save(screen, frame_filename)

    clock.tick(Framerate)

pyg.quit()