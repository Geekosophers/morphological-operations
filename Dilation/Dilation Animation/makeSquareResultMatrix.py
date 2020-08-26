def makeSquareResultMatrix(n1,n2):
    resultSquares = []
    squareResultMatrix = []

    def setVertices(x,y):
        resultSquares.append([(x,y,0),(x+1,y,0),(x+1,y-1,0),(x,y-1,0)])

    for y in range(1,n2-1):
        for x in range(1,n1-1):
            setVertices(x+n1+1,-y)
        squareResultMatrix.append(resultSquares)
        resultSquares = []

    return squareResultMatrix