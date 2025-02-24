def check(func):
    def wrapper(a,b):
        if b==0:
            raise ZeroDivisionError("denominator can not be zero")
        return int(func(a,b))
    return wrapper

@check
def div(a, b):
   return a / b
try:
    print(div(6,2))
    print(div(6,0))
except ZeroDivisionError as e:
    print(e)