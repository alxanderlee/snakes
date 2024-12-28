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

# Pygame initialization
pygame.init()
pygame.display.set_caption('Snakes')
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()

# Snake Initialization
snake_head = [30, 480]
snake_body = [[0, 480], [10, 480], [20, 480], [30, 480]]

# Fruit
random_fruit = [10* random.randint(1, 72), 10* random.randint(1, 32)]
fruit_spawn = True

direction = "RIGHT"
change_to = direction


while True:
    pygame.display.update()
    break