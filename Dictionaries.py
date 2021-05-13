# Dictionaries
info = {
    'name': 'om', 'city': 'pune', 'age': 30
}
print(info)

# Access Items
info = {
    'name': 'om', 'city': 'pune', 'age': 30
}
print(info['name'])
print(info['city'])

# using Get() method
info = {
    'name': 'om', 'city': 'pune', 'age': 30
}
print(info.get('name'))
print(info.get('age'))

# change value
i = {'name': 'jay', 'city': 'pune', 'age': 30}
i['city'] = 'mumbai'
print(i)

# Loop with dictionary
info1 = {'name': 'om', 'city': 'pune', 'age': 34}
for values in info1:
    print(values)

# Loop with dictionary
info2 = {'name': 'om', 'city': 'pune', 'age': 34}
for values in info2:
    print(values)

# FETCH BOTH KEYS AND VALUES
info3 = {'name': 'om', 'city': 'pune', 'age': 34}
for i, j in info3.items():
    print(i, j)

# delete dict
info2 = {'name': 'om', 'city': 'pune', 'age': 34}
del info2
print(info2)
