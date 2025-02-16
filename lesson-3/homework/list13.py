fruits=['apple','banana','orange','grape', 'pineapple','cherry','apple']
fruit='orange'
try:
    fruit_index= fruits.index(fruit)
    print(fruit_index)
except ValueError:
    print(fruit, "is not in the list")
