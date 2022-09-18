import numpy as np

file = open("1.in", "r")
lines = file.readlines()
game = []
for element in range(0, len(lines)-1):
    game.append(lines[element].strip("\n").split(" "))


direction = lines[-1]
LEFT, UP, RIGHT, DOWN = 0, 1, 2, 3

### FUNCTIONS ###
def isLateral(direction):
    return True if direction % 0 == 0 else False

def canAdd(row):
    canAdd = True
    # Check for duplicates. No duplicates == no addition
    for number in row:
        if number != 0 and row.count(number) > 1:
            canAdd = False
            return canAdd
    
    



    return True

def addRow(row, direction):
    newRow = []
    return newRow

def addCol(col, direction):
    newCol = []
    return newCol

def execLateral(game):
    newGame = []
    for row in game:
        if canAdd(row):
            newRow = addRow()
        else:
            newRow = list.copy(row)
        newGame.append(newRow)
    return newGame


if isLateral(direction):
    newGame = execLateral(game)
else:
    npGame = np.array(game)
    npGame = npGame.transpose()
    newGame = execLateral(npGame)

print(newGame)