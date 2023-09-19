data = {'a': 1, 'b': 2, 'c': 3}
print('dict data:', data)
# items values keys
# print('items:', data.items())
# print('values: ', data.values())
# print('keys: ', data.keys())

# new version
# keys = data.keys()
# items = data.items()
# values = data.values()
# print('mapping:', keys.mapping)
# print('mapping:', items.mapping)
# print('mapping:', values.mapping)

# old version
keys = ['name', 'age', 'gender']
values = ['jojo', 25, 'Mm']
# values = ['jojo', 25, 'Mm', 5]  # error coz length is not same
dictionary = dict(zip(keys, values))  # use dic(zip()) to create a dict
print(dictionary)

# new version
# new param: strict = True means each list (keys, values) has the same length
dictionary2 = dict(zip(keys, values, strict=True))
print(dictionary2)
