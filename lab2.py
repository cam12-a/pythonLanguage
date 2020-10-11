import re
from random import randint
import io
class lab2:
    openText=""
    data=""
    alphabet=[chr(i) for i in range(ord('А'), ord('Я')+1)]
    matrixAlphabet=[[] for i in range(len(alphabet))]
    for i in range(len(alphabet)):
        matrixAlphabet[i]=[chr(j) for j in range(ord('А'), ord('Я')+1)]
    def __init__ (self,fileName):
        with io.open(fileName, 'r',encoding="UTF-8") as file:
            self.openText = file.read().replace('\n', '')
        self.openText=self.openText.upper()
        self.openText = re.sub(r'[^\w\s]', '', self.openText)
        self.openText=self.openText.replace(" ","")
        print("Открытый текст "+self.openText)
        #generation table tritemy
        for i in range(len(self.alphabet)):
            for j in range(len(self.alphabet)):
                self.matrixAlphabet[i][j]=self.alphabet[(i+j)%32]
        #print(self.matrixAlphabet)
    #def opentext(self)
    def tritemy(self):
        textCipher=""
        for i in range(len(self.openText)):
            if(self.openText[i]==' '):
                textCipher+=" "
            elif self.openText[i]==',':
                textCipher+=","
            else:
                'print(self.openText[i],i+1, self.alphabet.index(self.openText[i])+1,(i+1+self.alphabet.index(self.openText[i]))%32)'
                textCipher+=self.alphabet[(i+self.alphabet.index(self.openText[i]))%32]
        return textCipher
    def pwdBelazo(self,key):
        key=key.upper()
        vueMatrix=""
        for i in range(32):
            vueMatrix+=self.alphabet[i]+" "
        vueMatrix+="\n"
        for i in range(len(key)):
            for j in range(self.alphabet.index(key[i]),32+self.alphabet.index(key[i])):
                vueMatrix+=self.alphabet[j%32]+' '
            vueMatrix+="\n"
        return vueMatrix
    def belazo(self,key):
        key=key.upper()        
        key=self.normalizeKey(key)
        textCipher=""
      
        
        for i in range(len(self.openText)):
                try:
                    #Recherche de la position des lettres dans le text ouvert et la dans la cle
                    indexOfOpenText=self.alphabet.index(self.openText[i])
                    indexofKey=self.alphabet.index(self.matrixAlphabet[0][self.matrixAlphabet[0].index(key[i])])
                    textCipher+=self.matrixAlphabet[indexOfOpenText][indexofKey]

                    #print(self.alphabet[indexofKey], self.alphabet[indexOfOpenText])
                except (ValueError):
                    continue
        return [self.openText,key,textCipher]
    def vigener(self,key):
        key=key+self.openText
        key=self.normalizeKey(key)
        key=key.upper()
        #print("Ключ Виженера",key)
        textCipher=""
        for i in range(len(self.openText)):
            #print(self.alphabet.index(key[i]),self.alphabet.index(self.openText[i]))
            textCipher+=self.alphabet[(self.alphabet.index(key[i])+self.alphabet.index(self.openText[i]))%32]
        return [key,textCipher]
    def normalizeKey(self,key):
        len_key=0
        new_key=""
        if(len(self.openText)<len(key)):
            len_key=len(self.openText)
        else:
            for i in range(len(self.openText)):
                new_key+=key[i%len(key)]
            key=new_key
        return key
    def descriptBelazo(self,textCipher,key):
        textOrigine=""
        key=self.normalizeKey(key)
        key=key.upper()
        textCipher=textCipher.upper()
        for i in range(len(textCipher)):
            textOrigine+=self.alphabet[(self.alphabet.index(textCipher[i])-self.alphabet.index(key[i]))%32]
        return textOrigine
    def decodeTextTritemy(self,textCipher):
        textOrigin=""
        textCipher=textCipher.upper()
        for i in range(len(textCipher)):
            textOrigin+=self.alphabet[(self.alphabet.index(textCipher[i])-i)%32]
        return textOrigin
    def decodeVegener(self,textCipher,key):
        textOrigine=""
        key+=self.openText
        key=self.normalizeKey(key)
        key=key.upper()
        textCipher=textCipher.upper()
        for i in range(len(textCipher)):
            textOrigine+=self.alphabet[(self.alphabet.index(textCipher[i])-self.alphabet.index(key[i]))%32]
        return textOrigine
    def encodeVegenere(self,key):
        key=self.openText
        gama=self.vigener(key)
        textCipher=""
        for i in range(len(self.openText)):
            textCipher+=self.alphabet[(self.alphabet.index(gama[i])-self.alphabet.index(self.openText[i]))%32]
        return textCipher

crypt=lab2('/home/kali/crypto/text.txt')
key=[chr(i) for i in range(ord('А'), ord('Я')+1)][randint(0,31)]
belazo=crypt.belazo('ЗОНД')
print("Шифр Тритемии "+crypt.tritemy())
print("Разшировка Третемии "+crypt.decodeTextTritemy(crypt.tritemy()))
print("Открытый текст \n",belazo[0])
print("Ключ Белоза: ЗОНД дополняем до длины открытого текста получаем:\n",belazo[1])
print("Пароль Белоза(Матрица шифрования) \n"+crypt.pwdBelazo('ЗОНД'))
print("Шифр Белоза "+belazo[2])
print("Разшировка Белоза "+crypt.descriptBelazo(belazo[2],'ЗОНД'))
vigener=crypt.vigener(key)
print("Ключ Вижинера"+vigener[0])
print("Шифр Вижинера "+vigener[1])
print("Origine text vegenere "+crypt.decodeVegener(vigener[1],key))



