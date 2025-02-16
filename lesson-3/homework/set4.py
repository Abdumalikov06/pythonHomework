set1={'a','b','c','d'}
set2={'a','b'}
if set1.issubset(set2) or set2.issubset(set1):
    print(bool(True))
else:
    print(bool(False))