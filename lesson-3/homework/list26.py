numbers=[1,2,3,4,5,6,7,8,9,12,13,14,15,11,20,22,24,23]

# Check if the list has an odd or even number of elements
n= len(numbers)

if n % 2 == 1:
    # Odd number of elements: return the middle element
    middle_element = numbers[n // 2]
    print("Middle element:", middle_element)
else:
    # Even number of elements: return the two middle elements
    middle_elements = numbers[n // 2 - 1 : n // 2 + 1]
    print("Middle elements:", middle_elements)