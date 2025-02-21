def factor_of_positive_int(n):
    initial=1
    while initial<=n:
        if n%initial==0:
            print(f"{initial} is a factor of {n} ")
        initial+=1
user_input=int(input("Enter a positive integer: "))
try:
    if user_input >0:
        factor_of_positive_int(user_input)
    else:
        f_user_input=int(input("Enter a positive, non-zero integer: "))
        factor_of_positive_int(f_user_input)
except KeyError:
    print("Invalid input! you entered not valid number.")