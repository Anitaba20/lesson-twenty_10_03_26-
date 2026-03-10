import socket
import time

host = 'localhost'
port = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    while True:
        time.sleep(1)
        sprava = input("Zadaj spravu na server: ")
        s.send(sprava.encode())