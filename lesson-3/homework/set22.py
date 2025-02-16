num=[1,1,2,2,3,3,4,4,5,6,67,87,9,9]
try:
    num2=set(num)
    print(len(num2))
except KeyError:
    print('list is empty')
