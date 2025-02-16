dict1={"name":'John',
       "age":18,
       "email":'johnjohnson@gmail.com'}
try:
    key1='name'
    print(dict1[key1])
except KeyError:
    print('dictionary is empty')