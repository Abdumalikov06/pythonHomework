numbers=[1,2,3,4,5,6,7,8,9,12,13,14,15,11,20,22,24,23,2,2,2,2,2,2,2,2,2]
element=2
indices_element=[]
for i in range(len(numbers)):
    if numbers[i]==element:
        indices_element.append(i)
print(indices_element)

