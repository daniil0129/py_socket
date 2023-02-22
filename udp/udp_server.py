import socket

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0', 8888))
    result = sock.recv(1024)
except Exception as e:
    sock.close()
else:
    print('Message', result.decode('utf-8'))



