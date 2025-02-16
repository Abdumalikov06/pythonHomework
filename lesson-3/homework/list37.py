numbers=[-1,-12,-15,1,2,3,4,5,6,7,8,9,12,13,14,15,11,20,22,24,23]
negative_num=[]
for number in numbers:
    if number<0:
        negative_num.append(number)
print(sum(negative_num))