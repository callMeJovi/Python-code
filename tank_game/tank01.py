# pip install pygame==2.3.0
# call terminal
# pip install virtualenvwrapper-win
# mkvirtualenv name of virtual env
import pygame

# initiating pygame
pygame.init()
# create a window
pygame.display.set_mode((800, 600))
# rename the window
pygame.display.set_caption("Tank Game by JingleTech")
# show window
while True:
    pygame.display.update()
