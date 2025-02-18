list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
list3=[]
try:
    for l in list1:
        if l not in list2:
            list3.append(l)
    for i in list2:
        if i not in list1:
            list3.append(i)
    print(list3)
except KeyError:
     print("KeyError: The key you're trying to access doesn't exist.")
