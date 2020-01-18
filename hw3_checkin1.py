'''
15-110 Homework 3 Check-in 1
Name: Clara Ye
Andrew ID: zixuany
'''

from tkinter import *

################################################################################

''' #1 - Smiley Face - 20pts
In a 400px x 400px Tkinter canvas window, draw the smiley face shown in the
write-up. Your canvas does not need to be a pixel-perfect match for ours, but 
should contain all the relevant components in approximately the right location 
and size.

Hint: to make the eyes, consider using text instead of lines...
'''

def drawSmileyFace(canvas):
    canvas.create_oval(25,25,375,375, fill = "yellow", width = 10)
    canvas.create_line(125,275,275,275, width = 15)
    canvas.create_text(100,90, text = "X", font = "Arial 70 bold", anchor = "nw")
    canvas.create_text(300,90, text = "X", font = "Arial 70 bold", anchor = "ne")
    pass


''' #2 - Checkerboard - 25pts
In a 400px x 400px Tkinter window, draw a checkerboard with checkers in the 
starting positions. A checkerboard alternates light and dark spaces in an 
8x8 grid. Pieces are placed on the dark spaces, with pieces of one color in the 
top three rows and pieces of a different color in the bottom three rows.

Examples of checkerboards and checkers can be found here, and in the write-up: 
https://en.wikipedia.org/wiki/Draughts

To get full credit, you can't have more than 10 create_rectangle or create_oval
calls. You must use loops instead!
'''

def drawCheckerboard(canvas):
    size = 50
    for v in range(0,8,2):
        for h in range(0,8,2):
            left = size * h
            top = size * v
            right = size + size * h
            bottom = size + size * v
            canvas.create_rectangle(left,top,right,bottom, fill = "ivory", width = 0)
    for v in range(1,8,2):
        for h in range(1,8,2):
            left = size * h
            top = size * v
            right = size + size * h
            bottom = size + size * v
            canvas.create_rectangle(left,top,right,bottom, fill = "ivory", width = 0)
    for v in range(1,8,2):
        for h in range(0,8,2):
            left = size * h
            top = size * v
            right = size + size * h
            bottom = size + size * v
            canvas.create_rectangle(left,top,right,bottom, fill = "gray10", width = 0)
    for v in range(0,8,2):
        for h in range(1,8,2):
            left = size * h
            top = size * v
            right = size + size * h
            bottom = size + size * v
            canvas.create_rectangle(left,top,right,bottom, fill = "gray10", width = 0)
    for v in range(0,3,2):
        for h in range(1,8,2):
            left = size * h
            top = size * v
            right = size + size * h
            bottom = size + size * v
            canvas.create_oval(left,top,right,bottom, fill = "khaki", width = 0)
    for v in range(1,2,2):
        for h in range(0,8,2):
            left = size * h
            top = size * v
            right = size + size * h
            bottom = size + size * v
            canvas.create_oval(left,top,right,bottom, fill = "khaki", width = 0)
    for v in range(5,8,2):
        for h in range(0,8,2):
            left = size * h
            top = size * v
            right = size + size * h
            bottom = size + size * v
            canvas.create_oval(left,top,right,bottom, fill = "wheat", width = 0)
    for v in range(6,8,2):
        for h in range(1,8,2):
            left = size * h
            top = size * v
            right = size + size * h
            bottom = size + size * v
            canvas.create_oval(left,top,right,bottom, fill = "wheat", width = 0)
    pass


################################################################################

''' To check your work, click 'Run File as Script' to run the test function
shown below. '''

def runSmileyFace():
    print("Testing drawSmileyFace(): check the outputted canvas!")
    root = Tk() # makes a window
    canvas = Canvas(root, width=400, height=400) # makes a canvas
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack() # packs the canvas in the window
    drawSmileyFace(canvas)
    root.mainloop() # tells the window to stay open until we close it

def runCheckerboard():
    print("Testing drawCheckerboard(): check the outputted canvas!")
    root = Tk() # makes a window
    canvas = Canvas(root, width=400, height=400) # makes a canvas
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack() # packs the canvas in the window
    drawCheckerboard(canvas)
    root.mainloop() # tells the window to stay open until we close it

def testAll():
    runSmileyFace()
    runCheckerboard()

testAll()