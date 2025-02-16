numbers=[1,2,3,4,5,6,7,8,9,12,13,14,15,11,20,22,24,23]
even_number=[]
for number in numbers: #it will go number by number in the list
    if number%2==0: #if remainder =0 when divided by 2 it will add it to even_numbers
        even_number.append(number)
print(even_number)
