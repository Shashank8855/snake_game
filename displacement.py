import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
SPEED = 5

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Displacement Calculator")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Object properties
object_size = 20
object_color = RED
object_position = [100, 100]
object_initial_position = object_position.copy()
object_final_position = object_position.copy()

# Font for displaying text
font = pygame.font.SysFont(None, 30)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle user input for movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        object_position[0] -= SPEED
    if keys[pygame.K_RIGHT]:
        object_position[0] += SPEED
    if keys[pygame.K_UP]:
        object_position[1] -= SPEED
    if keys[pygame.K_DOWN]:
        object_position[1] += SPEED

    # Calculate displacement
    displacement = math.sqrt((object_position[0] - object_initial_position[0])**2 + (object_position[1] - object_initial_position[1])**2)
    displacement_text = f"Displacement: {displacement:.2f}"

    # Clear the screen
    screen.fill(WHITE)

    # Draw the object
    pygame.draw.circle(screen, object_color, object_position, object_size)

    # Render and display the displacement text
    text_surface = font.render(displacement_text, True, BLACK)
    screen.blit(text_surface, (10, 10))

    # Update the final position
    object_final_position = object_position.copy()

    # Update the screen
    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
