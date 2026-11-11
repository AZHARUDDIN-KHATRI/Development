print("Distributed Network Server Started...")
print("Waiting for clients...")

while True:
    conn, address = server.accept()

    print("Connected by:", address)

    while True:
        data = conn.recv(1024)

        if not data:
            break

        message = data.decode()
        print("Client:", message)

        response = "Server received: " + message
        conn.send(response.encode())

    conn.close()