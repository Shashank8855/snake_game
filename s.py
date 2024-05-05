import pygame
from pygame.locals import *
import random

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 20
BLOCK_SIZE = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLOCK_TYPES = [BLACK, (100, 100, 100), (150, 75, 0), (0, 0, 255), (0, 255, 0)]

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Minecraft")

# Player attributes
player_x, player_y = WIDTH // 2, HEIGHT // 2
player_speed = 5

# Block attributes
blocks = []
for _ in range(50):  # Generate some random blocks
    blocks.append((random.randint(0, WIDTH - BLOCK_SIZE), random.randint(0, HEIGHT - BLOCK_SIZE), random.choice(BLOCK_TYPES)))

# Game loop
running = True
while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_UP:
                player_y -= player_speed
            elif event.key == K_DOWN:
                player_y += player_speed
            elif event.key == K_LEFT:
                player_x -= player_speed
            elif event.key == K_RIGHT:
                player_x += player_speed
            elif event.key == K_SPACE:
                blocks.append((player_x, player_y, BLACK))
    
    # Draw blocks
    for block in blocks:
        pygame.draw.rect(screen, block[2], (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))
    
    # Draw player
    pygame.draw.rect(screen, BLACK, (player_x, player_y, PLAYER_SIZE, PLAYER_SIZE))
    
    pygame.display.flip()

pygame.quit()
