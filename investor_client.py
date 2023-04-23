import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bank_host = socket.gethostname()
bank_port = 5050

print("I want to make a bank account")
inp = '0'
s.sendto(inp.encode(), (bank_host, bank_port))

data, addr = s.recvfrom(1024)
data = data.decode('utf-8')
print("Bank: ", data)
name = input()
print("Me: ", name)
s.sendto(name.encode(), (bank_host, bank_port))

while True:
    print("1. Deposit money")
    print("2. Withdraw money")
    print("3. Check bank balance")

    inp = input("Enter the number from the above options")
    if inp == '1':
        s.sendto(inp.encode(), (bank_host, bank_port))
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Bank: ", data)
        amount = input()
        print("Me: ", amount)
        s.sendto(name.encode(), addr)
        s.sendto(amount.encode(), addr)

    if inp == '2':
        s.sendto(inp.encode(), (bank_host, bank_port))
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Bank: ", data)
        amount = input()
        print("Me: ", amount)
        s.sendto(name.encode(), addr)
        s.sendto(amount.encode(), addr)

    if inp == '3':
        s.sendto(inp.encode(), (bank_host, bank_port))
        s.sendto(name.encode(), (bank_host, bank_port))
        amount, addr = s.recvfrom(1024)
        print('Bank: ', amount.decode('utf-8'))
