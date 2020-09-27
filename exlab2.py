import re
class exlab2:
    openText=""
    alphabet=[chr(i) for i in range(ord('А'), ord('Я')+1)]
    def __init__ (self,openText):
        self.openText=openText.upper()
        self.openText = re.sub(r'[^\w\s]', '', self.openText)
        self.openText=self.openText.replace(" ","")
        print(self.openText)
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
    def vigenera(self,key):
        textCipher=""
        key *= len(self.openText) // len(key) + 1
        for i in range(len(self.openText)):
            if(self.openText[i]==' '):
                textCipher+=" "
            elif self.openText[i]==',':
                textCipher+=","
            else:
               textCipher = ''.join([chr((ord(chplain) + ord(key[indx])) % 32 + ord('а')) for indx, chplain in enumerate(self.openText)])
                
        return textCipher
crypt=exlab2("Дом мой, как бы мал ты ни был, ты мне кажешься аббатством.")
print(crypt.tritemy())

print("\n")
print(crypt.vigenera('СУП'))