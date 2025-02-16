numbers=[1,2,3,4,5,6,7,8,9,12,13,14,15,11,20,22,24,23]
repeat_count = 2

new_numbers=[]
for number in numbers:
    repeated_numbers=[number]*repeat_count
    new_numbers.extend(repeated_numbers)
print(new_numbers)
