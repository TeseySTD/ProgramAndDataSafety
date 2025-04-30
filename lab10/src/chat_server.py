import socket
import threading
import os
from dotenv import load_dotenv

from crypto_utils import RC4Cipher

load_dotenv()

cipher = RC4Cipher(os.getenv("secret"))
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((os.getenv("host"), int(os.getenv("port"))))
server.listen(1)
print("Server is waiting for connection...")

conn, addr = server.accept()
print(f"Connected to {addr}")

def receive_loop():
    while True:
        data = conn.recv(4096)
        if not data:
            print("Client disconnected.")
            break
        print(f"\r[Client] {cipher.decrypt(data)}\n[You] ", end="", flush=True)

def send_loop():
    while True:
        msg = input("[You] ")
        conn.sendall(cipher.encrypt(msg))

t_recv = threading.Thread(target=receive_loop, daemon=True)
t_recv.start()

try:
    send_loop()
finally:
    conn.close()
    server.close()
