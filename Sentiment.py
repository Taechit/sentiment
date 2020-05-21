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

def naiveBayes (word,training):
    countPos = 0
    countNeg = 0
    
    print(word)
    for x in training :
        if(x.count("Positive")): countPos=countPos+1
        elif(x.count("Negative")): countNeg = countNeg+1
    classProbPos = countPos/len(training)
    classProbNeg = countNeg/len(training)
    print(classProbPos)
    print(classProbNeg)
    bayesPos=1
    bayesNeg=1

    for n in word : #วนลูปแต่ละคำใน word ที่เข้ามา
        print("word =",n)
        countWordPos = 0
        countWordNeg = 0
        for x in training : 
            if n == x[0] :
                if(x.count("Positive")): 
                    countWordPos = countWordPos+1
                elif(x.count("Negative")):
                    countWordNeg = countWordNeg+1
        countWord = countWordPos + countWordNeg
        #countPos จำนวน positive ทั้งหมดที่มีใน trainingData
        #countNeg จำนวน negative ทั้งหมดที่มีใน trainingData
        print("Count posisitve of",n,"is",countWordPos,",All positive words =",countPos,",Ratio beetween",n,"and all positive word =",countWordPos/countPos)
        print("Count negative of",n,"is",countWordNeg,",All negative words =",countNeg,",Ratio beetween",n,"and all negative word =",countWordNeg/countNeg)
        print("Probability of",n,"=",countWord/len(training)) 
        if(countWord/len(training)!=0):
            somethingPos = ((countWordPos/countPos)*classProbPos)/(countWord/len(training))
            somethingNeg = ((countWordNeg/countNeg)*classProbNeg)/(countWord/len(training))
            bayesPos = bayesPos*somethingPos
            bayesNeg = bayesNeg*somethingNeg       
        print("bayesPos =",bayesPos)
        print("bayesNeg =",bayesNeg)
    if (abs(bayesPos-bayesNeg)<=0.1):
        return("ให้ความรู้สึกธรรมด้าธรรมดา")
    else:
        if(bayesPos>bayesNeg): return("ให้ความรู้สึกที่ดี")
        else : return("ให้ความรู้สึกไม่ดีเลย")

textPeepo = ['ไม่ชอบ']
for txt in textPeepo :
    word = word_tokenize(txt,engine='newmm')
    pattern = re.compile("[A-Za-z0-9/+*#!]+")
    for x in word :
        if x == " ":
            word.remove(x) #ลบข่องว่างออก
        elif pattern.search(x): 
            word.remove(x)
        elif len(x) >= 3:            
            if x[len(x)-1] == x[len(x)-2] and x[len(x)-2] == x[len(x)-3]:
                word.remove(x)  
    sentiment = naiveBayes(word,trainingData) 
    print(txt,sentiment)      

#x='หมู'
#print(x.find('หมู'))
