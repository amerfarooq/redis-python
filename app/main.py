import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    client_socket, client_addr = server_socket.accept()

    with client_socket:
      print(f"Connected by {client_addr}")
      client_msg = client_socket.recv(1024)
      client_socket.sendall("+PONG\r\n".encode())


if __name__ == "__main__":
    main()
