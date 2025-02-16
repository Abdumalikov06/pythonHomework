my_dict = {
    'a': 1,
    'b': {'x': 10, 'y': 20},
    'c': 3,
    'd': {'z': 30}
}
for key, value in my_dict.items():
    if isinstance(value, dict):
        print(f"The value for key '{key}' is a dictionary: {value}")