import pygame
import sys

pygame.init()


running = True

while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.exit()
            sys.exit(0)
print("Hello world")
