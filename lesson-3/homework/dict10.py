dict1={"name":'John',
       "age":18,
       "email":'johnjohnson@gmail.com'}
key1='age'
if key1 in dict1:
    print('key is:',key1, 'and value is', dict1[key1])
else:
    print(key1, 'is not found in the dictionary')
