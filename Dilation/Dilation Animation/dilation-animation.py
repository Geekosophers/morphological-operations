import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import cv2
import numpy as np
from math import *
from PIL import Image

from graphics import Graphics
from makeKernelMatrix import makeKernelMatrix
from makeSquareMatrix import makeSquareMatrix 
from makeSquareResultMatrix import makeSquareResultMatrix
from drawOne import drawOne
from drawZero import drawZero
import textures


HEIGHT = 3 # distance of kernel from x-y plane

img = cv2.imread('./Dilation/assets/dilation7x7sample2.jpg',0)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

n1, n2 = img.shape
n1+=2 # horizontal number of pixels plus 2 for padding
n2+=2 # vertical number of pixels plus 2 for padding

threshNew = [['' for j in range(n1)] for i in range(n2)]
resultMatrix = [['' for j in range(n1)] for i in range(n2)]
dilationSquareMatrixFront = [[[(2+n1,-n2-2,0),(2+n1,0.5-n2-2,1),(n1-2,0.5-n2-2,1),(n1-2,-n2-2,0)]]]
dilationSquareMatrixBack = [[[(2+n1,-n2-2+1,0),(2+n1,0.5-n2-2,1),(n1-2,0.5-n2-2,1),(n1-2,-n2-2+1,0)]]]

for y in range(n2):
    for x in range(n1):
        if(y==0 or x==0 or y==n2-1 or x==n1-1):
            threshNew[y][x] = 0
        else:
            threshNew[y][x] = thresh1[y-1][x-1]
        resultMatrix[y][x] = ''


thresh1 = np.array(threshNew,np.uint8)
kernel = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], np.uint8)
kn1, kn2 = kernel.shape


def main():
    pygame.init()
    display = (1000,600)
    img = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    
    glTranslatef(-n1, n1/3, -(n1+n2))

    glEnable( GL_LINE_SMOOTH );
    glEnable( GL_POLYGON_SMOOTH );
    glHint( GL_LINE_SMOOTH_HINT, GL_NICEST );
    glHint( GL_POLYGON_SMOOTH_HINT, GL_NICEST );
    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    glEnable(GL_MULTISAMPLE);  

    glRotatef(20, 0, 0, 1)
    glRotatef(-50, 1, 0, 0)
    glRotatef(20, 0, 1, 0)

    xindex = 0
    yindex = 0

    texture = textures.Texture(True,n1,n2)
    texture.loadTexture(0)

    tmp_texture = textures.Texture(True,n1,n2)
    tmp_texture.loadTexture(1)
    tmp_texture.set_vertices(1)

    tmp_texture2 = textures.Texture(True,n1,n2)
    tmp_texture2.loadTexture(2)
    tmp_texture2.set_vertices(2)

    rate=0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0, -1, 0)
                elif event.button == 5:
                    glTranslatef(0, 1, 0)
            keys = pygame.key.get_pressed()
            if keys[K_LEFT]:
                glTranslatef(1, 0, 0)
            if keys[K_RIGHT]:
                glTranslatef(-1, 0, 0)
            if keys[K_UP]:
                glTranslatef(0, 0, -1)
            if keys[K_DOWN]:
                glTranslatef(0, 0, 1)

        glClearColor(0, 1, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        if(xindex==0 and yindex==0):
            for y in range(n2):
                for x in range(n1):
                    resultMatrix[y][x] = ''

        texture.draw()
        tmp_texture2.draw()
        Graphics(xindex,yindex,HEIGHT,kn1,kn2,n1,n2,squareMatrix,kernel,thresh1,squareResultMatrix,resultMatrix,dilationSquareMatrixBack,dilationSquareMatrixFront)
        tmp_texture.draw()
        
        if(rate==0):
            xindex = (xindex+1)%(n1-kn1+1)
            if(xindex==0):
                yindex = (yindex+1)%(n2-kn2+1)

        rate = (rate+1)%10
    
        pygame.display.flip()
        pygame.time.wait(10)

squareMatrix = makeSquareMatrix(n1,n2)
squareResultMatrix = makeSquareResultMatrix(n1,n2)
kernelSquareMatrix = makeKernelMatrix(0,0,HEIGHT,kn1,kn2)
main()



# NOTE: Here x and y denotes the axis in the 2d space
# ------------------->x
# |
# |
# |
# |
# |
# \/
# y
