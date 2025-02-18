try:
    password=input('enter password: ')
    while True:
        if len(password)<8:
            print("Password is too short")
        elif not any(char.isupper() for char in password):
            print("Password must contain an uppercase letter.")
        elif len(password)>8 and password!=password.lower():
            print("Password is strong.")
            break
        password=input("Enter password: ")
except KeyError:
     print("KeyError: The key you're trying to access doesn't exist.")