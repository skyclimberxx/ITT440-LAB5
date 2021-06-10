import socket
import os
import time 

# create socket
s = socket.socket()
print("[+] Berjaya buat soket yeay!")


port = 8880

#bind socket
s.bind(('',port))
print("[+] Berjaya bind soket pada port: "+ str(port))

#listen client
s.listen(5)
print("[+] Soket sedang menunggu klien...")

#accept client
client, addr = s.accept()

#file received detail
file_name = s.recv(100).decode()
file_size = s.recv(100).decode()

#open n write file
with open(file_name,"wb") as file:

	c = 0

	#start time capture
	start_time = time.time()

	#loop for receive all the file
	while c <= int(file_size):
		data = client.recv(1024)
		if not (data):
			break
		file.write(data)
		c = c + len(data)

	#end time capture
	end_time = time.time()

print("[SUCCESS] File transfer is complete! Estimate time: ",end_time - start_time)

#close socket
c.close()
