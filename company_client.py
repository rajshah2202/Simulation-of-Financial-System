import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bank_host = socket.gethostname()
bank_port = 1024

print("I want to launch an IPO")


inp = '0'
s.sendto(inp.encode(), (bank_host, bank_port))

data, addr = s.recvfrom(1024)
data = data.decode('utf-8')
print("Market: ", data)
name = input()
print("Me: ", name)
s.sendto(name.encode(), (bank_host, bank_port))

data, addr = s.recvfrom(1024)
data = data.decode('utf-8')
print("Market: ", data)
name = input()
print("Me: ", name)
s.sendto(name.encode(), (bank_host, bank_port))

data, addr = s.recvfrom(1024)
data = data.decode('utf-8')
print("Market: ", data)
name = input()
print("Me: ", name)
s.sendto(name.encode(), (bank_host, bank_port))
