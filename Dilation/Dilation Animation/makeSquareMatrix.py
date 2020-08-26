def makeSquareMatrix(n1,n2):
    squares = []
    squareMatrix = []

    def setVertices(x,y):
        squares.append([(x,y,0),(x+1,y,0),(x+1,y-1,0),(x,y-1,0)])

    for y in range(n2):
        for x in range(n1):
            setVertices(x,-y)
        squareMatrix.append(squares)
        squares = []

    return squareMatrix