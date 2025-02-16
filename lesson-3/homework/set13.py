set1={'a','b','c','d','e','d','a','t'}
try:
    r_element=set1.pop()
    print('removed element:',r_element,'\n',
          'updated set', set1)
except KeyError:
    print('set is empty')