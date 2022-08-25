# Based on: https://www.youtube.com/watch?v=nsLTQj-l_18
# Game Board with 2D Array / Processing + Python (Win11)

DEBUG = True

def DebugPrint(message):
    if DEBUG:
        print(message)

# Create Grid and assign the value 1 to all elements
grid = [ [1]*8 for n in range(8)]
DebugPrint(grid)

# Assign the value -1 to the first and last elements
grid[0][0] = -1
grid[7][7] = -1

# Define the number of pixels for each grid
w = 70
DebugPrint("Cell Height/Width: " + str(w))

# Define the size of the window
def setup():
    size(800,600)

def draw():
    # Define variables used for determining the top-left corner of each cell
    x,y = 0,0 
 
    # Looping mechanism to display the grid
    for row in grid:
        for col in row:
            if col == -1:
                fill(255,0,0)
            else:
                fill(255)
            rect(x,y,w,w) # Parameters: first two are upper left corner, width, height
            x += w # Increment the value of x by the width of the cell
        y += w # Increment the value of y by the width of the cell
        x = 0 # Reset the value of x after drawing each row
        
def mousePressed():
    grid[mouseY/w][mouseX/w] = -1 * grid[mouseY/w][mouseX/w]
    DebugPrint("Cell Selected: (" + str(mouseY/w) + "," + str(mouseX/w) + ")\tValue: " + str(grid[mouseY/w][mouseX/w]))

    
        
            
