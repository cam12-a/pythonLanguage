class lab1:
    alphabet="АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    al=[chr(i) for i in range(ord('А'),ord('Я'))]
    print(al)
    def __init__(self,openText):
        self.openText=openText
    def simpleChange(self,openText):
        chiffredText=""
        openText=openText.upper()
        for i in range(len(openText)):
            if(openText[i]==' '):
                chiffredText+=' '
            elif (openText[i]==','):
                chiffredText+=','
            else:
                chiffredText+=self.alphabet[::-1][self.alphabet.find(openText[i])]
        return chiffredText
    def hackSimpleChange(self,cipherText):
        return ""
    def cesar(self,openText,key):
        chiffredText=""
        openText=openText.upper()
        for i in range(len(openText)):
            if(openText[i]==' '):
                chiffredText+=" "
            elif (openText[i]==','):
                chiffredText+=','
            else:
                chiffredText+=self.alphabet[(self.alphabet.find(openText[i])+key)%32]
        return chiffredText
    def polibiya(self,openText):
        chiffredText=""
        openText=openText.upper()
        myPolibiya=[self.alphabet[i:i+6] for i in range(0,len(self.alphabet),6)]
        for i in range(len(openText)):
            if(openText[i]==' '):
                chiffredText+=" "
            elif (openText[i]==','):
                chiffredText+=','
            else:
                if(myPolibiya[5][0]==openText[i]):
                            chiffredText+="61 "
                if(myPolibiya[5][1]==openText[i]):
                    chiffredText+="62 "
                for j in range(5):
                    for k in range(6):
                        if(myPolibiya[j][k]==openText[i]):
                            chiffredText+=str(j+1)+''+str(k+1)+" "
                'chiffredText+=[myPolibiya[j][k].index(openText[i]) for j in range(6)]'
        return chiffredText
    def hackCesar(self,cipherText):
        textToReturn=""
        textArray=[0 for i in range(32)]
        for i in range(3,32):
            for j in range(len(cipherText)):
                if(cipherText[j]==' '):
                    textToReturn+=" "
                elif (cipherText[i]==','):
                    textToReturn+=','
                else:
                    textToReturn+=self.alphabet[(self.alphabet.find(cipherText[j])+i)%32]
            textArray[i]=textToReturn
            textToReturn=""
        return textArray

s=lab1("ddasdaf")
print("Шифр простой замены")
print(s.simpleChange("Тот, кто хочет есть яйца, должен примиться с кудрахтаньем"))
print("Шифр цезаря")
print(s.cesar("Добрались до интересной части Криптоанализ шифра можно, как обычно, разделить на две части: получение первичного ключа с помощью частотного анализа символов и нахождение финального ключа с помощью частотного анализа биграмм Получается, нам нужны идеальные частоты символов и биграмм английского текста Где их добыть, решайте сами Частоты одиночных символов я выгуглил а частоты биграмм собрал самостоятельно по очень большому количеству литературных текстов Так или иначе с этими частотами криптоанализ работает",3))
print("Шифр Полибии")
print(s.polibiya("Тот, кто хочет есть яйца, должен примиться с кудрахтаньем"))
print(s.hackCesar(s.cesar("Добрались до интересной части Криптоанализ шифра можно, как обычно, разделить на две части: получение первичного ключа с помощью частотного анализа символов и нахождение финального ключа с помощью частотного анализа биграмм Получается, нам нужны идеальные частоты символов и биграмм английского текста Где их добыть, решайте сами Частоты одиночных символов я выгуглил а частоты биграмм собрал самостоятельно по очень большому количеству литературных текстов Так или иначе с этими частотами криптоанализ работает",3)))