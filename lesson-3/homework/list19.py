numbers=[1,2,3,4,5,6,7,8,9,12,13]
old_number=8
new_number=100

if old_number in numbers:
    index = numbers.index(old_number)
    numbers[index]=new_number
print(numbers)