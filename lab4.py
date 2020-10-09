import random
import io
import re
def factors(n):
    i = 2
    factors = []
    while i <= n:
        if (n % i) == 0:
            factors.append(i)
            n = n / i
        else:
            i = i + 1
    return factors

def formatOpenText(fileName):
    opentext=""
    with io.open(fileName, 'r',encoding="UTF-8") as file:
        opentext = file.read().replace('\n', '')
    #opentext = re.sub(r'[^\w\s]', '', opentext)
    #opentext=opentext.replace(" ","")
    return opentext

def generateMatrix(openText):
    if not verifyLenght(openText):
        return "Открытый текст слишком короткий"
    ligne,col,isnotdivided=0,0,0
    if len(factors(len(openText)))==1:
        col=3
        ligne=len(openText)//col
        isnotdivided=1
    else:
        col=factors(len(openText))[len(factors(len(openText)))-1]
        ligne=len(openText)//col
    matrixPermutation=[]
    text=""
    for i in range(0,col*ligne,ligne):
        text+=openText[i:i+ligne]+"№"
    if isnotdivided==1:
        text+=openText[col*ligne:(col*ligne)+len(openText)%col]+"№"
    text=text.split('№')
    for i in range(len(text)):
        if (i+1)%2!=0:
            matrixPermutation.append(text[i])
        else:
            matrixPermutation.append(text[i][::-1])
    return [isnotdivided, matrixPermutation]

def verifyLenght(openText):
    if len(openText)==1:
        return False
    else:
        return True

def permutationEncryption(openText):
    if not verifyLenght:
        return "Открытый текст слишком короткий"
    if len(factors(len(openText)))==1:
        openText+="*"
    matrix=generateMatrix(openText)[1]
    isnotdivided=generateMatrix(openText)[0]
    key=random.sample(range(0,len(matrix[0][:])),len(matrix[0][:]))
    ligne=len(matrix[0][:])
    col=len(matrix)
    print("Permutation ",ligne,col,key,len(openText))
    textCipher=""
    if generateMatrix(openText)[0]==1:
        for i in range(ligne):
            for j in range(col-2):
                textCipher+=matrix[j][key[i]]
            if len(matrix[j][key[i]])>=key[i]:
                textCipher+=matrix[col-2][key[i]]
    else:
        for i in range(ligne):
            for j in range(col-1):
                textCipher+=matrix[j][key[i]]
    return [textCipher,matrix,key]

def decodePermutationEncrypt(textCipher,key):
    decodeText=""
    tempDecodeText=""
    if len(factors(len(textCipher)))==1:
        textCipher+="*"
    col=len(key)
    ligne=len(textCipher)//col
    matrixDecode=dict()
    print("decode ",ligne,col,key,len(textCipher))
    for i in range(0,len(textCipher),ligne):
        tempDecodeText+=textCipher[i:i+ligne]+"№"
    tempDecodeText=tempDecodeText.split('№')
    #print(tempDecodeText,len(tempDecodeText))
    for i in range(len(tempDecodeText)-1):
        matrixDecode.update({tempDecodeText[i]:key[i]})
    matrixDecode=dict(sorted((value, key) for (key,value) in matrixDecode.items())) 
    #print("fdsfsdfg ",matrixDecode,len(key),ligne)
    for i in range(ligne):
        if (i%2==0):
            for j in range(len(key)):
                decodeText+=matrixDecode.get(j)[i]
        else:
            for j in range(len(key)-1,-1,-1):
                decodeText+=matrixDecode.get(j)[i]
                
    return tempDecodeText,decodeText,matrixDecode

openText=formatOpenText('/home/kali/crypto/text.txt')
print(openText)
openText="путнойперес"
print(generateMatrix(openText))
permEncrypt=permutationEncryption(openText)
print(permEncrypt)
print(decodePermutationEncrypt(permEncrypt[0],permEncrypt[2])[1])
