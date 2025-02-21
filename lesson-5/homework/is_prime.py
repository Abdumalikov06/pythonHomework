def is_prime(n):
    if n<2:
        return False
    while n>1:
        for i in range(2,int((n**0.5)+1)):
            if n%i==0:
                return False
           
        return True
num=int(input("enter a positive number: "))
print(is_prime(num))