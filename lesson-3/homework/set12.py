set1={'a','b','c','d','e','d','a','t'}
element='o'
if element in set1:
    set1.add(element)
    print('set after adding element is:', set1)
else:
    print('it already exists')