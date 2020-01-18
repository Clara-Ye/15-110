"""
15-110 Hw6 - Battleship Project
Name: Clara Ye
AndrewID: zixuany
"""

project = "Battleship" # don't edit this

#### SIMULATION FUNCTIONS ####

from tkinter import *
import random

''' We'll use these four global variables to code for specific cell states '''
EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4

''' The simulation functions will be updated at each stage. Check the writeup
for more details. '''

''' makeModel manages the initial variables stored in data. '''

def makeModel(data):
    data["rows"] = 10
    data["cols"] = 10
    data["board_size"] = 500
    data["cell_size"] = data["board_size"] // data["rows"]
    data["numShip"] = 5
    data["computer_board"] = emptyGrid(data["rows"], data["cols"])
    data["user_board"] = emptyGrid(data["rows"], data["cols"])
    data["computer_board"] = addShips(data["computer_board"], data["numShip"])
    data["showShips"] = False
    data["temporaryShip"] = []
    data["numShips"] = 0
    data["winner"] = None
    data["maxTurns"] = 50
    data["currentTurns"] = 0
    return data

''' makeView manages all graphics. Note that we have two canvases - one for the
computer, and one for the user. '''

def makeView(data, userCanvas, compCanvas):
    drawGrid(data, compCanvas, data["computer_board"], False)
    drawGrid(data, userCanvas, data["user_board"], True)
    drawShip(data, userCanvas, data["temporaryShip"])
    if data["winner"] == "user":
        print("")
        print("Congratulations! You have clicked all the ships!")
        print("You are the winner!")
        print("")
        print("Press Enter if you want to start a new game.")
    elif data["winner"] == "comp":
        print("")
        print("Sorry, the computer has clicked all your ships.")
        print("The winner is the computer.")
        print("")
        print("Press Enter if you want to start a new game.")
    elif data["winner"] == "draw":
        print("")
        print("Sorry, you are out of turns.")
        print("You have reached a draw.")
        print("")
        print("Press Enter if you want to start a new game.")
    return

''' keyPressed listens for keyboard events. '''

def keyPressed(data, event):
    if event.keysym == "Return":
        makeModel(data)
    pass

''' mousePressed listens for mouse events. Note that the parameter board will be
"user" is the click happened on the user's canvas, or "comp" if the click happened
on the computer's canvas. '''

def mousePressed(data, event, board):
    if data["winner"] == None:
        cell = getClickedCell(data, event)
        if board == "user":
            clickUserBoard(data, cell[0], cell[1])
        elif data["numShips"] < 5 and board == "comp":
            print("")
            print("Please place your ships before you click on the computer board!")
        else:
            runGameTurn(data, cell[0], cell[1])
    pass

#### CHECK-IN 1 ####

'''
Write a function emptyGrid(rows,cols) which creates a new 2D
list (called a grid) with rows number of rows and cols number of
columns. The value of each grid[row][col] should be 1, which stands for an
empty spot that has not been clicked. Return the new 2D list.
'''

def emptyGrid(rows,cols):
    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row += [1]
        grid.append(row)
    return grid

'''
Write a function createShip() which chooses a random row in the range [1,8] and 
random column in the same range to be the center point of a ship. We choose 1-8
so that it cannot put a ship in the last row or column, which wouldn't fit on the board. 

After choosing a row and column as the center, your code should choose a random 
number 0 or 1 to decide if the ship will be vertical or horizontal.
If it chose vertical, create a ship within the same column, where the
ends are one above and one below the chosen center - e.g., row-1, row,
row+1. Similarly, if it chose horizontal, create a ship in the same
row, where the ends are one column left and right of center - e.g., col-1, col, col+1.

Each ship will be a list of 3 coordinates (two-elementlists). Return the 
ship (2D list) created.
'''

def createShip():
    center_r = random.randint(1,8)
    center_c = random.randint(1,8)
    direction = random.randint(0,1)
    if direction == 0:
        ship = [[center_r-1,center_c],[center_r,center_c],[center_r+1,center_c]]
    elif direction == 1:
        ship = [[center_r,center_c-1],[center_r,center_c],[center_r,center_c+1]]
    return ship

'''
Write a function checkShip(grid, ship) that iterates through the given ship and
checks if each coordinate in the ship is 'clear'. A coordinate is clear if the
corresponding location on the given grid is empty (EMPTY_UNCLICKED). It should 
return the list of not-clear coordinates, or the empty list if all coordinates are clear.
'''

def checkShip(grid, ship):
    not_clear = []
    for coordinate in ship:
        if grid[coordinate[0]][coordinate[1]] != 1:
            not_clear += [coordinate]
    return not_clear

