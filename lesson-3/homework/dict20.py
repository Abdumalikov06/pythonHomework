my_dict = {
    'c': 3,
    'a': 1,
    'b': 2,
    'e': 5,
    'd': 4
}

sorted_keys = sorted(my_dict.keys())
sorted_dict = {}
for key in sorted_keys:
    sorted_dict[key] = my_dict[key]
print(sorted_dict)
