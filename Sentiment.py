from pythainlp.tokenize import word_tokenize
text='ที่เปิดปีโป้เค้าเรียกว่าหมู อะไรเหรอคะ ที่เป็นพลาสติก ปีโป้ เรียกยังไง'
e=word_tokenize(text,engine='newmm') 
for x in e : 
    if x == " ":
        e.remove(' ')
print (e)  
#moo2