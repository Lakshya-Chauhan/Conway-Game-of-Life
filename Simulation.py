import pygame
from os import system

stopped = 0

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

    pygame.init()
    screen = pygame.display.set_mode((1080,720))
    pygame.display.set_caption("Game Of Life")
    cls()

    Gen1 = construct_gen(108,72)
    Gen2 = next_gen(Gen1)
    Gen3 = next_gen(Gen2)
    running = True
    clock = pygame.time.Clock()

    while running:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    stopped = not(stopped)

            if pygame.mouse.get_pressed()[0]:
                mpos = pygame.mouse.get_pos()
                pos = (mpos[0]//10,mpos[1]//10)

                if Gen1[pos[0]][pos[1]] == 0:
                    Gen1[pos[0]][pos[1]] = 1

        screen.fill(BLACK)
        for x in range(len(Gen1)):
            for y in range(len(Gen1[x])):
                if Gen1[x][y]:
                    if Gen2[x][y]:
                        if Gen3[x][y]:
                            colour = BLUE 

                        else:
                            colour = PEACH

                    elif Gen3[x][y]:
                        colour = GREEN

                    else:
                        colour = RED

                    pygame.draw.rect(screen, colour, pygame.Rect(x*10,y*10,10,10))

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