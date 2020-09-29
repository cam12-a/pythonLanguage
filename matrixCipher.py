import numpy as np
from random import randint
from numpy import linalg as LA
import math as mt
import re
import io
import string
class matrixCipher:

    def __init__(self,fileName,matrixSize,key):
        with io.open(fileName, 'r',encoding="UTF-8") as file:
            self.opentext = file.read().replace('\n', '')
        self.opentext=self.opentext.lower()
        self.opentext = re.sub(r'[^\w\s]', '', self.opentext)
        self.opentext=self.opentext.replace(" ","")
        self.matrixSize=matrixSize
        self.key=key
        self.key=[[1,4,8],[3,7,2],[6,9,5]]
    
    def alphabet(self):
        return [chr(i) for i in range(ord('а'), ord('я')+1)]

    def indexofOpenTextinAphabet(self,textToFind):
        return [self.alphabet().index(textToFind[i]) for i in range(len(textToFind))]

    def multmat(self,Key,B,k):
        C=[0 for i in range(self.matrixSize)]
        for i in range(self.matrixSize):
            for j in range(self.matrixSize):
                C[i]+=Key[i][j]*B[k][j]
            #C[i]=int(C[i])%32
        return C

    def matrixCipher(self):
        B,C=[],[]
        if(len(self.opentext)%self.matrixSize==0):
            for i in range(0,len(self.opentext),self.matrixSize):
                B.append(self.indexofOpenTextinAphabet(self.opentext)[i:self.matrixSize+i])
        else:
            return "Невозможно шифровать потому что длина открытого теста и размер матрицы некратны"
        cipherText=""
        for k in range(len(self.opentext)//self.matrixSize):
            C.append(self.multmat(self.key,B,k))
        for i in range(len(C)):
            for j in range(self.matrixSize):
                cipherText+=self.alphabet()[(C[i][j])%32]
        
        return [C,cipherText]

    def decodeMatrixCipher(self,textToDecode,codeCipherText):
        cipherText=""
        self.opentext=textToDecode
        key=np.array(self.key)
        try:
            invKey=LA.inv(key)
        except np.linalg.LinAlgError:
            return "Данная матрица не имеет обратную матрицу"
        B,C=[],[]
        if(len(self.opentext)%self.matrixSize==0):
            for i in range(0,len(self.opentext),self.matrixSize):
                B.append(self.indexofOpenTextinAphabet(self.opentext)[i:self.matrixSize+i])
        else:
            return "Невозможно шифровать потому что длина открытого теста и размер матрицы некратны"
        invKey=invKey.tolist()
        for i in range(len(codeCipherText)):
            C.append(self.multmat(invKey,codeCipherText,i))
        for i in range(len(C)):
            for j in range(self.matrixSize):
                C[i][j]=round(C[i][j])
        for i in range(len(C)):
            for j in range(self.matrixSize):
                cipherText+=self.alphabet()[int(C[i][j])]
        
        return cipherText

    def generateKeyPlayfair(self,opentext):
        d=set()
        self.opentext=opentext
        #Для удаления повторяющих букв используем множество
        d={opentext[i] for i in range(len(self.opentext))}
        for i in range(32):
            if not(self.alphabet()[i] in d):
                d.add(self.alphabet()[i])

        d=list(d)
        #для шифртаблицы сгенерируем матрицу 8*4
        key=[['0' for i in range(8)] for i in range(4)]
        k=0
        for i in range(len(key)):
            for j in range(8):
                if(k<len(d)):
                    key[i][j]=d[k]
                    k+=1
                else:break

        return key
    def returnBigram(self,opentext):
        a=""
        b=""
        opentext=opentext.lower()
        #выравниваем длина чтобы было кратна 2
        if len(opentext)%2!=0:
            opentext+=" "
        #избегаем от повторяющих символов дабовив букв ф мужду ними
        for i in range(0,len(opentext),2):
            if opentext[i:i+2][0]==opentext[i:i+2][1]:
                a+=opentext[i]+"ф"+opentext[i+1]
            else:
                a+=opentext[i:i+2]
        #если остается одну букву дополняем на 2
        if(len(a)%2!=0):
            a+="ф"
        #разбываем строку на биграммы
        for i in range(0,len(opentext),2):
            b+=a[i:i+2]+" "
        b=b.split(' ')
        return b
    def playfair(self,opentext,key):
        textCipher=""
        self.opentext=opentext.lower()
        key=self.generateKeyPlayfair(self.opentext)
        #key=[['р','е','с','п','у','б'],['л','и','к','а','в','г'],['д','ж','з','м','н','о'],['т','ф','х','ц','ч','ш'],['щ','ь','ы','э','ю','я']]
        bigram=self.returnBigram(self.opentext)
        print(key)
        b=0
        col=8
        line=4
        for i in range(len(bigram)-1):
            b=0
            for j in range(len(key)):

                for k in range(col):

                    if key[j][k]==bigram[i][0]:

                        indexI1,indexJ1=j,k
                       
                        b+=1
                    if key[j][k]==bigram[i][1]:

                        indexI2,indexJ2=j,k
                        b+=1
                    if b==2:

                        break
                if b==2:

                    break       
            if b==2:
                if indexI1==indexI2:

                    if indexI2==7:
                        indexJ2=0
                    if indexI1==7:
                        indexJ1=0
                    indexJ1=indexJ1+1
                    indexJ2=indexJ2+1
                    textCipher+=key[indexI1%line][indexJ1%col]+key[indexI1%line][indexJ2%col]+" "
                if indexJ1==indexJ2:
                    if indexJ1==7:
                        indexI1=0
                    if indexJ2==7:
                        indexI2=0                
                    indexI1=indexI1+1
                    indexI2=indexI2+1
                    textCipher+=key[indexI1%line][indexJ1%col]+key[indexI2%line][indexJ1%col]+" " 
                    
                if indexI1!=indexI2 and indexJ1!=indexJ2:
                    if indexJ1>indexJ2:
                        textCipher+=key[indexI1%line][indexJ2%col]+key[indexI2%line][indexJ1%col]+" "
                    if indexJ2>indexJ1:
                        textCipher+=key[indexI1%line][indexJ2%col]+key[indexI2%line][indexJ1%col]+" "
                    #textCipher+=key[indexI1][indexJ2%6]+key[indexI2][indexJ1%6]+" "

        return textCipher
    def descriptPlaysir(self,opentext,key):
        return ""
    
       
matrixSize=3
key=[[randint(0,31) for i in range(matrixSize)] for i in range(matrixSize)]
s=matrixCipher("/home/kali/crypto/variant.txt",matrixSize,key)
inscrpited=s.matrixCipher()
print("Encoding text \n",inscrpited[1])
print("Decoded text\n",s.decodeMatrixCipher(inscrpited[1],inscrpited[0]))
print("Плейфер ключ ",s.playfair("ПУСТЬКОНСУЛЫБУДУТБДИТЕЛЬНЫ",key))