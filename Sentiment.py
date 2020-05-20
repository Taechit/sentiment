from pythainlp.tokenize import word_tokenize
import codecs
import re 

text='ทั้งถุงมีสีขาวอันเดียว...คืออันเดียวจิงๆๆๆๆๆ ทำมัยยยยย  สีที่ไม่ชอบก็มีเยอะเกินนนนนนน'
word=word_tokenize(text,engine='newmm') 
for x in word : 
    if x == " ":
        word.remove(' ')

#word.replace("ปี","เทส")
#print (word)  

with codecs.open('peepo', 'r', "utf-8") as f:
  lines = f.readlines()
textPeepo=[e.strip() for e in lines]
del lines
f.close() # ปิดไฟล์
#print(textPeepo)
for x in textPeepo :
    word = word_tokenize(x,engine='newmm')
    pattern = re.compile("[A-Za-z0-9/+*#!]+")
    for x in word :
        if x == " ":
            word.remove(x) #ลบข่องว่างออก
        elif pattern.search(x): 
            word.remove(x)
        elif len(x) >= 3:
            if x[len(x)-1] == x[len(x)-2] and x[len(x)-2] == x[len(x)-3]:
                word.remove(x)          
    print(word)
