set1={'a','b','c','d','e','d','a','t'}
element='a'
if element in set1:
    set1.remove(element)
    print('set after', element , 'is removed:', set1)
else:
    print(element, 'is not in the set')