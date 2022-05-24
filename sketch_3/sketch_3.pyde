# Knights Tour
# Game Board with 2D Array / Processing + Python

DEBUG = True
LowerRange = 0
MoveCounter = 1
UpperRange = 8

def DebugPrint(message):
    if DEBUG:
        print(message)

# Create Grid and assign the value 1 to all elements
grid = [[0]*UpperRange for n in range(UpperRange)]
DebugPrint(grid)

# Define the number of pixels for each grid
w = 70

# Define the size of the window
def setup():
    size(800,600)

def draw():
    # Define variables used for determining the top-left corner of each cell
    x,y = 0,0 
 
    # Looping mechanism to display the grid
    for row in grid:
        for col in row:
            if col != 0:
                fill(0,255,0)
            elif col == -1:
                fill(255,0,0)
            else:
                fill(255)
            rect(x,y,w,w) # Parameters: first two are upper left corner, width, height
            x += w # Increment the value of x by the width of the cell
        y += w # Increment the value of y by the width of the cell
        x = 0 # Reset the value of x after drawing each row
        
def mousePressed():
    global MoveCounter
    if MoveCounter == 1:
        grid[mouseY/w][mouseX/w] = MoveCounter
        DebugPrint("\n{" + str(MoveCounter) + "] Cell Selected: (" + str(mouseY/w) + "," + str(mouseX/w) + ")\tValue Set: " + str(grid[mouseY/w][mouseX/w]))
        MoveCounter += 1
        DebugPrint(grid)
        DebugPrint("MoveCounter: " + str(MoveCounter))
    
        # Move Type 1 > Up Two, Left 1
        if (mouseY/w) >= 2:
            DebugPrint("Type1_Y: True")
        if (mouseY/w) <= 5:
            DebugPrint("Type3_Y: True")
        if (mouseX/w) >= 2:
            DebugPrint("Type2_X: True")
        if (mouseX/w) <= 5:
            DebugPrint("Type4_X: True")
    
        
            
