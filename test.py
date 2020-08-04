import json

data_dir = 'data_to_crc/'

with open(data_dir + 'pmath.json', 'r') as f:
    datastore = json.load(f)

for data in datastore:
    print(data['catalog_number']) 
    print(data['prerequisites'])

print(len(datastore))
