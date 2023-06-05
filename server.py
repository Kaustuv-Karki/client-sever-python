import socket
import threading


HEADER = 64
PORT = 8000
SERVER = socket.gethostbyname(socket.gethostname())  # Gives the local IP address 192.168.1.69
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handleClient(conn, addr):
    print(f"New connection {addr} connected to the server")
    
    connected = True
    while True:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print(f"Server is running on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = handleClient, args = (conn, addr))
        thread.start()
        print(f"[Active Connections : {threading.active_count() - 1} ]")

print("The server is starting...")
start()