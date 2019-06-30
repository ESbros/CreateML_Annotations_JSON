import json

filename = '/Users/edsg/Desktop/annotations.json'

with open(filename, 'r') as f:
    datastore = json.load(f)

#Use the new datastore datastructure
print(len(datastore))
print(datastore)
print('\n')

for dictionary in datastore:
    print(dictionary)
    print('\n')
    print(dictionary['annotations'])
    print('\n')
    print(dictionary['annotations']['label'])
    print('\n')
    print(dictionary['annotations']['coordinates'])