'''
Write a function addShips(grid, numShips) which loops until it has added numShips 
ships to the grid. For each time through the loop, it should create a ship using 
createShip(), then checkShip for that ship on the given grid. If the returned 
not-clear list is empty, then the ship can be placed. 

To place the ship, iterate through each coordinate of the ship, and set the grid 
at that coordinate to 2 (SHIP_UNCLICKED), then add 1 to the current count of ships. 
The function should return the grid that was modified to add numShips ships.
'''

def addShips(grid, numShips):
    num = 0
    while num < numShips:
        ship = createShip()
        if checkShip(grid,ship) == []:
            grid[ship[0][0]][ship[0][1]] = 2
            grid[ship[1][0]][ship[1][1]] = 2
            grid[ship[2][0]][ship[2][1]] = 2
            num += 1
    return grid

'''
Now we just need to add graphics. Write drawGrid, which draws a grid of rows x cols 
squares on the given canvas. Each square should have the cell size you determined 
in the previous step. If the cell in the given grid at a coordinate is SHIP_UNCLICKED, 
the square should be filled yellow; otherwise, it should be filled blue.

Hint: you did something very similar to this in Hw3 Check-in 1...
'''

def drawGrid(data, canvas, grid, showShips):
    for r in range(data["rows"]):
        for c in range(data["cols"]):
            if grid[r][c] == 1:
                canvas.create_rectangle(data["cell_size"]*r, data["cell_size"]*c,
                                        data["cell_size"]*(r+1), data["cell_size"]*(c+1),
                                        fill = "blue")
            elif grid[r][c] == 2:
                if showShips == True:
                    canvas.create_rectangle(data["cell_size"]*r, data["cell_size"]*c,
                                            data["cell_size"]*(r+1), data["cell_size"]*(c+1),
                                            fill = "yellow")
                else:
                    canvas.create_rectangle(data["cell_size"]*r, data["cell_size"]*c,
                                            data["cell_size"]*(r+1), data["cell_size"]*(c+1),
                                            fill = "blue")
            elif grid[r][c] == 3:
                canvas.create_rectangle(data["cell_size"]*r, data["cell_size"]*c,
                                        data["cell_size"]*(r+1), data["cell_size"]*(c+1),
                                        fill = "white")
            elif grid[r][c] == 4:
                canvas.create_rectangle(data["cell_size"]*r, data["cell_size"]*c,
                                        data["cell_size"]*(r+1), data["cell_size"]*(c+1),
                                        fill = "red")
    pass


#### WEEK 1 TESTS ####

def testEmptyGrid():
    print("Testing emptyGrid()...", end="")
    assert(emptyGrid(5, 5) == [ [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1] ])
    assert(emptyGrid(4, 6) == [ [1,1,1,1,1,1], [1,1,1,1,1,1], [1,1,1,1,1,1], [1,1,1,1,1,1] ])
    assert(emptyGrid(0, 0) == [ ])
    
    # Make sure that the grid doesn't have any aliasing problems!
    g = emptyGrid(3, 3)
    g[0][1] = "foo"
    assert(g[1][1] != "foo")
    print("... done!")

def testCreateShip():
    print("Testing createShip()...", end="")
    ship = createShip()
    assert(type(ship) == list)
    assert(len(ship) == 3)
    ship.sort()
    # All in same row/col
    assert((ship[0][0] == ship[1][0] == ship[2][0]) or \
        (ship[0][1] == ship[1][1] == ship[2][1]))
    # All connected
    assert((ship[0][0] + 1 == ship[1][0] == ship[2][0] - 1) or \
        (ship[0][1] + 1 == ship[1][1] == ship[2][1] - 1))
    print("... done!")
    
def testCheckShip():
    print("Testing checkShip()...", end="")
    grid = [ [1, 1, 2, 1], [1, 1, 2, 1], [1, 1, 2, 1], [2, 2, 2, 1] ]
    assert(checkShip(grid, [[0, 0], [1, 0], [2, 0]]) == [])
    assert(checkShip(grid, [[0, 2], [1, 2], [2, 2]]) == [[0, 2], [1, 2], [2, 2]])
    assert(checkShip(grid, [[1, 1], [2, 1], [3, 1]]) == [[3, 1]])
    print("... done!")

def testAddShips():
    print("Testing addShips()...", end="")
    grid = [ [1] * 10 for row in range(10) ]
    grid2 = addShips(grid, 2)
    print("Check whether two ships have been added to this grid:")
    for row in grid2:
        print(row)
    print("... done!")

