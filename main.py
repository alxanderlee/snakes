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
fps = pygame.time.Clock()

# defining the snake
snake_position = [100, 50]
snake_body = [[100, 50],[90, 50],[80, 50],[70, 50]]
fruit_position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True
direction = 'RIGHT'
change_to = direction

def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/4)    
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()    
    time.sleep(2)
    pygame.quit()    
    quit()

# Task 1: Create a function that displays the score.
# Utilize pygame.font.SysFont(), score_font.render(), score_surface.get_rect(), and game_window.blit() as in game_over()
def show_score(choice, color, font, size):
    return

# Main Function
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Task 2: According to the change_to variable, adjust the new snake's position. Up: y - 10; Down: y + 10; Left: x - 10; Right: x + 10
    # ___________ # Position Code Here

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_position))

    # Task 3: Create an if-else statement that will first check if the snake_position equals the fruit position. If so, increment score by 10 and set fruit_spawn to false.
    # If false, remove the last value of the snake list.
    # ______________ # Code Here

    # Task 4: If fruit spawn is false, spawn a new fruit and set fruit_spawn to true
    if not fruit_spawn:
        # ___________ # Code here

    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(
          pos[0], pos[1], 10, 10))
        
    pygame.draw.rect(game_window, turquoise, pygame.Rect(
      fruit_position[0], fruit_position[1], 10, 10))

    # Task 5: Create 3 game-over conditions
    # ______________ # Code Here


    show_score(1, turquoise, 'times new roman', 20)    
    pygame.display.update()
    fps.tick(snake_speed)
    
