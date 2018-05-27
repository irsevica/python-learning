examp_dict = { 'food': 'spam', 'quanity' : 4, 'colour': 'pink'}
print(examp_dict['food'])

#changing values

examp_dict['food'] = 'mushroom'
print(examp_dict)

# nested dictionaries
rec = { 'name': {'first': 'Bob', 'last': 'Smith'}, 
        'jobs': ['dev', 'mgr'], 
        'age': 40.5}

print(rec)
print(rec['jobs'][0])

# sort list alphabetically by key and print line by line

for key in sorted(rec):
    print(key, '=>', rec[key])