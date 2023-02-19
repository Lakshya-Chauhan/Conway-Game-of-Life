import pygame
from os import system

stopped = False
frameRate = 600
size = 15

BG    = (10,10,10)
BLUE  = (131, 193, 224)
PEACH = (224, 196, 148)
GREEN = (146, 219, 148)
RED   = (235, 147, 147)
BLACK = (0,0,0)

def neighbours_count(old_gen: list, x: int, y: int):
    """Counts the neighbouring cells of the cell whose indices in the generation are given in the argument."""

    if x == len(old_gen)-1 and y == len(old_gen[x])-1:
        neighbours = old_gen[0][y] + old_gen[0][0] + old_gen[0][y-1] + old_gen[x-1][y-1] + old_gen[x-1][y] + old_gen[x-1][0] + old_gen[x][0] + old_gen[x][y-1]
    elif x == len(old_gen)-1:
        neighbours = old_gen[0][y] + old_gen[0][y+1] + old_gen[0][y-1] + old_gen[x-1][y-1] + old_gen[x-1][y] + old_gen[x-1][y+1] + old_gen[x][y+1] + old_gen[x][y-1]
    elif y == len(old_gen[x])-1:
        neighbours = old_gen[x+1][y] + old_gen[x+1][0] + old_gen[x+1][y-1] + old_gen[x-1][y-1] + old_gen[x-1][y] + old_gen[x-1][0] + old_gen[x][0] + old_gen[x][y-1]
    else:
        neighbours = old_gen[x+1][y] + old_gen[x+1][y+1] + old_gen[x+1][y-1] + old_gen[x-1][y-1] + old_gen[x-1][y] + old_gen[x-1][y+1] + old_gen[x][y+1] + old_gen[x][y-1]

    return neighbours

def check_next_state(cell: int, neighbours: int):
    """Checks whether a given cell will live for the next generation or not."""

    if cell: # cell is alive
        if (neighbours < 2) or (neighbours > 3): # cell is undercrowded or overcrowded
            return 0
        else:
            return 1
    else: # cell is dead
        if (neighbours == 3): # suitable cells for reproduction
            return 1
        else:
            return 0

def next_gen(old_gen: list):
    """Creates a new generation of cells, from the old generation given as an argument."""
    new_gen = []
    neighbours = 0

    for x in range(len(old_gen)):
        new_gen.append([])
        for y in range((len(old_gen[x]))):
            neighbours = neighbours_count(old_gen, x, y)
            new_gen[x].append(check_next_state(old_gen[x][y], neighbours))

    return new_gen

def construct_gen(rows,column):
    """Construct an empty generation i.e. a generation of only dead cells."""

    gen = []
    for i in range(rows):
        gen.append([])
        for j in range(column):
            gen[i].append(0)
    return gen

def cls():
    system("cls")

def main():
    global stopped
    global frameRate

    pygame.init()
    screen = pygame.display.set_mode((1080,720))
    pygame.display.set_caption("Game Of Life")
    cls()

    Gen1 = construct_gen(108,72)
    Gen2 = next_gen(Gen1)
    Gen3 = next_gen(Gen2)
    running = True
    clock = pygame.time.Clock()

    screen.fill(BG)

    while running:
        clock.tick(frameRate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    stopped = not(stopped)

            if pygame.mouse.get_pressed()[0]: # left mouse click
                mpos = pygame.mouse.get_pos()
                pos = (mpos[0]//size, mpos[1]//size)

                Gen1[pos[0]][pos[1]] = 1 if not(Gen1[pos[0]][pos[1]]) else 1    # turn dead cell live on left click
                frameRate = 600

            elif pygame.mouse.get_pressed()[2]: # right mouse click
                mpos = pygame.mouse.get_pos()
                pos = (mpos[0]//size, mpos[1]//size)

                Gen1[pos[0]][pos[1]] = 0 if Gen1[pos[0]][pos[1]] else 0         # turn live cell dead on right click
                frameRate = 600

            else:
                frameRate = 30

        for x in range(len(Gen1)):
            for y in range(len(Gen1[x])):
                if Gen1[x][y]:
                    if Gen2[x][y]:
                        if Gen3[x][y]:  # cell survives for next 3 generations
                            colour = BLUE 
                        else:           # cell survives for next 2 generations 
                            colour = PEACH

                    elif Gen3[x][y]: # cell survives 1st generation, then dies, and takes birth in the 3rd generation
                        colour = GREEN
                    else: # cell surives only 1st generation
                        colour = RED
                else: # cell is dead
                    colour = BLACK

                pygame.draw.rect(screen, colour, pygame.Rect(x * size, y * size, size - 1, size - 1))

        if stopped:
            if next_gen(Gen1) != Gen2:
                Gen1 = next_gen(Gen1)
                Gen2 = next_gen(Gen1)
                Gen3 = next_gen(Gen2)
            else:
                Gen1 = Gen2
                Gen2 = Gen3
                Gen3 = next_gen(Gen3)

        pygame.display.update()

        
        
if __name__ == "__main__":
    main()
