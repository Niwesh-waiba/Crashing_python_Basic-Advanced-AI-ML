import json

to_save_dictionary={
    'Student': ['Ram', 'Shyam', 'Sita'],
    'Marks': [10,20,30],
 }

with open('databse_json.json','w') as f:
    json.dump(to_save_dictionary,f)

with open('databse_json.json','r') as f:
    loaded_json=json.load(f)

print(loaded_json)

student = loaded_json['Student']
