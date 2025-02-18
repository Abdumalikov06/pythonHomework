try:
    num=int(input('enter an integer n:'))
    for i in range(1,num):
        print(i**2)
except KeyError:
     print("KeyError: The key you're trying to access doesn't exist.")