def week1Tests():
    testEmptyGrid()
    testCreateShip()
    testCheckShip()
    testAddShips()

week1Tests()

#### CHECK-IN 2 ####

''' Write isVertical, which takes in a ship (recall from last week that a ship is 
a 2D list of coordinates) and returns True if the ship is placed vertically, or 
False otherwise. Recall that a ship is vertical if its coordinates all share the 
same column, and are each 1 row away from the next part.  '''

def isVertical(ship):
    ship = sorted(ship)
    if ship[0][1] != ship[1][1] or ship[0][1] != ship[2][1] or ship[1][1] != ship[2][1]:
        return False
    elif abs(ship[0][0] - ship[1][0]) != 1 or abs(ship[2][0] - ship[1][0]) != 1:
        return False
    return True

''' Then write isHorizontal, which takes in a ship and returns True if the ship 
is placed horizontally, and False otherwise. This should work in a similar manner 
to isVertical, except that the dimensions are flipped. '''

def isHorizontal(ship):
    ship = sorted(ship)
    if ship[0][0] != ship[1][0] or ship[0][0] != ship[2][0] or ship[1][0] != ship[2][0]:
        return False
    elif abs(ship[0][1] - ship[1][1]) != 1 or abs(ship[2][1] - ship[1][1]) != 1:
        return False
    return True

''' Write the function getClickedCell(data, event) which takes the simulation's 
data dictionary and a mouse event, and returns a two-element list holding the row 
and col of the cell that was clicked.

Recall that the event value holds event.x and event.y; you need to convert these 
to the row and col. How can you do this? You have two choices- either derive the 
row and col mathematically, or iterate over every possible row and col in the board, 
calculate each (row, col) cell's left, top, right, and bottom bounds, and check 
if the (x,y) coordinate falls within those. '''

def getClickedCell(data, event):
    row = event.x // data["cell_size"]
    col = event.y // data["cell_size"]
    return [row, col]

''' Implement the function clickUserBoard(data, row, col), which handles a click 
event on a specific cell. First, check if the clicked location is already in the 
temporary ship list; if it is, return early. This will keep the user from adding 
multiple cells in the same location. Assuming the clicked cell is not in the 
temporary ship, add it to the temporary ship value.

If the temporary ship contains three cells, we'll try to add it to the board, 
since all of our ships will be three units long. However, ships should only be 
added if they do not overlap any already-placed ships, and if they cover three 
connected cells (either vertically or horizontally). You can test this by calling 
checkShip(), isVertical, and isHorizontal().

If the temporary ship is legal, add it to the user's board by updating the board 
at each cell to hold the value 2 (SHIP_UNCLICKED). If it is illegal, print an 
error message to the interpreter and reset the temporary ship to be empty.

Finally, we need to keep track of how many ships the user has added so far. Add 
one more variable to data in makeModel, in order to track the number of user 
ships; it should start as 0. Then, in clickUserBoard(), add one to that variable 
if a ship is added. At the end of the function, check if the user has added 5 
ships, and tell them to start playing the game if so. And at the beginning of 
the function, exit immediately if 5 ships have already been added, to keep the 
user from adding too many ships. '''

def clickUserBoard(data, row, col):
    # check if there are already 5 ships on the board
    if data["numShips"] == 5:
        print("")
        print("There are already 5 ships on the board!")
        print("Stop adding more ships and we can start the game now!")
        print("Click on the computer board to reveal a cell.")
        return
    # if not, check if the cell is already in a temporary ship
    if [row, col] in data["temporaryShip"]:
        print("")
        print("You have already selected this cell.")
        print("Please select another cell")
        return 
    # if not, add it to temporary ship
    data["temporaryShip"].append([row, col])
    # check if there are 3 cells added
    if len(data["temporaryShip"]) == 3:
        # check if the temporary ship overlaps an existing ship
        if checkShip(data["user_board"], data["temporaryShip"]) != []:
            print("")
            print("The ship you just created overlaps an existing ship.")
            print("Please create another ship.")
            data["temporaryShip"] = []
            return
        # if not, check if the ship is legal
        if isHorizontal(data["temporaryShip"]) == False and isVertical(data["temporaryShip"]) == False:
            print("")
            print("This ship is illegal.")
            print("Please make sure the ship occupies 3 neighboring cells.")
            data["temporaryShip"] = []
            return
        # if it is, add ship to user board
        data["user_board"][data["temporaryShip"][0][0]][data["temporaryShip"][0][1]] = 2
        data["user_board"][data["temporaryShip"][1][0]][data["temporaryShip"][1][1]] = 2
        data["user_board"][data["temporaryShip"][2][0]][data["temporaryShip"][2][1]] = 2
        data["temporaryShip"] = []
        data["numShips"] += 1
        # if there are 5 ships already, tell the user to start the game
        if data["numShips"] == 5:
            print("")
            print("The ships are ready!")
            print("We can start the game now!")
            print("Click on the computer board to reveal a cell.")

