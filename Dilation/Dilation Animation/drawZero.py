from math import *
from OpenGL.GL import *

def drawZero(posx,posy,kernel,HEIGHT=0):
    sides = 32    
    radius = 0.25    
        
    for j in range(100):    
        cosine = radius * cos(j*2*pi/sides) + posx    
        sine = radius * sin(j*2*pi/sides) + posy    
        if(kernel):
            glVertex3f(cosine,sine,HEIGHT)
        else:
            glVertex2f(cosine,sine)