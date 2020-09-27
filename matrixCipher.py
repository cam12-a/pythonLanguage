import numpy as np
from random import randint
from numpy import linalg as LA
import math as mt
class matrixCipher:

    def __init__(self,opentext,matrixSize,key):
        self.opentext=opentext.lower()
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
            C[i]=int(C[i])%32
        return C

    def matrixCipher(self):
        B=[]
        print(self.opentext)
        C=[]
        if(len(self.opentext)%self.matrixSize==0):
            for i in range(0,len(self.opentext),self.matrixSize):
                B.append(self.indexofOpenTextinAphabet(self.opentext)[i:self.matrixSize+i])
        else:
            return "Невозможно шифровать потому что длина открытого теста и размер матрицы некратны"
        cipherText=""
        print("Code cipherText ",B)
        print("Key in encode ",self.key)
        for k in range(len(self.opentext)//self.matrixSize):
            C.append(self.multmat(self.key,B,k))
        print("C ",C)
        for i in range(len(C)):
            for j in range(self.matrixSize):
                cipherText+=self.alphabet()[(C[i][j])%32]
        return cipherText

    def decodeMatrixCipher(self,textToDecode):
        #det=np.array(self.key)
        cipherText=""
        self.opentext=textToDecode
        key=np.array(self.key)
        print("Key in decode ",key)
        invKey=LA.inv(key)
        for i in range(self.matrixSize):
            for j in range(self.matrixSize):
                invKey[i][j]=invKey[i][j]%32
        print("Inversed key",invKey)
        print(self.opentext)
        B=[]
        C=[]
        if(len(self.opentext)%self.matrixSize==0):
            for i in range(0,len(self.opentext),self.matrixSize):
                B.append(self.indexofOpenTextinAphabet(self.opentext)[i:self.matrixSize+i])
        else:
            return "Невозможно шифровать потому что длина открытого теста и размер матрицы некратны"
        print("code encoding text ",B)
        for k in range(len(self.opentext)//self.matrixSize):
            C.append(self.multmat(invKey,B,k))
        print("C111 ",C)
        for i in range(len(C)):
            for j in range(self.matrixSize):
                cipherText+=self.alphabet()[int(C[i][j])]
        return cipherText
       
matrixSize=3
key=[[randint(0,31) for i in range(matrixSize)] for i in range(matrixSize)]
print("key outup object ",key)
s=matrixCipher("ЗАБАВА",matrixSize,key)
inscrpited=s.matrixCipher()
print(inscrpited)
print(s.decodeMatrixCipher(inscrpited))
