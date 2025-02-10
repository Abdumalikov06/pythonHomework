a=input()
b=any(char.isdigit() for char in a)
if b:
    print('string contains numbers')
else:
    print('string does not contain numbers')
            
