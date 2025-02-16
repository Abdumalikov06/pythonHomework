my_dict = {
    'a': 1,
    'b': 2,
    'c': 1,
    'd': 3,
    'e': 1
}
my_dict2={
    'ad': 1,
    'r': 2,
    't': 8,
    'y': 5,
    'u': 4
}
set_dict=set(my_dict.keys())
set_dict2=set(my_dict2.keys())
same_keys=set_dict.intersection(set_dict2)
if len(same_keys)>0:
    print('they have keys in common')
else:
    print('they do not have keys in common')