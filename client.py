import socket
s=socket.socket()
s.connect(("locolhost",8001))
data=c.recv(1024)
print(data)
c.send("hi Priya".encode())
c.close()
