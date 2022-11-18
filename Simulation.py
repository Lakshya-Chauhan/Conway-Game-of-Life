import pygame
import random
from os import system
from msvcrt import getch
def next_gen(old_gen):
    new_gen = []
    neighbours = 0
    for x in range(len(old_gen)):
        new_gen.append([])
        for y in range((len(old_gen[x]))):
            if x == len(old_gen)-1 and y == len(old_gen)-1:
                neighbours = old_gen[0][y] + old_gen[0][0] + old_gen[0][y-1] + old_gen[x-1][y-1] + old_gen[x-1][y] + old_gen[x-1][0] + old_gen[x][0] + old_gen[x][y-1]
            elif x == len(old_gen)-1:
                neighbours = old_gen[0][y] + old_gen[0][y+1] + old_gen[0][y-1] + old_gen[x-1][y-1] + old_gen[x-1][y] + old_gen[x-1][y+1] + old_gen[x][y+1] + old_gen[x][y-1]
            elif y == len(old_gen)-1:
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
            gen[i].append(round(random.random()))
    return gen

def cls():
    system("cls")
pygame.init()
screen = pygame.display.set_mode((800,800))
#icon = pygame.image.load('')
pygame.display.set_caption("")
#pygame.display.set_icon(icon)
cls()

Gen = construct_gen(80,80)
running = True
clock = pygame.time.Clock()
while running == True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Code Here
    screen.fill((0,0,0))
    for x in range(len(Gen)):
        for y in range(len(Gen)):
            if Gen[x][y] == 1:
                pygame.draw.rect(screen,(255,255,255),pygame.Rect(x*10,y*10,10,10))
    Gen = next_gen(Gen)
    pygame.display.update()