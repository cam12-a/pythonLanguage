import re
class lab2:
    openText=""
    alphabet=[chr(i) for i in range(ord('А'), ord('Я')+1)]
    matrixAlphabet=[[] for i in range(len(alphabet))]
    for i in range(len(alphabet)):
        matrixAlphabet[i]=[chr(j) for j in range(ord('А'), ord('Я')+1)]
    def __init__ (self,openText):
        self.openText=openText.upper()
        self.openText = re.sub(r'[^\w\s]', '', self.openText)
        self.openText=self.openText.replace(" ","")
        #generation table tritemy
        for i in range(len(self.alphabet)):
            for j in range(len(self.alphabet)):
                self.matrixAlphabet[i][j]=self.alphabet[(i+j)%32]
        #print(self.matrixAlphabet)
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
    def belazo(self,key):
        key=key.upper()
        len_key=0
        new_key=""
        textCipher=""
        print(self.openText)
        if(len(self.openText)<len(key)):
            len_key=len(self.openText)
        else:
            for i in range(len(self.openText)):
                new_key+=key[i%len(key)]
            key=new_key
        for i in range(len(self.openText)):
                try:
                    #Recherche de la position des lettres dans le text ouvert et la dans la cle
                    indexOfOpenText=self.alphabet.index(self.openText[i])
                    indexofKey=self.alphabet.index(self.matrixAlphabet[0][self.matrixAlphabet[0].index(key[i])])
                    textCipher+=self.matrixAlphabet[indexOfOpenText][indexofKey]
                    #print(indexofKey, indexOfOpenText)
                except (ValueError):
                    continue
        print(key)
        return textCipher
crypt=lab2('криптография')
print(crypt.tritemy())
print(crypt.belazo('ЗОНД'))