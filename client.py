import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((HOST, PORT))
    print("Connected to Server!")

    message = input("Enter message: ")
    client.send(message.encode())

    response = client.recv(1024).decode()
    print("Server Response:", response)

except ConnectionRefusedError:
    print("Server is not running!")

finally:
    client.close()
