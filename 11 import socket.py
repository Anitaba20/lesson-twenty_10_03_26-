import socket

host = 'localhost'
port = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    print(f"Server počúva na {host}:{port}")

    conn, addr = s.accept()
    with conn:
        print(f"Pripojený klient: {addr}")
        while True:
            data = conn.recv(1024)
            print("Klient poslal spravu: {}".format(data.decode()))