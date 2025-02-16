my_dict = {
    'a': 1,
    'b': 2,
    'c': 1,
    'd': 3,
    'e': 1
}
n='f'
if n not in my_dict.keys():
     value=my_dict.setdefault(n,0)
print(value)
