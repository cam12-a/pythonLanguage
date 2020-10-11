from io import open
from re import sub
import base64
class DES:
    def __init__(self,fileName):
        self.openText=fileName
        with open(fileName, 'r',encoding="UTF-8") as file:
            self.openText = file.read().replace('\n', '')
        self.openText = sub(r'[^\w\s]', '', self.openText)
        self.opentext=self.openText.replace(" ","")

    def openTextToBlock64(self):
        return [self.openText[i:i+64] for i in range(0,len(self.openText),64)]

    def textToByte(self):
        return bytes(self.openText,encoding="UTF-8")

    def Block64ToTwoBlockOf32(self,text64Block):
        #Если длина некротна 64 дополняем сторку с # до 64 символов 
        if len(text64Block)%64!=0:
            for i in range(len(text64Block),64,1):
                text64Block+='#'
        return [text64Block[0:31],text64Block[32:63]]
    
    

Des=DES("/home/kali/crypto/text.txt")
textToBlock64=Des.openTextToBlock64()
print(textToBlock64)
print(bytes(textToBlock64[0],encoding="UTF-8"))
print(base64.encodestring(textToBlock64[0]).strip())