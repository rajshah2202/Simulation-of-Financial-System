import json

input_file = open('../data/market.json')
f = input_file.read()
bank = json.loads(f)

