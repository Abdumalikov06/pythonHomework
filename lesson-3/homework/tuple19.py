numbers=(1,2,3,4,5,6,6,7,8,9,9)
num=6
lnum=list(numbers)
if num in lnum:
    lnum.remove(num)
tnum=tuple(lnum)
print(tnum)