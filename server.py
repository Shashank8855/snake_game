import socket
import pickle
import threading

# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5555))
server.listen()

# Player information
players = {}
player_id = 0

# Handle client connections
def handle_client(conn, addr):
    global player_id
    conn.send(str.encode(str(player_id)))
    players[player_id] = {'id': player_id, 'x': 0, 'y': 0}
    player_id += 1

    while True:
        try:
            data = conn.recv(4096)
            player = pickle.loads(data)
            players[player['id']] = player
            conn.sendall(pickle.dumps(players))
        except:
            break

    print(f"Disconnected: {addr}")
    del players[player['id']]
    conn.close()

# Accept connections
print("Server started, waiting for connections...")
while True:
    conn, addr = server.accept()
    print(f"Connected to: {addr}")

    # Start a new thread to handle the client
    threading.Thread(target=handle_client, args=(conn, addr)).start()
