numbers=[-1,-12,-15,1,2,3,4,5,6,7,8,9,12,13,14,15,11,20,22,24,23]
sublist_size=2
new_numbers=[]
for i in range(0, len(numbers),sublist_size):
    new_numbers.append(numbers[i:i+sublist_size])
print(new_numbers)

