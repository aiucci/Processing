# Knights Tour
# Game Board with 2D Array / Processing + Python

DEBUG = True                                          # Set to True to print debug messages
LowerRange = 0                                        # The lower range
MoveCounter = 1                                       # Counts the number of valid moves
UpperRange = 12                                       # The size of grid is 8 x 8, but is surrounded by a guard zone of two cells on each side (which makes the grid 12x12
w = 50                                                # Define the number of pixels for each grid
grid = [[-1]*UpperRange for n in range(UpperRange)]   # Create Grid and assign the value -1 to all elements

def DebugPrint(message):
    if DEBUG:
        print(message)
        
def setup():
    global grid
    size(800,600) # Define the size of the window
    initializeGrid()
    DebugPrint(grid)

def initializeGrid():
    global grid
    
    for col in range(0,UpperRange):
        for row in range(0,UpperRange):
            if row in range(2,10) and  col in range(2,10):
                    grid[row][col] = 0

def mousePressed():
    Evaluate(mouseY/w,mouseX/w)

def markPotentialMoves(y,x):
    
    # Set any values that were previously set to -2 (indicating a permissable move based on the previous coordinates) to 0 (indicating that the value is in the initial state)
    for col in range(0,UpperRange):
        for row in range(0,UpperRange):
            if row in range(2,10) and  col in range(2,10):
                    if grid[row][col] == -2:
                        grid[row][col] = 0
    
    # Use the current values of the mouse coordinates to determine and mark the permissable moves
    if grid[y - 2][x - 1] == 0: # Move Type 1 (Up Two, Left 1)
        grid[y - 2][x - 1] =-2
    if grid[y - 2][x + 1] == 0: # Move Type 2 (Up Two, Right 1)
        grid[y - 2][x + 1] =-2
    if grid[y - 1][x + 2] == 0: # Move Type 3 (Right Two, Up 1)
        grid[y - 1][x + 2] =-2
    if grid[y + 1][x + 2] == 0: # Move Type 4 (Right Two, Down 1)
        grid[y + 1][x + 2] =-2
    if grid[y + 2][x + 1] == 0: # Move Type 5 (Down Two, Right 1)
        grid[y + 2][x + 1] =-2
    if grid[y + 2][x - 1] == 0: # Move Type 6 (Down Two, Left 1)
        grid[y + 2][x - 1] =-2
    if grid[y + 1][x - 2] == 0: # Move Type 7 (Left Two, Down 1)
        grid[y + 1][x - 2] =-2
    if grid[y - 1][x - 2] == 0: # Move Type 8 (Left Two, Up 1)
        grid[y - 1][x - 2] =-2    
        
def Evaluate(Y,X):   
    
    global MoveCounter
    
    DebugPrint("Coordinates: (" + str(Y) + "," + str(X) + ")")
    
    if MoveCounter == 1:
        if grid[Y][X] == 0:
            grid[Y][X] = MoveCounter
            DebugPrint("\n[" + str(MoveCounter) + "] Cell Selected: (" + str(Y) + "," + str(X) + ")\tValue Set: " + str(grid[Y][X]))
            MoveCounter += 1
            DebugPrint(grid)
            markPotentialMoves(Y,X)
    else:  
        if grid[Y][X] == -2:
            grid[Y][X] = MoveCounter
            DebugPrint("\n[" + str(MoveCounter) + "] Cell Selected: (" + str(Y) + "," + str(X) + ")\tValue Set: " + str(grid[Y][X]))
            MoveCounter += 1
            DebugPrint(grid)
            markPotentialMoves(Y,X)
        else:
            print("\nThe selected cell is not valid. Please select another cell")

def draw():
    # Define variables used for determining the top-left corner of each cell
    x,y = 0,0 
 
    # Looping mechanism to display the grid
    for row in grid:
        for col in row:
            if col > 0:         # Cells with a value greater than zero are green
                fill(0,255,0)
            elif col == -1:     # Cells with a value = to -1 are border cells
                fill(153)
            elif col == -2:     # Cells with a value = to -2 are potential moves
                fill(255,255,0)
            else:
                fill(255)
            rect(x,y,w,w) # Parameters: first two are upper left corner, width, height
            x += w # Increment the value of x by the width of the cell
        y += w # Increment the value of y by the width of the cell
        x = 0 # Reset the value of x after drawing each row
        

        
    

    
        
            
