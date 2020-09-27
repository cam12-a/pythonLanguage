import numpy as np
from random import randint
from numpy import linalg as LA
import math as mt
import re
class matrixCipher:

    def __init__(self,fileName,matrixSize,key):
        with open(fileName, 'r') as file:
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
       
matrixSize=3
key=[[randint(0,31) for i in range(matrixSize)] for i in range(matrixSize)]
s=matrixCipher("/home/kali/crypto/text.txt",matrixSize,key)
inscrpited=s.matrixCipher()
print("Encoding text \n",inscrpited[1])
print("Decoded text\n",s.decodeMatrixCipher(inscrpited[1],inscrpited[0]))
