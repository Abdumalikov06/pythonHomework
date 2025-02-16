num1=[1,2,3,4,5]
num2=[6,7,8,9,10,1,1,2]
try:
    num3=num1+num2
    print(set(num3))
except KeyError:
    print('lists are empty')
