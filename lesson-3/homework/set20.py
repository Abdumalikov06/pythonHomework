num={1,2,3,4,5,6}
num1={4,5,6,7,8,9}
try:
    num2=num.isdisjoint(num1)
    print(num2)
except KeyError:
    print('sets are empty')