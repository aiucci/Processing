# Aidan's Project with graphics
# Based on: https://www.youtube.com/watch?v=nsLTQj-l_18
# Game Board with 2D Array / Processing + Python

# Define game variables
intRange = 10                 # The number of rows and columns. CHANGE THIS VALUE TO ALTER THE GAME SIZE

Continue = True
countU = 0                    # Count results of random direction Up
countD = 0                    # Count results of random direction Down
countL = 0                    # Count results of random direction Left
countR = 0                    # Count results of random direction Right
currentIndicator = -3         # The value used to mark the location of a grid location that has been visited
DEBUG = True                  # Set to true to enable DebugPrint statements
endIndicator = -2             # The value used to mark the ending location
intSize = 800                 # The size of the play area
lowerLimit = 0                # The lower limit (Always Zero)
moveCounter = 1               # The number of moves played
startIndicator = -1           # The value used to mark the starting location
upperLimit = intRange - 1     # The upper limit (Always one less than the range (which is zero based)
w = intSize / (10 + intRange) # Define the number of pixels for each grid

# Create Grid and assign the value 1 to all elements
grid = [ [1]*intRange for n in range(intRange)]

# Generate and assign random starting and ending coordinates
startX=int(random(intRange))
startY=int(random(intRange))
grid[startX][startY] = startIndicator
endX=int(random(intRange))
endY=int(random(intRange))
grid[endX][endY] = endIndicator

# Initialize current and previous coordinates
currentX = startX
currentY = startY
previousX=0
previousY=0

# Define the size of the window
def setup():
    size(intSize,intSize)

def DebugPrint(message):
    if DEBUG:
        print(message)

def gen_random_direction():
    global countU
    global countD
    global countL
    global countR
    direction = "" # Up(U), Down(D), Left(L), Right(R)
    
    randomNumber = int(random(0,4))
    
    if randomNumber == 0:
        direction = "U"
        countU += 1
    elif randomNumber == 1:
        direction = "D"
        countD += 1
    elif randomNumber == 2:
        direction = "L"
        countL += 1
    elif randomNumber == 3:
        direction = "R"
        countR += 1
    #DebugPrint("Random Number: " + str(randomNumber) + " : Direction: " + direction)
    #delay(100)
    return direction

def play_game():
    global Continue
    global currentX
    global currentY
    global grid
    global moveCounter
    global previousX
    global previousY

    #Generate a random direction to move. Valid directions: Up(U), Down(D), Left(L), Right(R)
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

    if moveCounter == 1: # Execute this if statement once at the begining of the game
        DebugPrint("Move|Direction|Current Coordinates")
        DebugPrint("[" + str(moveCounter).zfill(4) + "] " + directionGenerated.upper() + " (" + str(currentX) + "," + str(currentY) + ")")
        grid[currentX][currentY] = currentIndicator
        moveCounter += 1
        previousX = currentX
        previousY = currentY
    else:
        if grid[currentX][currentY] == endIndicator: # Execute this once at the conclusion of the game
            grid[previousX][previousY] = 1
            #moveCounter += 1
            grid[startX][startY] = startIndicator # Restore the starting location
            grid[currentX][currentY] = -3
            DebugPrint("[" + str(moveCounter).zfill(4) + "] " + directionGenerated.upper() + " (" + str(currentX) + "," + str(currentY) + ")")
            print("\nThe game is over. Moves required: " + str(moveCounter))
            print("The starting coordinates are: (" + str(startX) + "," + str(startY) + ")" )
            print("The ending coordinates are: (" + str(endX) + "," + str(endY) + ")" )
            print("The current coordinates are: (" + str(currentX) + "," + str(currentY) + ")" )
            DebugPrint("Results of RandomDirectionGenerator (U,D,L,R): " + str(countU) + "," + str(countD) + "," + str(countL) + "," + str(countR) + ")")
            Continue = False
            return Continue
        else: # Execute this else statement for all moves except for the first and last
            grid[previousX][previousY] = 1
            grid[currentX][currentY] = currentIndicator
            grid[startX][startY] = startIndicator # Restore the starting location
            DebugPrint("[" + str(moveCounter).zfill(4) + "] " + directionGenerated.upper() + " (" + str(currentX) + "," + str(currentY) + ")")
            moveCounter += 1
            previousX = currentX
            previousY = currentY

def draw():
    # Define variables used for determining the top-left corner of each cell
    x,y = 0,0
    ContinuePlaying = play_game()
            
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
    
    if ContinuePlaying == False:
        noLoop()    
    
        
   
