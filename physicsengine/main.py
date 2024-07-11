import sys
import pygame
import numpy as np


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

g = 9.81 
m = 1
t = 0
dt = 0.01

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()