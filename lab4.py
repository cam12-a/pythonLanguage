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
    opentext = re.sub(r'[^\w\s]', '', opentext)
    opentext=opentext.replace(" ","")
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
        col=factors(len(openText))[0]
        ligne=len(openText)//col
    matrixPermutation=[]
    #print(col,ligne)
    text=""
    for i in range(0,col*ligne,ligne):
        text+=openText[i:i+ligne]+" "
    if isnotdivided==1:
        text+=openText[col*ligne:(col*ligne)+len(openText)%col]+" "
    text=text.split(' ')
    #print(len(text))
    for i in range(len(text)):
        if (i+1)%2!=0:
            matrixPermutation.append(text[i])
        else:
            matrixPermutation.append(text[i][::-1])
    #print(len(matrixPermutation))
    return [isnotdivided, matrixPermutation]
def verifyLenght(openText):
    if len(openText)==1:
        return False
    else:
        return True

def permutationEncryption(openText):
    if not verifyLenght:
        return "Открытый текст слишком короткий"
    matrix=generateMatrix(openText)[1]
    isnotdivided=generateMatrix(openText)[0]
    key=random.sample(range(0,len(matrix[0][:])),len(matrix[0][:]))
    
    ligne=len(matrix[0][:])
    col=len(matrix)
   
    print(ligne,col,key)
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
def decodePermutationEncrypt(textCipher,matrix):
    pass
openText=formatOpenText('/home/kali/crypto/variant.txt')
openText="путнойперестановк"
print(generateMatrix(openText))
print(permutationEncryption(openText))