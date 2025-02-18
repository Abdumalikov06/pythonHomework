try:
    for num1 in range(1,101):
        if num1<=1:
            continue
        prime=True
        for num2 in range(2,num1):
            if num1%num2==0:
                prime=False
                break
        if prime:
            print(num1, end=' ')
except KeyError:
     print("KeyError: The key you're trying to access doesn't exist.")