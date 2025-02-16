try:
    nested_dict={
        'x': {'a':1,
        'b':2},
        'y':{
            'c':3,
            'd':4
        }
    }
    print(nested_dict['x']['a'])
except KeyError:
    print('list is empty')