def convert_cel_to_far(c):
    cel_to_far =(c - 32) * 5/9
    output=f"{c} degree F = {cel_to_far:.2f} degree C"
    return output
def convert_far_to_cel(f):
    far_to_cel=f * 9/5 + 32
    output=f"{f} degree C={far_to_cel:.2f} degree C"
    return output
    
cel=float(input("Enter a temperature in degrees F: "))
far=float(input("Enter a temperature in degrees C: "))
print(convert_cel_to_far(cel))
print(convert_far_to_cel(far))

  