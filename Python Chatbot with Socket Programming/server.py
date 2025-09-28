import socket
import json

# JSON dosyasını yükleme
with open("responses.json", "r", encoding="utf-8") as f:
    responses = json.load(f)

HOST = "127.0.0.1"
PORT = 5001

# TCP soketi oluşturma
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Server {PORT} portunda dinleniyor...")

conn, addr = server_socket.accept()
print(f"{addr} bağlandı.")

while True:
    data = conn.recv(1024).decode("utf-8")
    if not data:
        break

    print(f"İstemciden gelen: {data}")

    # JSON üzerinden cevap bulma
    response = responses.get(data.lower(), "Üzgünüm, bu konuda yardımcı olamıyorum.")

    conn.sendall(response.encode("utf-8"))

conn.close()
server_socket.close()