# Import Libraries
import pygame
import time
import random

# Global Variables
window_x = 720
window_y = 480
black = pygame.Color(0, 0, 0)
green = pygame.Color(0, 255, 50)
red = pygame.Color(255, 0, 0)
orange = pygame.Color(255, 165, 0)
turquoise = pygame.Color(48, 213, 200)
Snake_speed = 10


pygame.init()
pygame.display.set_caption('Snakes')
game_window = pygame.display.set_mode((window_x, window_y))

while True:
    pygame.display.update()