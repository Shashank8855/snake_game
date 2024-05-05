import pygame
import sys

pygame.init()

width, height = 400, 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Clicker")

counter = 0
font = pygame.font.Font(None, 36)

while True:
    window.fill((0, 0, 0))
    text = font.render(f"Clicks: {counter}", True, (255, 255, 255))
    window.blit(text, (10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                counter += 1

    pygame.display.update()
pygame.quit()