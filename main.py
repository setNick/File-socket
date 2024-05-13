import socket

# Получить имя сокета от пользователя
socket_name = input("Введите имя сокета: ")

# Создать файловый сокет
try:
  socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
except socket.error as e:
  print(f"Ошибка создания сокета: {e}")
  exit(1)

# Подключиться к серверу
try:
  socket.connect(("localhost", 8000))
except socket.error as e:
  print(f"Ошибка подключения к серверу: {e}")
  exit(1)

# Отправить имя сокета серверу
socket.send(socket_name.encode())

# Закрыть сокет
socket.close()

print("Имя сокета отправлено на сервер.")
