from makeKernelMatrix import makeKernelMatrix
from drawZero import drawZero
from drawOne import drawOne
from OpenGL.GL import *

edges = [
    (0,1),
    (1,2),
    (2,3),
    (3,0)
]

def Graphics(xindex,yindex,HEIGHT,kn1,kn2,n1,n2,squareMatrix,kernel,thresh1,squareResultMatrix,resultMatrix,dilationSquareMatrixBack,dilationSquareMatrixFront):
    
    kernelSquareMatrix = makeKernelMatrix(xindex,yindex,HEIGHT,kn1,kn2)
    
    # draw edge for Original Image text
    glBegin(GL_LINES)
    glColor3fv((0,0,0))
    matrix =[[(5,-n1-0.5,-1),(5,-n1,0),(0,-n1,0),(0,-n1-0.5,-1)]]
    for vertices in matrix:
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
    glEnd()

    # draw edge for Result Image text
    glBegin(GL_LINES)
    glColor3fv((0,0,0))
    matrix =[[(7+n1,-n2+1-0.5,-1),(7+n1,-n2+1,0),(n1+2,-n2+1,0),(n1+2,-n2+1-0.5,-1)]]
    for vertices in matrix:
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
    glEnd()

    # coloring padded image matrix
    glBegin(GL_QUADS)
    for y in range(n2):
        for x in range(n1):
            for vertex in squareMatrix[y][x]:
                if(x==0 or y==0 or x==n1-1 or y==n2-1):
                    glColor3fv((0.5,0.5,0.5))
                    glVertex3fv(vertex)
                else:
                    glColor3fv((0.162,0.162,0.162))
                    glVertex3fv(vertex)
    glEnd()

    # highlighting padded image imatrix operations (green or yellow)
    glBegin(GL_QUADS)
    matchFound = False
    for y in range(kn2):
        for x in range(kn1):
            if(kernel[y][x]==1):
                for vertex in squareMatrix[y+yindex][x+xindex]:
                    if(thresh1[y+yindex][x+xindex]==255):
                        glColor3fv((0.13,0.297,0.13)) # green color
                        glVertex3fv(vertex)
                        matchFound = 255
                    else:
                        glColor3b((95),(75),(139))
                        glVertex3fv(vertex)

            else:
                for vertex in squareMatrix[y+yindex][x+xindex]:
                    glColor3fv((0.192,0.192,0.192))
                    glVertex3fv(vertex)
    glEnd()

    if(matchFound):
        resultMatrix[yindex+1][xindex+1] = 255
    else:
        resultMatrix[yindex+1][xindex+1] = 0

    # draw 0s and 1s for padded image matrix
    glBegin(GL_LINES)
    glColor3fv((1,1,1))
    for y in range(n2):
        for x in range(n1):
            if(thresh1[y][x]==0):
                drawZero(0.5+x,-0.5-y,False)
            else:
                drawOne(0.5+x,-0.5-y,False)
    glEnd()

    # draw image matrix with padding
    glBegin(GL_LINES)
    glColor3fv((1,1,1))
    for squares in squareMatrix:
        for vertices in squares:
            for edge in edges:
                for vertex in edge:
                    glVertex3fv(vertices[vertex])
    glEnd()

    # coloring result matrix
    glBegin(GL_QUADS)
    for y in range(n2-2):
        for x in range(n1-2):
            for vertex in squareResultMatrix[y][x]:
                glColor3fv((0.162,0.162,0.162))
                glVertex3fv(vertex)
    glEnd()

    # draw result matrix with padding
    glBegin(GL_LINES)
    glColor3fv((1,1,1))
    for squares in squareResultMatrix:
        for vertices in squares:
            for edge in edges:
                for vertex in edge:
                    glVertex3fv(vertices[vertex])
    glEnd()

    # draw 0s and 1s for result matrix
    glBegin(GL_LINES)
    glColor3fv((1,1,1))
    for y in range(n2):
        for x in range(n1):
            if(resultMatrix[y][x]==0):
                drawZero(0.5+x+1+n1,-0.5-y,False)
            elif(resultMatrix[y][x]==255):
                drawOne(0.5+x+1+n1,-0.5-y,False)
    glEnd()

    # drawLine between kernel and highlight image area
    glBegin(GL_LINES)
    glColor3fv((0,0,0))
    
    glVertex3fv(squareMatrix[0+yindex][0+xindex][0])
    glVertex3fv(kernelSquareMatrix[0][0][0])
    
    glVertex3fv(squareMatrix[0+yindex][2+xindex][1])
    glVertex3fv(kernelSquareMatrix[0][2][1])
    
    glVertex3fv(squareMatrix[2+yindex][0+xindex][3])
    glVertex3fv(kernelSquareMatrix[2][0][3])
    
    glVertex3fv(squareMatrix[2+yindex][2+xindex][2])
    glVertex3fv(kernelSquareMatrix[2][2][2])
    
    glEnd()

    # highlighting kernel matrix 1s
    glBegin(GL_QUADS)
    for y in range(kn2):
        for x in range(kn1):
            if(kernel[y][x]==1):
                # highlight kernel cells containing 1
                for vertex in kernelSquareMatrix[y][x]:
                    glColor3b((95),(75),(139))
                    glVertex3fv(vertex)
            else:
                for vertex in kernelSquareMatrix[y][x]:
                    glColor3fv((0.192,0.192,0.192))
                    glVertex3fv(vertex)
    glEnd()

    # draw kernel
    glBegin(GL_LINES)
    glColor3fv((1,1,1))
    for kernelSquares in kernelSquareMatrix:
        for vertices in kernelSquares:
            for edge in edges:
                for vertex in edge:
                    glVertex3fv(vertices[vertex])
    glEnd()

    # draw 0s and 1s for kernel
    glBegin(GL_LINES)
    glColor3fv((1,1,1))
    for y in range(kn2):
        for x in range(kn1):
            if(kernel[y][x]==0):
                drawZero(0.5+x+xindex,-0.5-y-yindex,True,HEIGHT)
            else:
                drawOne(0.5+x+xindex,-0.5-y-yindex,True,HEIGHT)
    glEnd()

    # draw dilation text back
    glBegin(GL_LINES)
    glColor3fv((0,0,0))
    for dilationSquares in dilationSquareMatrixBack:
        for vertices in dilationSquares:
            for edge in edges:
                for vertex in edge:
                    glVertex3fv(vertices[vertex])
    glEnd()
    
    # draw dilation text front
    glBegin(GL_LINES)
    glColor3fv((0,0,0))
    for dilationSquares in dilationSquareMatrixFront:
        for vertices in dilationSquares:
            for edge in edges:
                for vertex in edge:
                    glVertex3fv(vertices[vertex])
    glEnd()