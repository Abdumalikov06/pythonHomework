my_dict = {
    'a': 1,
    'b': 2,
    'c': 1,
    'd': 3,
    'e': 1
}
target_value = 1
count = 0
for value in my_dict.values():
    if value == target_value:
        count += 1
print(f"The value {target_value} appears {count} times in the dictionary.")
