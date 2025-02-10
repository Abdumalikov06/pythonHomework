a=input()
vowels='aeiouAEIOU'
c=''.join([char if char not in vowels else "*" for char in a])
print(c)
