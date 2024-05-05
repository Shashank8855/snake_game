import pygame
import sys
import random

pygame.init()

width, height = 400, 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

snake_size = 20
snake = [(width // 2, height // 2)]
food = (random.randint(0, width // snake_size - 1) * snake_size,
        random.randint(0, height // snake_size - 1) * snake_size)
direction = (0, -1)  # Initial direction: up

clock = pygame.time.Clock()

while True:
    window.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and direction != (1, 0):
        direction = (-1, 0)
    elif keys[pygame.K_RIGHT] and direction != (-1, 0):
        direction = (1, 0)
    elif keys[pygame.K_UP] and direction != (0, 1):
        direction = (0, -1)
    elif keys[pygame.K_DOWN] and direction != (0, -1):
        direction = (0, 1)

    # Move the snake
    head = (snake[0][0] + direction[0] * snake_size,
            snake[0][1] + direction[1] * snake_size)
    snake.insert(0, head)
    
    # Check for collision with food
    if head == food:
        food = (random.randint(0, width // snake_size - 1) * snake_size,
                random.randint(0, height // snake_size - 1) * snake_size)
    else:
        snake.pop()

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(window, (255, 255, 255), (segment[0], segment[1], snake_size, snake_size))
    
    # Draw the food
    pygame.draw.rect(window, (255, 0, 0), (food[0], food[1], snake_size, snake_size))

    pygame.display.update()
    clock.tick(10)  # Snake speed
pygame.quit()