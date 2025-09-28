import socket

HOST = "127.0.0.1"  # server adresi
PORT = 5001

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print("Sohbete başlayabilirsin! (çıkmak için 'exit' yaz)")

while True:
    message = input("Sen: ")
    if message.lower() == "exit":
        break

    client_socket.sendall(message.encode("utf-8"))

    response = client_socket.recv(1024).decode("utf-8")
    print("Bot:", response)

client_socket.close()