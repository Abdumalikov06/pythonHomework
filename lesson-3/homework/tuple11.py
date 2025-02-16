numbers=(1,2,3,4,5,6,7,8,9,9,9,9)
num=9
indices=[]
if num not in numbers:
    print("element is not in the tuple")
for i in range(len(numbers)):
    if numbers[i]==num:
        indices.append(i)
print(indices)