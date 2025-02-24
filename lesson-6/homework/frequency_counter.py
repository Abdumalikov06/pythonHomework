import os
import re
from collections import Counter
def frequncy(paragraph):
    words = re.findall(r'\b\w+\b', paragraph.lower())
    count=Counter(words)
    return count
file_name='sample.txt'
if not os.path.exists(file_name):
    print("file does not exists")
    paragraph =input("Enter a paragraoh to create a file: ")
    with open('sample.txt','w')  as file:
        file.write(paragraph)
        print('file opened successfully')
with open('sample.txt', 'r') as file:
    content=file.read()
    word_frequency=frequncy(content)
total_words=sum(word_frequency.values())
print(f"Total words: {total_words}")
common_words=word_frequency.most_common(5)
print("Top 5 most common words: ")
for words, values in common_words:
    if values>1:
        print(f"{words}-{values} times")
    else:
        print(f"{words}-{values} time")
try:
    with open("words_count_report.txt",'w') as file:
        file.write("Word count report\n")
        file.write(f"Total words:{total_words}\n")
        file.write("Top 5 words:\n")
        for words,values in common_words:
            file.write(f"{words}-{values}\n")
except Exception as e:
    print(f"Error writing to file word_count_report.txt: {e}")
        
