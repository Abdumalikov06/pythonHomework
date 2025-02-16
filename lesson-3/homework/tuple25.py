numbers=(1,2,3,4,5,6,7,8,9,9,9,9,9,9,9)
unique_num=[]
for n in numbers:
    if n not in unique_num:
        unique_num.append(n)
tuple_num=tuple(unique_num)
print(tuple_num)