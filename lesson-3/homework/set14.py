set1={1,2,3,4,5,6,7,8,9,9,9,9}
try:
    print(max(set1))
except KeyError:
    print('set is empty')