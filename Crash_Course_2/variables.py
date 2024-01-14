my_dict = {'key1': 'value1', 'key2': 111}
my_dict2 = {
   'key1': 'value1',
   'key2': 111,
   'key3': [1, 2, 3],
   'key4': {'nested_key': 'nested_value'}
}

print(my_dict2['key1'])
print(my_dict2['key4']['nested_key'])

my_set = {1, 1, 1, 2, 2, 2, 3, 3, 3}
print(my_set)