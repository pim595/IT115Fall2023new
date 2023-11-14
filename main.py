#import the class library
import json

#create the data dictionary

data = {

    'name': 'Quynh Nguyen',
    'age':24,
    'city':'Shoreline,WA',
    'interests': ['hiking','cooking','videogames'],
    'is_student': True

}

#
with open('data.json','w') as json_file:

    json.dump(data,json_file,indent=4)

print('Data has been written to data.json')


#
with open('data.json','r') as json_file:

    loaded_data = json.load(json_file)

print("Successfully able to read data.json")
print(loaded_data)

#modifying loaded data
loaded_data['age'] = 34
loaded_data['interests'].append('Cats')

#
with open('data.json','w') as json_file:

    json.dump(loaded_data, json_file, indent=4)

print('Modified data written to data.json')