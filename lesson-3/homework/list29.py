numbers=[1,2,3,4,5,6,7,8,9,12,13,14,15,11,20,22,24,23]
given_index=4
if 0<=given_index<=len(numbers):
    del numbers[given_index]
    print('updated numbers:', numbers)
else:
    print('it is not exist')
