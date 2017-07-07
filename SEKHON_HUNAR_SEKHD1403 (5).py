from __future__ import print_function
import random
# Constants we need in the program
northArrow = u'\u2191'
eastArrow = u'\u2192'
southArrow = u'\u2193'
westArrow = u'\u2190'
northEastArrow = u'\u21B1'
northWestArrow = u'\u21B0'
eastNorthArrow = u'\u2934'
eastSouthArrow = u'\u2935'
southEastArrow = u'\u21B3'
southWestArrow = u'\u21B2'
westNorthArrow = u'\u2B11'
westSouthArrow = u'\u2B10'

def readBoardSize():
     while True:
         n = int(input("Enter Board Size (min 5, max 20): "))
         if n >=5 and n <= 20:
             break
     return n


def createBoard(n):
     B = []
     for i in range(n):
         B.append([])
         for j in range(n):
             if random.random() < 0.75:
                 B[i].append("F")
             else:
                 B[i].append("O")
     return B

def markStartAndDestinationCells(B):
     B[0][0] = "S"
     B[len(B)-1][len(B[0])-1] = "D"

def printBoard(B):
     for i in range(25):
         print()
     for i in range(len(B)):
         print(" ", end="")
         for j in range(len(B[0])):
             print(B[i][j], end=" ")
         print()
     for i in range(3):
         print()
         
def getArrow(previousDirection, currentDirection):
     if previousDirection == "north" and currentDirection == "north":
         return northArrow
     elif previousDirection == "east" and currentDirection == "east":
         return eastArrow
     elif previousDirection == "south" and currentDirection == "south":
         return southArrow
     elif previousDirection == "west" and currentDirection == "west":
         return westArrow
     elif previousDirection == "north" and currentDirection == "south":
         return southArrow
     elif previousDirection == "east" and currentDirection == "west":
         return westArrow
     elif previousDirection == "south" and currentDirection == "north":
         return northArrow
     elif previousDirection == "west" and currentDirection == "east":
         return eastArrow
     elif previousDirection == "north" and currentDirection == "east":
         return northEastArrow
     elif previousDirection == "north" and currentDirection == "west":
         return northWestArrow
     elif previousDirection == "east" and currentDirection == "north":
         return eastNorthArrow
     elif previousDirection == "east" and currentDirection == "south":
         return eastSouthArrow
     elif previousDirection == "south" and currentDirection == "east":
         return southEastArrow
     elif previousDirection == "south" and currentDirection == "west":
         return southWestArrow
     elif previousDirection == "west" and currentDirection == "north":
         return westNorthArrow
     elif previousDirection == "west" and currentDirection == "south":
         return westSouthArrow



def isCellAlreadyVisited(B, currentRow, currentCol):
     if B[currentRow][currentCol] == "V":
         return True
     elif B[currentRow][currentCol] == northArrow:
         return True
     elif B[currentRow][currentCol] == eastArrow:
         return True
     elif B[currentRow][currentCol] == southArrow:
         return True
     elif B[currentRow][currentCol] == westArrow:
         return True
     elif B[currentRow][currentCol] == northEastArrow:
         return True
     elif B[currentRow][currentCol] == northWestArrow:
         return True
     elif B[currentRow][currentCol] == eastNorthArrow:
         return True
     elif B[currentRow][currentCol] == eastSouthArrow:
         return True
     elif B[currentRow][currentCol] == southEastArrow:
         return True
     elif B[currentRow][currentCol] == southWestArrow:
         return True
     elif B[currentRow][currentCol] == westNorthArrow:
         return True
     elif B[currentRow][currentCol] == westSouthArrow:
         return True
     else:
         return False


def searchPath(B, currentRow, currentColumn, previousDirection):
    if currentRow < 0 or currentRow >= len(B):
        return False
    if currentColumn < 0 or currentColumn >= len(B[0]):
        return False
    if B[currentRow][currentColumn] == "O":
        return False
    if isCellAlreadyVisited(B, currentRow, currentColumn) == True:
        return False
    if B[currentRow][currentColumn] == "D":
        return True

    #Search NORTH direction
    currentDirection = "north"
    arrow = getArrow(previousDirection, currentDirection)
    B[currentRow][currentColumn] = arrow
    flag = searchPath(B, currentRow-1, currentColumn, currentDirection)
    if not(flag):
        #Search EAST direction
        currentDirection = "east"
        arrow = getArrow(previousDirection, currentDirection)
        B[currentRow][currentColumn] = arrow
        flag = searchPath(B, currentRow, currentColumn+1, currentDirection)
    if not(flag):
        #Search SOUTH direction
        currentDirection = "south"
        arrow = getArrow(previousDirection, currentDirection)
        B[currentRow][currentColumn] = arrow
        flag = searchPath(B,currentRow+1, currentColumn, currentDirection)
    if not(flag):
        #Search WEST direction
        currentDirection = "west"
        arrow = getArrow(previousDirection, currentDirection)
        B[currentRow][currentColumn] = arrow
        flag = searchPath(B, currentRow, currentColumn-1, currentDirection)
    if not(flag):
        B[currentRow][currentColumn] = "V"
    #Finally return flag
    return flag
def numberOfSteps(a):
     count=0
     for i in range(len(a)):
          for j in range(len(a)):
               if a[i][j]==northArrow or a[i][j]==southArrow or a[i][j]==eastArrow or a[i][j]==westArrow or a[i][j]==northEastArrow or a[i][j]==northWestArrow or a[i][j]==eastNorthArrow or a[i][j]==eastSouthArrow or a[i][j]==southEastArrow or a[i][j]==southWestArrow or a[i][j]==westNorthArrow or a[i][j]==westSouthArrow:
                    count=count+1
     return count+1


n = readBoardSize()
B = createBoard(n)
markStartAndDestinationCells(B)
printBoard(B)
flag = searchPath(B, 0, 0, "north") ##We will start searching north direction
markStartAndDestinationCells(B) ##After searching re-mark the start and destination
printBoard(B)
x=numberOfSteps(B)

if flag:
    print("Path was found successfully and is shown in arrows.")
    print("The path found has",x,"steps") 
else:
    print("Sorry, no path exists from start cell to destination cell")
