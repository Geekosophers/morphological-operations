# from math import *
from OpenGL.GL import *

def drawOne(posx,posy,kernel,HEIGHT=0):
    sides = 32    
    radius = 0.25      
    if(kernel):
        glVertex3f(posx,posy-0.25,HEIGHT)
        glVertex3f(posx,posy+0.25,HEIGHT)
    else:
        glVertex2f(posx,posy-0.25)
        glVertex2f(posx,posy+0.25)