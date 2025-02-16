main_list = [1, 2, 3, 4, 5, 6]
sublist = [3, 4, 6]
found = False
for i in range(len(main_list) - len(sublist) + 1):
    if main_list[i:i+len(sublist)] == sublist:
        found = True 
        break  
if found:
    print("Sublist found!")
else:
    print("Sublist not found!")
