my_dict = {
    'c': 3,
    'a': 1,
    'b': 2,
    'e': 5,
    'd': 4
}


sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print(sorted_dict)