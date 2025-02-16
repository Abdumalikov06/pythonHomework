my_dict = {
    'c': 3,
    'a': 1,
    'b': 2,
    'e': 5,
    'd': 4,
    'f':11
}
condition=9
filtered_dict={}
for key,value in my_dict.items():
    if value<condition:
        filtered_dict[key]=value
print(filtered_dict)