import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = socket.gethostname()
port = 5050

s.bind((host, port))

while True:

    input_file = open('../data/bank.json')
    f = input_file.read()
    bank = json.loads(f)

    data, addr = s.recvfrom(1024)
    data = data.decode('utf-8')
    if data == '0':
        data = "What is your name?"
        s.sendto(data.encode(), addr)

        name, addr = s.recvfrom(1024)
        name = name.decode('utf-8')

        bank['investors'].append({"name": name, "amount": 0})
        data = json.dumps(bank)

        out = open('../data/bank.json', 'w')
        out.write(data)
        out.close()

    if data == '1':
        data = "How much?"
        s.sendto(data.encode(), addr)
        name, addr = s.recvfrom(1024)
        amount, addr = s.recvfrom(1024)

        for i in bank['investors']:
            if i['name'] == name.decode('utf-8'):
                i['amount'] = i['amount'] + int(amount)

        data = json.dumps(bank)
        out = open('../data/bank.json', 'w')
        out.write(data)
        out.close()

    if data == '2':
        data = "How much?"
        s.sendto(data.encode(), addr)
        name, addr = s.recvfrom(1024)
        amount, addr = s.recvfrom(1024)

        for i in bank['investors']:
            if i['name'] == name.decode('utf-8'):
                if i['amount'] > int(amount):
                    i['amount'] = i['amount'] - int(amount)
                else:
                    print('No sufficient balance')

        data = json.dumps(bank)
        out = open('../data/bank.json', 'w')
        out.write(data)
        out.close()

    if data == '3':
        name, addr = s.recvfrom(1024)
        name = name.decode('utf-8')
        for i in bank['investors']:
            if i['name'] == name:
                amount = i['amount']
        amount = str(amount)
        s.sendto(amount.encode(), addr)