''' Write drawShip(data, canvas, ship), which draws white cells for each 
component of the given ship. '''

def drawShip(data, canvas, ship):
    for cell in ship:
        r = cell[0]
        c = cell[1]
        canvas.create_rectangle(data["cell_size"]*r, data["cell_size"]*c,
                                data["cell_size"]*(r+1), data["cell_size"]*(c+1),
                                fill = "white")
    pass

#### WEEK 2 TESTS ####

def testIsVertical():
    print("Testing isVertical()...", end="")
    assert(isVertical([ [0, 1], [1, 1], [2, 1] ]) == True)
    assert(isVertical([ [2, 1], [0, 1], [1, 1] ]) == True) # order doesn't matter
    assert(isVertical([ [1, 0], [1, 1], [1, 2] ]) == False)
    assert(isVertical([ [0, 0], [0, 1], [0, 3] ]) == False) # must be sequential
    assert(isVertical([ [0, 1], [2, 3], [1, 0] ]) == False)
    print("... done!")

def testIsHorizontal():
    print("Testing isHorizontal()...", end="")
    assert(isHorizontal([ [1, 0], [1, 1], [1, 2] ]) == True)
    assert(isHorizontal([ [1, 2], [1, 0], [1, 1] ]) == True) # order doesn't matter
    assert(isHorizontal([ [0, 1], [1, 1], [2, 1] ]) == False)
    assert(isHorizontal([ [0, 0], [1, 0], [3, 0] ]) == False) # must be sequential
    assert(isHorizontal([ [1, 0], [3, 2], [0, 1] ]) == False)
    print("... done!")

def week2Tests():
    testIsVertical()
    testIsHorizontal()

week2Tests()

#### FULL ASSIGNMENT ####

''' This function will update the board when (row, col) is clicked, and will
detect game-over conditions. Instructions are in the write-up. '''
def updateBoard(data, board, row, col, player):
    if board[row][col] == 1:
        board[row][col] = 3
    elif board[row][col] == 2:
        board[row][col] = 4
    data["currentTurns"] += 1
    if data["currentTurns"] == data["maxTurns"]:
        data["winner"] = "draw"
    elif isGameOver(data, board):
        data["winner"] = player
    return board

''' This function will manage each turn of the game. Instructions are in the write-up. '''
def runGameTurn(data, row, col):
    if data["computer_board"][row][col] == 3 or data["computer_board"][row][col] == 4:
        print("This cell is already clicked!")
        return
    else:
        data["computer_board"] = updateBoard(data, data["computer_board"], row, col, "user")
        [row, col] = getComputerGuess(data)
        data["user_board"] = updateBoard(data, data["user_board"], row, col, "comp")

''' This function should return a cell that the computer will 'click' on the 
user's board. We'll have the computer select cells completely randomly; use the 
random.randint() function to pick the row and col. Finally, to make sure that the 
computer doesn't click the same cell twice, use a while loop to keep picking new 
(row, col) pairs until you find one that hasn't been clicked in the user board yet. '''
def getComputerGuess(data):
    row = random.randint(0,9)
    col = random.randint(0,9)
    while data["user_board"][row][col] == 3 or data["user_board"][row][col] == 4:
        row = random.randint(0,9)
        col = random.randint(0,9)
    return [row, col]

''' Write the function isGameOver(data, board), which checks whether the game 
is over for the given board. The game is done if there are no SHIP_UNCLICKED 
cells left in the board- in other words, when every ship has been clicked. 
Return True if the game is over for that board, and False otherwise. '''
def isGameOver(data, board):
    for row in range(data["rows"]):
        for col in range(data["cols"]):
            if board[row][col] == 2:
                return False
    return True

################### DO NOT MODIFY THE FOLLOWING CODE ###########################

# You do not need to be able to write the following functions;
# just modify the core simulation functions at the top of the file.

from tkinter import *

def updateView(data, userCanvas, compCanvas):    
    userCanvas.delete(ALL)    
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()    
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)
    
def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)
    
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    
    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()
    
    makeView(data, userCanvas, compCanvas)
    
    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))
    
    updateView(data, userCanvas, compCanvas)
    
    root.mainloop()
    
runSimulation(500, 500)