dict1={"name":'John',
       "age":18,
       "email":'johnjohnson@gmail.com'}
key1='age'
if key1 in dict1:
    del dict1[key1]
    print('after deleting the key, dictionary is:',dict1)
else:
    print(key1,'is not in the dictionary')