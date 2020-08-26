def makeKernelMatrix(xindex,yindex,HEIGHT,kn1,kn2):
    kernelSquares = []
    kernelSquareMatrix = []

    kernelSquareMatrix = []

    def setKernel(x,y):
        kernelSquares.append([(x+xindex,y-yindex,HEIGHT),(x+1+xindex,y-yindex,HEIGHT),(x+1+xindex,y-1-yindex,HEIGHT),(x+xindex,y-1-yindex,HEIGHT)])
    
    for y in range(kn2):
        for x in range(kn1):
            setKernel(x,-y)
        kernelSquareMatrix.append(kernelSquares)
        kernelSquares = []

    return kernelSquareMatrix