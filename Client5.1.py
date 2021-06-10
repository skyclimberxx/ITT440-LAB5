import socket


s = socket.socket()


port = 8888


s.connect(('192.168.114.6',port))


data = s.recv(1024)


s.send(b'[+]Hi Server, Saya klien dari Afrika Laut. Thanks x!');


print(data)


s.close()
