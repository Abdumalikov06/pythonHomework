set1={'a','b','c','d','e','d','a','t'}
l_set=[]
for n in set1:
    if n not in l_set:
        l_set.append(n)
len_set=len(set(l_set))
print(len_set)