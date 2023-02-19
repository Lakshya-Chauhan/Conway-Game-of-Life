import pygame
import random
from os import system
from msvcrt import getch
stopped = -1
frameRate = 600
def next_gen(old_gen):
    new_gen = []
    neighbours = 0
    for x in range(len(old_gen)):
        new_gen.append([])
        for y in range((len(old_gen[x]))):
            if x == len(old_gen)-1 and y == len(old_gen[x])-1:
                neighbours = old_gen[0][y] + old_gen[0][0] + old_gen[0][y-1] + old_gen[x-1][y-1] + old_gen[x-1][y] + old_gen[x-1][0] + old_gen[x][0] + old_gen[x][y-1]
            elif x == len(old_gen)-1:
                neighbours = old_gen[0][y] + old_gen[0][y+1] + old_gen[0][y-1] + old_gen[x-1][y-1] + old_gen[x-1][y] + old_gen[x-1][y+1] + old_gen[x][y+1] + old_gen[x][y-1]
            elif y == len(old_gen[x])-1:
                neighbours = old_gen[x+1][y] + old_gen[x+1][0] + old_gen[x+1][y-1] + old_gen[x-1][y-1] + old_gen[x-1][y] + old_gen[x-1][0] + old_gen[x][0] + old_gen[x][y-1]
            else:
                neighbours = old_gen[x+1][y] + old_gen[x+1][y+1] + old_gen[x+1][y-1] + old_gen[x-1][y-1] + old_gen[x-1][y] + old_gen[x-1][y+1] + old_gen[x][y+1] + old_gen[x][y-1]
            if neighbours < 2:
                new_gen[x].append(0)
                continue
            elif (neighbours in [2,3]) and (old_gen[x][y] == 1):
                new_gen[x].append(1)
                continue
            elif (neighbours > 3) and (old_gen[x][y] == 1):
                new_gen[x].append(0)
                continue
            elif (neighbours == 3) and (old_gen[x][y] == 0):
                new_gen[x].append(1)
                continue
            else:
                new_gen[x].append(0)
                continue
    return new_gen


def construct_gen(rows,column):
    gen = []
    for i in range(rows):
        gen.append([])
        for j in range(column):
            gen[i].append(0)
            # gen[i].append(round(random.choice([0,0,0,0,0,0,0,0,0,0,0,0,1])))
    return gen

def cls():
    system("cls")
pygame.init()
screen = pygame.display.set_mode((1920,1080))
#icon = pygame.image.load('')
pygame.display.set_caption("")
#pygame.display.set_icon(icon)
cls()

Gen = construct_gen(1920//15,1080//15)
Gen2 = next_gen(Gen)
Gen3 = next_gen(Gen2)
running = True
clock = pygame.time.Clock()
while running == True:
    clock.tick(frameRate)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                stopped *= -1
        if pygame.mouse.get_pressed()[0] == True:
            mpos = pygame.mouse.get_pos()
            mpos = (mpos[0]//15,mpos[1]//15)
            Gen[mpos[0]][mpos[1]] = 1
            frameRate = 600
        elif pygame.mouse.get_pressed()[2] == True:
            mpos = pygame.mouse.get_pos()
            mpos = (mpos[0]//15,mpos[1]//15)
            Gen[mpos[0]][mpos[1]] = 0
            frameRate = 600
        else:
            frameRate = 20
    #Code Here
    screen.fill((0,0,0))
    for x in range(len(Gen)):
        for y in range(len(Gen[x])):
            if Gen[x][y] == 1:
                if Gen2[x][y] == 1:
                    if Gen3[x][y] == 1:
                        colour = (131,193,224)
                    else:
                        colour = (224,196,148)
                elif Gen3[x][y] == 1:
                    colour = (146,219,136)
                else:
                    colour = (235,147,147)

                pygame.draw.rect(screen, colour, pygame.Rect(x*15,y*15,15,15))
            pygame.draw.rect(screen, (15,15,15),pygame.Rect(x*15,y*15,15,15),1)
    if stopped == 1:
        if next_gen(Gen) != Gen2:
            Gen = next_gen(Gen)
            Gen2 = next_gen(Gen)
            Gen3 = next_gen(Gen2)
        else:
            Gen = Gen2
            Gen2 = Gen3
            Gen3 = next_gen(Gen3)
    pygame.display.update()
