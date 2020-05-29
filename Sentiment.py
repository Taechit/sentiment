#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
from pythainlp.tokenize import word_tokenize
import codecs
import re 

#สำหรับแยกคำ
def stringSplit(txt):
    pos = txt.rfind(',')
    return txt[:pos-1],txt[pos+1:]


def naiveBayes (word,training):
    countPos = 0
    countNeg = 0
    
    #print(word)
    for x in training :
        if(x.count("Positive")): countPos=countPos+1
        elif(x.count("Negative")): countNeg = countNeg+1
    classProbPos = countPos/len(training)
    classProbNeg = countNeg/len(training)
    bayesPos=1
    bayesNeg=1

    for n in word : #วนลูปแต่ละคำใน word ที่เข้ามา
        #print("word =",n)
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
        #print("Count posisitve of",n,"is",countWordPos,",All positive words =",countPos,",Ratio beetween",n,"and all positive word =",countWordPos/countPos)
        #print("Count negative of",n,"is",countWordNeg,",All negative words =",countNeg,",Ratio beetween",n,"and all negative word =",countWordNeg/countNeg)
        #print("Probability of",n,"=",countWord/len(training)) 
        if(countWord/len(training)!=0):
            somethingPos = ((countWordPos/countPos)*classProbPos)/(countWord/len(training))
            somethingNeg = ((countWordNeg/countNeg)*classProbNeg)/(countWord/len(training))
            bayesPos = bayesPos*somethingPos
            bayesNeg = bayesNeg*somethingNeg       
        #print("bayesPos =",bayesPos)
        #print("bayesNeg =",bayesNeg)
    if (abs(bayesPos-bayesNeg)<=0.1):
        return("ให้ความรู้สึกธรรมด้าธรรมดา",0)
    else:
        if(bayesPos>bayesNeg): return("ให้ความรู้สึกที่ดี",1)
        else : return("ให้ความรู้สึกไม่ดีเลย",-1)

#textPeepo = ['คืองี้นะ รู้แหละแบบใหม่มีขายแยกสี แต่ๆๆ อิชั้นยังอยากมีโมเม้น ถุงนี้จะได้สีไหนเท่าไหร่บ้างนะ แต่มันก็ต้องมีครบทุกสีแหละถูกม่ะ ละจะเลือกถุงที่มีสีที่ชอบเยอะๆ ไปถึงชั้นขายของนับร้อยถุงตรงหน้า ไม่มีสีเขียวเลย ไม่มีเลยอ่ะ บางถุงมีสองสี แม๊ ได้อ่อ ประเด็นคืองงตัวเอง ดราม่าทำไม #ปีโป้']
def sentimentAnalized (filePeepo,trainingData):
    textPeepo = filePeepo
    round=1
    rank = 0
    print(textPeepo)
    for txt in textPeepo :
        #txt.replace(" ", "")
        re.sub(' +','',txt)
        word = word_tokenize(txt,engine='newmm')
        pattern = re.compile("[A-Za-z0-9/+*!#]+")
        for x in word :
            if x == " ":
                word.remove(x) #ลบข่องว่างออก
            elif pattern.search(x): 
                word.remove(x)
            elif len(x) >= 3:            
                if x[len(x)-1] == x[len(x)-2] and x[len(x)-2] == x[len(x)-3]:
                    word.remove(x)  
        sentiment ,ranking,countd,countda,countnotd  = naiveBayes(word,trainingData) 
        countReald= countReald + countd
        countRealda= countRealda + countda
        countRealNotD = countRealNotD + countnotd
        rank = rank+ranking
        print(round,")",txt,'\n',"-->",sentiment)
        round=round+1
    print("คนพูดถึงในทางที่ดี : ",rank/len(textPeepo)*100,'%','count of good =',countReald,' count of neutral =',countRealda,' count of not good =',countRealNotD, )

def readFile(sorce):
    #อ่านไฟล์ 
    with codecs.open(sorce, 'r', "utf-8") as f:
        lines = f.readlines()
    textFile=[x.strip() for x in lines]
    del lines
    f.close() # ปิดไฟล์
    return textFile
def main():
    
    #อ่านไฟล์ peepo
    textPeepo = readFile("peepo")
    textApple = readFile("peepoApple")
    textGrape = readFile("peepoGrape")
    textLychee = readFile("peepoLychee")
    textOrange = readFile("peepoOrange")
    textStraw = readFile("peepoStraw")
    training = readFile("trainingData")

    #training data
    trainingData = []
    for x in training:
        string1,string2 = stringSplit(x)
        trainingData.append((string1,string2))
        sentimentAnalized
    print('ปีโป้โดยรวม')
    sentimentAnalized(textPeepo,trainingData)
    print("-----------------\n",'ปีโป้เขียวรสแอปเปิ้ล')
    sentimentAnalized(textApple,trainingData)
    print("-----------------\n",'ปีโป้สีม่วงรสองุ่น')
    sentimentAnalized(textGrape,trainingData)
    print("-----------------\n",'ปีโป้สีขาวรสลิ้นจี่')
    sentimentAnalized(textLychee,trainingData)
    print("-----------------\n",'ปีโป้สีส้มรสส้ม')
    sentimentAnalized(textOrange,trainingData)
    print("-----------------\n",'ปีโป้สีแดงรสสตอเบอรี่')
    sentimentAnalized(textStraw,trainingData)

if __name__ == "__main__":
    main()
