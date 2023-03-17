from wordslist import words
valid=[]
for i in words:
    if '-' not in i and ' ' not in i:
        valid.append(i)

   
