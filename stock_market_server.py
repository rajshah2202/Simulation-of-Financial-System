import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = socket.gethostname()
port = 1024

s.bind((host, port))

while True:
    input_file = open('../data/market.json')
    f = input_file.read()
    bank = json.loads(f)

    data, addr = s.recvfrom(1024)
    data = data.decode('utf-8')

    if data == '0':
        data = "What is the name of the company?"
        s.sendto(data.encode(), addr)
        name, addr = s.recvfrom(1024)
        name = name.decode('utf-8')

        data = "How many shares?"
        s.sendto(data.encode(), addr)
        quantity, addr = s.recvfrom(1024)
        quantity = quantity.decode('utf-8')

        data = "At what base price?"
        s.sendto(data.encode(), addr)
        base, addr = s.recvfrom(1024)
        base = base.decode('utf-8')

        bank['companies'].append(
            {"name": name, "quantity": quantity, "price": base})

        data = json.dumps(bank)
        out = open('../data/market.json', 'w')
        out.write(data)
        out.close()
