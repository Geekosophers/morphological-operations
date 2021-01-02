import pygame, sys
from pygame.locals import *
import numpy as np
from dilationAnimation import main

def toggleImageArrayValue(imageArray,mouse):
    m = len(imageArray)
    n = len(imageArray[0])
    for i in range(m):
        for j in range(n):
            if (500+50*i <= mouse[0] <= 550+50*i) and (150+50*j <= mouse[1] <= 200+50*j):
                if(imageArray[i][j]=='0'):
                    imageArray[i][j] = '1'
                else:
                    imageArray[i][j] = '0'
                return

def toggleKernelArrayValue(kernelArray,mouse):
    m = len(kernelArray)
    n = len(kernelArray[0])
    for i in range(m):
        for j in range(n):
            if (200+50*i <= mouse[0] <= 250+50*i) and (150+50*j <= mouse[1] <= 200+50*j):
                if(kernelArray[i][j]=='0'):
                    kernelArray[i][j] = '1'
                else:
                    kernelArray[i][j] = '0'
                return

def getInputs():
    pygame.init()

    X = 1000
    Y = 563

    m = 0
    n = 0
    mk = 0
    nk = 0

    DISPLAY=pygame.display.set_mode((X,Y),0,32)

    whiteColor = (255,255,255)
    squareColor = (75,83,153)
    borderColor = (225,78,135)
    greenColor = (93,186,124)
    colorLight = (170,170,170)
    colorDark = (100,100,100)

    DISPLAY.fill(whiteColor)
    smallfont = pygame.font.SysFont('Corbel',30)
    
    imageRows =  ''
    imageCols = ''
    kernelRows = ''
    kernelCols = ''
    selectedBox = 0 # random integer apart from 1,2,3,4

    imageArray = []
    renderImage = False
    imageGoPressed = False
    kernelArray = []
    renderKernel = False
    kernelGoPressed = False

    # Kernel Matrix Text
    DISPLAY.blit(smallfont.render('Kernel Matrix' ,True,squareColor), (200,45))
    
    # Kernel Go Button
    pygame.draw.rect(DISPLAY,greenColor,(320,75,40,25))
    DISPLAY.blit(smallfont.render('Go' ,True,whiteColor), (325,78))
    
    # Image Matrix Text
    DISPLAY.blit(smallfont.render('Image Matrix' ,True,squareColor), (500,45))
    
    # Image Go Button
    pygame.draw.rect(DISPLAY,greenColor,(620,75,40,25))
    DISPLAY.blit(smallfont.render('Go' ,True,whiteColor), (625,78))

    # x Text
    DISPLAY.blit(smallfont.render('x' ,True,squareColor), (245,78))
    DISPLAY.blit(smallfont.render('x' ,True,squareColor), (545,78))

    # START Text
    startText = smallfont.render('START' , True , whiteColor)

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Image Row Label Click Handler
                if(500 <= mouse[0] <= 535 and 75 <= mouse[1] <= 100):
                    pygame.draw.rect(DISPLAY,whiteColor,(198,73,39,29),1)
                    pygame.draw.rect(DISPLAY,whiteColor,(263,73,39,29),1)
                    pygame.draw.rect(DISPLAY,borderColor,(498,73,39,29),1)
                    pygame.draw.rect(DISPLAY,whiteColor,(563,73,39,29),1)
                    selectedBox = 3
                # Image Column Label Click Handler
                elif(565 <= mouse[0] <= 600 and 75 <= mouse[1] <= 100):
                    pygame.draw.rect(DISPLAY,whiteColor,(198,73,39,29),1)
                    pygame.draw.rect(DISPLAY,whiteColor,(263,73,39,29),1)
                    pygame.draw.rect(DISPLAY,whiteColor,(498,73,39,29),1)
                    pygame.draw.rect(DISPLAY,borderColor,(563,73,39,29),1)
                    selectedBox = 4
                # Image Go Button Click Handler
                elif(620 <= mouse[0] <= 660 and 75 <= mouse[1] <= 100):
                    m = int(imageRows)
                    n = int(imageCols)
                    if(renderImage==True):
                        imageGoPressed = True
                    imageArray = []
                    for i in range(m):
                        rowList = []
                        for j in range(n):
                            rowList.append('0')
                        imageArray.append(rowList)
                    renderImage = True
                # Kernel Row Label Click Handler
                elif(200 <= mouse[0] <= 235 and 75 <= mouse[1] <= 100):
                    pygame.draw.rect(DISPLAY,borderColor,(198,73,39,29),1)
                    pygame.draw.rect(DISPLAY,whiteColor,(263,73,39,29),1)
                    pygame.draw.rect(DISPLAY,whiteColor,(498,73,39,29),1)
                    pygame.draw.rect(DISPLAY,whiteColor,(563,73,39,29),1)
                    selectedBox = 1
                # Kernel Column Label Click Handler
                elif(265 <= mouse[0] <= 300 and 75 <= mouse[1] <= 100):
                    pygame.draw.rect(DISPLAY,whiteColor,(198,73,39,29),1)
                    pygame.draw.rect(DISPLAY,borderColor,(263,73,39,29),1)
                    pygame.draw.rect(DISPLAY,whiteColor,(498,73,39,29),1)
                    pygame.draw.rect(DISPLAY,whiteColor,(563,73,39,29),1)
                    selectedBox = 2
                # Kernel Go Button Click Handler
                elif(320 <= mouse[0] <= 360 and 75 <= mouse[1] <= 100):
                    mk = int(kernelRows)
                    nk = int(kernelCols)
                    if(renderKernel==True):
                        kernelGoPressed = True
                    kernelArray = []
                    for i in range(mk):
                        rowList = []
                        for j in range(nk):
                            rowList.append('0')
                        kernelArray.append(rowList)
                    renderKernel = True
                # On START Button Click
                elif 800 <= mouse[0] <= 800+140 and 75 <= mouse[1] <= 75+40:
                    for i in range(mk):
                        for j in range(nk):
                            kernelArray[i][j] = int(kernelArray[i][j])
                    for i in range(m):
                        for j in range(n):
                            if(imageArray[i][j]=='1'):
                                imageArray[i][j]=255
                            else:
                                imageArray[i][j]=0
                    try:
                        main(np.array(imageArray).T,np.array(kernelArray).T)
                    except:
                        pass
                else:
                    try:
                        # On Image Cell Click
                        toggleImageArrayValue(imageArray,mouse)
                    except:
                        pass
                    try:
                        # On Kernel Cell Click
                        toggleKernelArrayValue(kernelArray,mouse)
                    except:
                        pass

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if(selectedBox==1):
                        kernelRows = kernelRows[:-1]
                    elif(selectedBox==2):
                        kernelCols = kernelCols[:-1]
                    elif(selectedBox==3):
                        imageRows = imageRows[:-1]
                    elif(selectedBox==4):
                        imageCols = imageCols[:-1]
                else:
                    text = event.unicode
                    if(text>=str(0) and text<=str(9)):
                        if(selectedBox==1 and len(kernelRows)<2):
                            kernelRows += text
                        elif(selectedBox==2 and len(kernelCols)<22):
                            kernelCols += text
                        elif(selectedBox==3 and len(imageRows)<2):
                            imageRows += text
                        elif(selectedBox==4 and len(imageCols)<22):
                            imageCols += text

        # Kernel Text Label Boxes
        pygame.draw.rect(DISPLAY,squareColor,(200,75,35,25))
        DISPLAY.blit(smallfont.render(kernelRows ,True,whiteColor), (205,78))
        pygame.draw.rect(DISPLAY,squareColor,(265,75,35,25))
        DISPLAY.blit(smallfont.render(kernelCols ,True,whiteColor), (270,78))

        # Image Text Label Boxes
        pygame.draw.rect(DISPLAY,squareColor,(500,75,35,25))
        DISPLAY.blit(smallfont.render(imageRows ,True,whiteColor), (505,78))
        pygame.draw.rect(DISPLAY,squareColor,(565,75,35,25))
        DISPLAY.blit(smallfont.render(imageCols ,True,whiteColor), (570,78))

        # Render Image Matrix
        if(renderImage==True):
            if(imageGoPressed==True):
                for i in range(prevM):
                    for j in range(prevN):
                        pygame.draw.rect(DISPLAY,whiteColor,(500+51*i,150+51*j,50,50))
                imageGoPressed = False   
            else:
                for i in range(m):
                    for j in range(n):
                        pygame.draw.rect(DISPLAY,squareColor,(500+51*i,150+51*j,50,50))
                        DISPLAY.blit(smallfont.render(imageArray[i][j] , True , whiteColor) , (520+(51*i),165+51*j))

        # Render Kernel Matrix
        if(renderKernel==True):
            if(kernelGoPressed==True):
                for i in range(prevMK):
                    for j in range(prevNK):
                        pygame.draw.rect(DISPLAY,whiteColor,(200+51*i,150+51*j,50,50))
                kernelGoPressed = False
            else:
                for i in range(mk):
                    for j in range(nk):
                        pygame.draw.rect(DISPLAY,squareColor,(200+51*i,150+51*j,50,50))
                        DISPLAY.blit(smallfont.render(kernelArray[i][j] , True , whiteColor) , (220+(51*i),165+51*j))

        mouse = pygame.mouse.get_pos()
        
        # START Button
        if 800 <= mouse[0] <= 800+140 and 75 <= mouse[1] <= 75+40:
            pygame.draw.rect(DISPLAY,colorLight,[800,75,140,40])
        else:
            pygame.draw.rect(DISPLAY,colorDark,[800,75,140,40])

        DISPLAY.blit(startText , (840,85))
        
        prevM = m
        prevN = n
        prevMK = mk
        prevNK = nk

        pygame.display.update()

getInputs()