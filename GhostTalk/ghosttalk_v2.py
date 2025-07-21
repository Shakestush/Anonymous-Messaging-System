import socket
import threading
import random
import string
from cryptography.fernet import Fernet

HOST = '127.0.0.1'
NODE_PORTS = [5001, 5002, 5003]  # relay nodes
CHAT_PORT = 6000                 # chatroom server port

# Generate encryption keys for relay nodes
node_keys = {port: Fernet.generate_key() for port in NODE_PORTS}
ciphers = {port: Fernet(node_keys[port]) for port in NODE_PORTS}

# --- Relay Node ---
def relay_node(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, port))
    s.listen(5)
    print(f"[Node {port}] Running...")
    while True:
        conn, _ = s.accept()
        data = conn.recv(4096)
        conn.close()
        try:
            msg = ciphers[port].decrypt(data)
        except:
            continue
        # Pick next hop or final server
        if random.random() > 0.3:  # 70% chance to go to another node
            next_port = random.choice([p for p in NODE_PORTS if p != port])
            forward(next_port, msg)
        else:
            forward(CHAT_PORT, msg)

def forward(port, message):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, port))
    s.sendall(message)
    s.close()

# --- Chatroom Server ---
clients = []

def chatroom_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, CHAT_PORT))
    s.listen(5)
    print("[Chatroom] Server running...")
    while True:
        conn, addr = s.accept()
        clients.append(conn)
        threading.Thread(target=handle_client, args=(conn,), daemon=True).start()

def handle_client(conn):
    while True:
        try:
            data = conn.recv(4096)
            if not data:
                break
            broadcast(data, conn)
        except:
            break
    conn.close()
    clients.remove(conn)

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.sendall(message)
            except:
                pass

# --- User Client ---
def random_nickname():
    return ''.join(random.choices(string.ascii_lowercase, k=5))

def user_client():
    nickname = random_nickname()
    threading.Thread(target=receive_messages, daemon=True).start()
    print(f"[You are {nickname}]\nType your messages:")
    while True:
        msg = input()
        if msg.strip() == "":
            continue
        full_msg = f"{nickname}: {msg}"
        send_via_onion(full_msg)

def receive_messages():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, CHAT_PORT))
    while True:
        try:
            data = s.recv(4096)
            if data:
                print("\n" + data.decode() + "\n> ", end="")
        except:
            break

def send_via_onion(message):
    path = random.sample(NODE_PORTS, k=3)  # 3 random hops
    payload = message.encode()
    for port in reversed(path):
        payload = ciphers[port].encrypt(payload)
    forward(path[0], payload)

# --- Entry Point ---
if __name__ == "__main__":
    mode = input("Mode? (node/chat/server): ").strip().lower()
    if mode == "node":
        port = int(input(f"Enter port {NODE_PORTS}: "))
        relay_node(port)
    elif mode == "server":
        chatroom_server()
    elif mode == "chat":
        user_client()
    else:
        print("Invalid mode.")
