import socket
import threading
import os
from dotenv import load_dotenv
from crypto_utils import RC4Cipher

load_dotenv()

cipher = RC4Cipher(os.getenv("secret"))
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((os.getenv("host"), int(os.getenv("port"))))

def receive_loop():
    while True:
        data = client.recv(4096)
        if not data:
            print("Server disconnected.")
            break
        print(f"\r[Server] {cipher.decrypt(data)}\n[You] ", end="", flush=True)

def send_loop():
    while True:
        msg = input("[You] ")
        client.sendall(cipher.encrypt(msg))

t_recv = threading.Thread(target=receive_loop, daemon=True)
t_recv.start()

try:
    send_loop()
finally:
    client.close()
