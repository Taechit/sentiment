from pythainlp.tokenize import word_tokenize
import codecs
import re 

#method สำหรับแยกคำ
def stringSplit(txt):
    pos = txt.rfind(',')
    return txt[:pos-1],txt[pos+1:]


#อ่านไฟล์ peepo
with codecs.open('peepo', 'r', "utf-8") as f:
  lines = f.readlines()
textPeepo=[x.strip() for x in lines]
del lines
f.close() # ปิดไฟล์


#อ่านไฟล์ training
with codecs.open('trainingData', 'r', "utf-8") as f:
  lines = f.readlines()
training=[x.strip() for x in lines]
del lines
f.close() # ปิดไฟล์


#training data
trainingData = []
for x in training:
    string1,string2 = stringSplit(x)
    trainingData.append((string1,string2))


#
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

#x='หมู'
#print(x.find('หมู'))
