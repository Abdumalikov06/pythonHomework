dict1={"name":'John',
       "age":18,
       "email":'johnjohnson@gmail.com'}
key1='name'
try:
    if key1 in dict1:
        print('it exists and value is', dict1[key1])
    else:
        print('key is not in dictionary')
except KeyError:
    print('dictionary is empty')