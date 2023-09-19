dict1 = {'a': 1}
dict2 = {'b': 2}
# old version
dict1.update(dict2)  # dict1 changed its value
print(dict1)

# new version |
result = dict1 | dict2  # dict1 and dict2 don't change
print(result)

# assign the value to dict1 after combining two dicts
dict1 |= dict2   # => dict1=dict1|dict2   same for +=
print(dict1)
