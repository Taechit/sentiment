from pythainlp.tokenize import word_tokenize
text='ที่เปิดปีโป้เค้าเรียกว่า อะไรเหรอคะ ที่เป็นพลาสติก ปีโป้ เรียกยังไง'
word=word_tokenize(text,engine='newmm') 
for x in word : 
    if x == " ":
        word.remove(' ')

word.replace("ปี","เทส")
print (word)  
#moomek
#moo 2
