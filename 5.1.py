import socket 


s = socket.socket()
print("[+] Berjaya buat soket yeay!")


port = 8888

s.bind(('',port))
print("[+] Berjaya bind soket pada port: "+ str(port))


s.listen(5)
print("[+] Soket sedang menunggu klien...")


while True:

	c, addr = s.accept()
	print("[SUCCESS] Dapat capaian dari: "+ str(addr))

	c.send(b'Terima Kasih!')
	buffer = c.recv(1024)
	print(buffer)

c.close()
