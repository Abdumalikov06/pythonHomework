my_dict = {
    'a': 1,
    'b': 2,
    'c': 1,
    'd': 3,
    'e': 1
}
nvalue=1
new_list=[]
for key,value in my_dict.items():
    if value==nvalue:
        new_list.append(key)
print(new_list)