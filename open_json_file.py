import json

filename = 'path_to/annotations.json'

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
    print(dictionary['annotations'][0]['label'])
    print('\n')
    print(dictionary['annotations'][0]['coordinates'])
    print('\n')
    print(dictionary['annotations'][0]['coordinates']['x'])
    print(dictionary['annotations'][0]['coordinates']['y'])
    print(dictionary['annotations'][0]['coordinates']['width'])
    print(dictionary['annotations'][0]['coordinates']['height'])
    print('\n')
