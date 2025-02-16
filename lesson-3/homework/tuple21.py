num=(1,2,3,4,5,6,7,8)
given_num=2
new_num=[]
for n in num:
    for i in range(given_num):
        new_num.append(n)
repeated_tuple=tuple(new_num)
print(repeated_tuple)
   