import pygame
import socket
import pickle

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multiplayer Game")

# Connect to server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(('localhost', 5555))
player_id = int(server.recv(4096).decode())

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        # Send player data to server
        server.sendall(pickle.dumps({'id': player_id, 'x': -1, 'y': 0}))
    elif keys[pygame.K_RIGHT]:
        server.sendall(pickle.dumps({'id': player_id, 'x': 1, 'y': 0}))
    elif keys[pygame.K_UP]:
        server.sendall(pickle.dumps({'id': player_id, 'x': 0, 'y': -1}))
    elif keys[pygame.K_DOWN]:
        server.sendall(pickle.dumps({'id': player_id, 'x': 0, 'y': 1}))

    # Receive updated player positions from server
    players = pickle.loads(server.recv(4096))
    for player in players.values():
        pygame.draw.rect(win, (255, 0, 0), (player['x'], player['y'], 10, 10))

    pygame.display.update()

pygame.quit()
