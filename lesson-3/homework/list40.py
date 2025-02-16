numbers=[-1,-12,-15,1,2,3,4,5,6,7,8,9,12,13,1,1,1,1,1]
unique_elements=[]
for number in numbers:
    if number not in unique_elements:
        unique_elements.append(number)
print(unique_elements)