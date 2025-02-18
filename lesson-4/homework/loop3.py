txt='abcabcdabcdeabcdefabcdefg'
#txt="Hello"
#txt = "hello"  
used_chars = 'euioaAEIUO'  
i = 2
try:
    while i < len(txt):
        while True:
            if txt[i] not in used_chars: 
                txt = txt[:i+1] + '_' + txt[i+1:]  
                used_chars = used_chars + txt[i]  
                break  
            i += 1  

        i += 4  
    if txt[-1]=='_':
        print(txt[:-1])
    else:
        print(txt)
except KeyError:
     print("KeyError: The key you're trying to access doesn't exist.")
 