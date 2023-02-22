import os
import socket

unix_sock_name = 'unix.sock'
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

if os.path.exists(unix_sock_name):
    os.remove(unix_sock_name)

sock.bind(unix_sock_name)

while True:
    try:
        res = sock.recvfrom(1024)
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        print('message', res.decode('utf-8'))
