# Pathfinder

## Project Description:
This project was experimenting with maze solving techniques using python in addition to the pygame library. 

The strategy used consists of the following steps:
1. Starting at the first endpoint tile, record the distance each tile is from the beginning (creates a heatmap shown by the gradient)
    * Avoid any blocks
    * Only go on tiles that have not been recorded
2. Start at endpoint and check for the lowest tile surrounding it
3. Make this the new endpoint
4. Repeat from step 2 until the start is reached


## Requirements:
1. Python 3
    * Installed on PATH if running from command prompt
3. Pygame 2
    * Find out more about pygame:<br>[www.pygame.org](https://www.pygame.org/)


## Run the Program:
1. From the command line, locate the project folder
2. Run the following command: <code>python grid.py</code>


## Controls/Shortcuts
<kbd>r</kbd> Restart

<kbd>t</kbd> Toggle Action (Endpoint or Block)
