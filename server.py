import socket
import threading

HEADER=64                    #defining the size of the first message to the sever
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER, PORT)
FORMAT='utf-8'
DICONNECT_MESSAGE="!DISCONNECT"

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr): 
    print(f"[NEW CONNECTION] {addr} connected")

    connected=True
    while connected:
        msg_length=conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length=int(msg_length)
            msg=conn.recv(msg_length).decode(FORMAT)
            if msg == DICONNECT_MESSAGE:
                connected=False 
                
            print(f"[{addr}] {msg}")

    conn.close()

def start():
    server.listen()
    print(F"[LISENING] Server is listening on {SERVER}")
    while True:
        conn, addr =server.accept()
        thread= threading.Thread(target=handle_client, args=(conn, addr))      #creating a new thread for the connection
        thread.start()
        print(f"[ACTIVE CONNECTIONS]{threading.activeCount()-1}")


print("[STARTING] sever is starting...")
start()
