a=input("Enter a sentence: ")
b=a[::-1]
b=b.lower()
if a==b:
    print("Palindorme")
else:
    print("not Palindorme")