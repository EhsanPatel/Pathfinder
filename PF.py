'''
Ehsan Patel
Pathfinding Program
June 21st 2020
'''

'''
make a grid of 0,0,0 to give each tile three characteristics
0. Is the tile a block or a path
1. What step is the tile from the source
return to start by using the lowest number on the surrounding tiles
'''



def main():
    #  prompts for input
    startx = int(input("X1: "))
    starty = int(input("Y1: "))
    endx = int(input("X2: "))
    endy = int(input("Y2: "))

    # example blocklist (will be overwritten)
    blockList = [[1,1],[3,4],[3,5],[5,4],[6,4],[4,4],[8,7],[7,7],[2,8]]
    
    newGrid = createGrid(18, 9, startx, endx, starty, endy, blockList)
    for i in range(9):
        print(newGrid[i])
    print(getNumSteps(newGrid))



def createGrid(w, h, x1, x2, y1, y2, blocks):
    printable = False
    
    WIDTH = w
    HEIGHT = h
    
    grid = [[[0,0,0] for col in range(WIDTH)] for row in range(HEIGHT)]
    
    #input a start and finish
    startx = x1
    starty = y1
    endx = x2
    endy = y2
    
    #create the start block
    grid[starty - 1][startx - 1][1] = 1
    
    #create a blockage for the path to go around - will change to use the first 0 in the pair of 0,0
    for i in range(len(blocks)):
        grid[(blocks[i][1])][(blocks[i][0])][0] = 1  
    
    #prints the grid if allowed
    if printable:
        #prints the original grid
        print()
        for i in range(HEIGHT):
            print(WIDTH)
        
    #found loop runs until the program is over
    found = False
    
    #the step counter keeps track of how many tiles you have traversed
    step = 1
    
    #runs through the steps until the end block is found
    while not found:
        
        #loops through the y of the grid
        for i in range(HEIGHT):
            #loops through the x of the grid
            for j in range(WIDTH):
                #counts the number of times a block is in contact with a block closer to the source
                count = 0
                
                #loops through the y around a tile
                for k in range(-1,2):
                    #loops through the x around a tile
                    for l in range(-1,2):
                        #if the tile is within the grid and not the tile being checked
                        if (0 <= i+k < len(grid)) and (0 <= j+l < len(grid[0])) and not (k == 0 and l==0):
                            #if the tile makes contact with a closer to the source block
                            if grid[i+k][j+l][1] == step:
                                #add to the number of contacts
                                count = count + 1
                #if a block is making contact and it is not a closer to source block
                if count >= 1 and grid[i][j][1] == 0 and grid[i][j][0] == 0:
                    #mark the block for the next iteration
                    grid[i][j][1] = step + 1
        
        
        if printable:        
            #print out a white space
            print()
            #print a copy of the current grid by row
            for i in range(len(grid)):
                print(grid[i])
        #increase the step for the next iteration
        step = step + 1
        
        #breaks the loop after 18 steps have been made
        if step >= 162:
            found = True
    return grid



def getNumSteps(grid, w, h):
    WIDTH = w
    HEIGHT = h
    return max([grid[i][j][1] for i in range(HEIGHT)]for j in range(WIDTH))[0]




    
if __name__ == "__main__":
    main()
