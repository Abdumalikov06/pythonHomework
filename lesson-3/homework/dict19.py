my_dict = {
    'a': 1,
    'b': 2,
    'c': 1,
    'd': 3,
    'e': 1,
    'f':4
}
value=[]
for n in my_dict.values():
    if n not in value:
        value.append(n)
print(len(value))