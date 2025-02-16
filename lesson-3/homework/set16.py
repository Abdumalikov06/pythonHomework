set1={1,2,3,4,5,6,7,8,9,9,9,9}
even_num=[]
try:
    for n in set1:
        if n%2==0:
            even_num.append(n)
    set2=set(even_num)
    print(set2)
except KeyError:
    print('set is empty')
