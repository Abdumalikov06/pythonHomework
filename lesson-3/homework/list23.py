numbers=[1,2,3,4,5,6,7,8,9,12,13,14,15,11,20,22,24,23]
odd_number=[]
for number in numbers: #it will go number by number in the list
    if number%2!=0: #if remainder is not equal 0 when divided by 2 it will add it to odd_numbers
        odd_number.append(number)
print(odd_number)
