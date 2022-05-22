# Based on: https://www.youtube.com/watch?v=nsLTQj-l_18
# Game Board with 2D Array / Processing + Python

DEBUG = True

def DebugPrint(message):
    if DEBUG:
        print(message)

def gen_random_direction():
  direction = "" # Up(U), Down(D), Left(L), Right(R)
  randomNumber = int(random(0,4))
  if randomNumber == 0:
    direction = "U"
  elif randomNumber == 1:
    direction = "D"
  elif randomNumber == 2:
    direction = "L"
  elif randomNumber == 3:
    direction = "R"
  #DebugPrint("Random Number: " + str(randomNumber) + " : Direction: " + direction)
  delay(100)
  return direction

# Create Grid and assign the value 1 to all elements
grid = [ [1]*8 for n in range(8)]

# Generate and assign random starting and ending coordinates
startX=int(random(8))
startY=int(random(8))
endX=int(random(8))
endY=int(random(8))
grid[startX][startY] = -1
grid[endX][endY] = -2

# Define variables
upperLimit = 7
lowerLimit = 0
moveCounter = 1
currentX = startX
currentY = startY
previousX=0
previousY=0
w = 70 # Define the number of pixels for each grid

# Define the size of the window
def setup():
    size(800,600)

def draw():
    global currentX
    global currentY
    global moveCounter
    global previousX
    global previousY
    
    # Define variables used for determining the top-left corner of each cell
    x,y = 0,0 
 
    # Display the grid
    for row in grid:
        for col in row:
            if col == -1:
                fill(0,255,0) # Green: Start Coordinates
            elif col == -2:
                fill(255,0,0) # Red: Stop Coordinates
            elif col == -3:
                    fill(0,0,255) # Blue: Current Coordinates
            else:
                fill(255)
            rect(x,y,w,w) # Parameters: first two are upper left corner, width, height
            x += w # Increment the value of x by the width of the cell
        y += w # Increment the value of y by the width of the cell
        x = 0 # Reset the value of x after drawing each row

    # Generate a random direction to move. Valid directions: Up(U), Down(D), Left(L), Right(R)
    directionGenerated = gen_random_direction()
    
    # Apply random direction to current coordinates
    if directionGenerated == "U": 
        if (currentY + 1) <= upperLimit:
            currentY += 1
        else:
            currentY -= 1
    elif directionGenerated == "D": 
        if (currentY - 1) >= lowerLimit:
            currentY -= 1
        else:
            currentY += 1
    elif directionGenerated == "L": 
        if (currentX - 1) >= lowerLimit:
            currentX -= 1
        else:
            currentX += 1
    elif directionGenerated == "R":
        if (currentX + 1) <= upperLimit:
            currentX += 1
        else:
            currentX -= 1

    if moveCounter == 1:
        DebugPrint("Move|Direction|Current Coordinates")
        DebugPrint("[" + str(moveCounter).zfill(4) + "] " + directionGenerated.upper() + " (" + str(currentX) + "," + str(currentY) + ")")
        grid[currentX][currentY] = -3
        moveCounter += 1
        previousX = currentX
        previousY = currentY
    else:
        if grid[currentX][currentY] == -2:
            grid[currentX][currentY] = -3
            moveCounter += 1
            DebugPrint("[" + str(moveCounter).zfill(4) + "] " + directionGenerated.upper() + " (" + str(currentX) + "," + str(currentY) + ")")
            print("The starting coordinates are: (" + str(startX) + "," + str(startY) + ")" )
            print("The ending coordinates are: (" + str(endX) + "," + str(endY) + ")" )
            print("The current coordinates are: (" + str(currentX) + "," + str(currentY) + ")" )
            print("The game is over. Moves required: " + str(moveCounter))
            delay(5000)
            exit()
        else:
            grid[previousX][previousY] = 1
            grid[currentX][currentY] = -3
            DebugPrint("[" + str(moveCounter).zfill(4) + "] " + directionGenerated.upper() + " (" + str(currentX) + "," + str(currentY) + ")")
            moveCounter += 1
            previousX = currentX
            previousY = currentY
