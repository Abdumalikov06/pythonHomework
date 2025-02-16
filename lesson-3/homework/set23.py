import random
set1=set()
set_number=6
lower_bound=1
upper_bound=100
while len(set1)<set_number:
    set1.add(random.randint(lower_bound,upper_bound))

print(set1)

