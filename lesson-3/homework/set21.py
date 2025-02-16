num=[1,1,1,1,2,3,4,5,6,7,8,9,8,8,8,87,6,6,5,44]
try:
    num2=set(num)
    num3=list(num2)
    print(num3)
except KeyError:
    print('list is empty')