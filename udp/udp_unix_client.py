# unix_socket исползуется в рамках одного компьютера
import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
sock.sendto(b'Test message', 'unix.sock')
