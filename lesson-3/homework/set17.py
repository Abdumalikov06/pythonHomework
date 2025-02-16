set1={1,2,3,4,5,6,7,8,9,9,9,9}
odd_num=[]
try:
    for n in set1:
        if n%2==1:
            odd_num.append(n)
    set2=set(odd_num)
    print(set2)
except KeyError:
    print('set is empty')