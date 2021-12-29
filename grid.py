'''
Ehsan Patel
June 21st 2020

The grid program merges the grid created by the PF (Path Finder)
This program is a visual representation of what the P program does
By recieving input from the window, the information is sent to the grid creator
The visual program then retrieves the created grid to display
'''

import pygame
import PF

#Initializes the window
pygame.init()
width,height = 1260,630
size = (width,height)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pathfinder Grid")


# grid size
gridX = 18
gridY = 9

# scales the grid tiles to the screen size
gridXScale = width/gridX
gridYScale = height/gridY

#DEFAULT COLOURS
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

#Enabling Gridlines instead of just the cool gradient - keep off unless counting
gridLines = False
#State of the program, starts rerieving input until it is ready to display
state = "INPUT"
#Counts the mouse clicks to determine what block is being set
clickCount = 0
#Positions of the start and end points on the grid
startx = 0
starty = 0
endx = 0
endy = 0

#A list of all the blocking tiles
#blockList = [[1,1],[4,3],[5,3],[4,5],[4,6],[4,4],[7,8],[7,7],[8,2],[12,8],[17,8]]
blockList = []

currentBacking = [endx - 1,endy - 1]
#stores the points that were travelled over to return to start
backedPoints = []

#toggles between walls and endpoints
blockToggle = True

#Pygame display loop
done = False
while not done:
    #Retrieves the events from the window
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            if event.key == pygame.K_r:
                state = "INPUT"
                clickCount = 0
                startx = 0
                starty = 0
                endx = 0
                endy = 0
                blockList = []
                backedPoints = []

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_t:
                blockToggle = not blockToggle

        #Exit button of window
        if event.type == pygame.QUIT:
            done = True
        #Mouse click event (when button lifted)
        if event.type == pygame.MOUSEBUTTONUP:
            #Assigns the mouse coordinated
            x,y = pygame.mouse.get_pos()
            
            if event.button == 1:
                if blockToggle:
                    #Adds to the number of mouse clicks
                    clickCount = clickCount + 1
                    if clickCount == 1:
                        #Assigns the x and y values of the start point
                        #Must convert from pixels to grid points (pixel/block dimmension) + 1
                        startx = int(x/gridXScale) + 1
                        starty = int(y/gridYScale) + 1
                else:
                    blockList.append([int(x/gridXScale),int(y/gridYScale)])

            elif event.button == 3:
                if not blockToggle:
                    blockList.append([int(x/gridXScale),int(y/gridYScale)])
                else:
                    #Adds to the number of mouse clicks
                    clickCount = clickCount + 1
                    if clickCount == 1:
                        #Assigns the x and y values of the start point
                        #Must convert from pixels to grid points (pixel/block dimmension) + 1
                        startx = int(x/gridXScale) + 1
                        starty = int(y/gridYScale) + 1

    
    #Fills the screen black
    screen.fill(BLACK)
    
    #Loops through the grid x then y
    for a in range(gridX):
        for b in range(gridY):
            #Program receives input from the user on the window
            if state == "INPUT":
                #Draws the grid tiles everywhere
                pygame.draw.rect(screen, WHITE, [int(a*gridXScale), int(b*gridYScale), int(gridXScale), int(gridYScale)],1)
                for i in range(len(blockList)):
                    pygame.draw.rect(screen, BLUE, [int(blockList[i][0]*gridXScale), int(blockList[i][1]*gridYScale), int(gridXScale), int(gridYScale)])
                    
                #When the first click occurs, displays the start point
                if clickCount == 1:

                    #Draws a square over the clicked tile to signify start
                    pygame.draw.rect(screen, GREEN, [int((startx - 1)*gridXScale), int((starty - 1)*gridYScale), int(gridXScale), int(gridYScale)])
                #The second click is the end point
                if clickCount == 2:
                    #Assigns the x and y values of the end point
                    endx = int(x/gridXScale) + 1
                    endy = int(y/gridYScale) + 1
                    currentBacking = [endx - 1,endy - 1]

                    #Passes the coordinates and grid size into the PF grid making program
                    newGrid = PF.createGrid(gridX,gridY, startx, endx, starty, endy, blockList)
                    #Changes the state to display
                    state = "SHOWGRID"
            #When the program has recieved all of its input, it can now display the visual
            if state == "SHOWGRID":

                #If the grid has a block in the location on the grid
                if newGrid[b][a][0] == 1:
                    #Fill with a solid blue block
                    color = BLUE
                    fill = 0
                #If the grid has any other tile that does not block the path
                else:
                    #Fill with a gradient that gets lighter as it moves away from the source
                    color = (0,(min(255, newGrid[b][a][1]*(255/PF.getNumSteps(newGrid, gridX, gridY)))),min(255, newGrid[b][a][1]*(255/PF.getNumSteps(newGrid, gridX, gridY))))
                    #print(color)
                    fill = 0
                #Draws the tile depending on what type of grid item it is
                pygame.draw.rect(screen, color, [int(a*gridXScale), int(b*gridYScale), int(gridXScale), int(gridYScale)],fill)
                #Draws the grid lines if selected
                if gridLines:
                    pygame.draw.rect(screen, WHITE, [int(a*gridXScale), int(b*gridYScale), int(gridXScale), int(gridYScale)],1)
                    

                for i in range(len(backedPoints)):
                    pygame.draw.rect(screen, WHITE, [int(backedPoints[i][0]*gridXScale), int(backedPoints[i][1]*gridYScale), int(gridXScale), int(gridYScale)],2)
                
                #Draws an outline over the start and end points on the visual grid
                pygame.draw.rect(screen, GREEN, [int((startx - 1)*gridXScale), int((starty - 1)*gridYScale), int(gridXScale), int(gridYScale)], 2)
                pygame.draw.rect(screen, RED, [int((endx - 1)*gridXScale), int((endy - 1)*gridYScale), int(gridXScale), int(gridYScale)], 2)

                if a == gridX - 1 and b == gridY - 1:
                    state = "BACKTRACK"
                    v = 0
            if state == "BACKTRACK":
                if v == 0:
                    v = 1

                tempList1 = []
                tempList2 = []
                if newGrid[starty - 1][startx - 1][2] == 0:
                    for y in range(-1,2):
                        for x in range(-1,2):
                            if x == 0 or y == 0:
                                xv = currentBacking[0] + x
                                yv = currentBacking[1] + y
                                if xv >= 0 and xv < gridX and yv >= 0 and yv < gridY:
                                    if newGrid[yv][xv][0] != 1:
                                        tempList1.append([xv,yv])
                                        tempList2.append(newGrid[yv][xv][1])

                    for y in range(-1,2):
                        for x in range(-1,2):
                            if x != 0 or y != 0:
                                xv = currentBacking[0] + x
                                yv = currentBacking[1] + y
                                if xv >= 0 and xv < gridX and yv >= 0 and yv < gridY:
                                    if newGrid[yv][xv][0] != 1:
                                        tempList1.append([xv,yv])
                                        tempList2.append(newGrid[yv][xv][1])

                    backedPoints.append(tempList1[tempList2.index(min(tempList2))])
                    currentBacking[0] = backedPoints[len(backedPoints) - 1][0]
                    currentBacking[1] = backedPoints[len(backedPoints) - 1][1]
                    # backedPoints.append([xv,yv])
                    state = "SHOWGRID"

    pygame.display.flip()
pygame.quit()