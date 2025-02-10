a=input()
vowels="aeiouAEIOU"
vowels_n=0
consonant_n=0
for char in a:
    if char in a:
        if char in vowels:
            vowels_n=vowels_n+1
        else:
            consonant_n=consonant_n+1
print("number of vowels",vowels_n,"number of consonants", consonant_n)


