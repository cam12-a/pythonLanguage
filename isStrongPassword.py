import re
from random import randint
import random
import string
import io
#Сильный пароль
def isStrongPassword(textToVerify):
	x=re.findall("[а-я]", textToVerify)
	y=re.findall("[А-Я]",textToVerify)
	z=re.findall("[0-9]",textToVerify)
	t=re.findall("['!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~']",textToVerify)
	b=0
	textToReturn=""
	if x:
		b+=1
	if y:
		b+=1
	if z:
		b+=1
	if t:
		b+=1
	if b==4:
		textToReturn="Strong password"
	elif b>1 and b<=3:
		textToReturn="medium password"
	else:
		textToReturn="Low password"
	return textToReturn
#Задание 1 вывод четных индексов
def evenNumber(number):
	a=[]
	for i in range(number):
		if(i%2==0):
			a.append(i)
	return a
#Задание 2 вывод всех элементов больше предыдущего
def biggerThan(ListLen):
	L=[randint(-ListLen,ListLen) for i in range(ListLen)]
	print("generated List ",L)
	returnList=[]
	for i in range(ListLen-1):
		if(L[i]<L[i+1]):
			returnList.append(L[i+1])
	if(L[len(L)-2]<L[len(L)-1]):
		L.append(L[len(L)-1])
	return returnList
#Задание 3 swap макс. и мин.
def changePlace(ListLen):
	L=[randint(-ListLen,ListLen) for i in range(ListLen)]
	print("generated List ",L)
	maxL,minL=max(L),min(L)
	maxIndex,minIndex=L.index(maxL),L.index(minL)
	L[maxIndex],L[minIndex]=minL,maxL
	return L
#Задание 1 вывод значения по ключу
def returnValueByKey(lenDict,key):
	d={i: randint(-lenDict,lenDict) for i in range(lenDict)}
	print("Возвращать Ключ словарь, исход. слов. \n",d)
	try:
		a=d[key]
	except:
		a="нет такого ключа"
	return a
#Задание 2 поиск по значению и вывод ключа
def returnKeyByValue(lenDict,val):
	d={i:randint(-lenDict,lenDict) for i in range(lenDict)}
	Nwd={}
	print("Возвращать значение по ключу, исход. слов. \n",d)
	for i in range(lenDict):
		if val==d[i]:
			try:
				Nwd.update({i:d[i]})
			except:
				continue
	return Nwd
#Задание 3 количество построк
def countStr(strNumberToGenerate,strTocount):
	strTocount=strTocount.lower()
	alphabet=[chr(i) for i in range(ord('а'),ord('я'))]
	mystr=[''.join(alphabet[randint(2,strNumberToGenerate)%32] for j in range(strNumberToGenerate)) for i in range(strNumberToGenerate)]
	print(mystr)
	count=0
	for i in range(strNumberToGenerate):
		if mystr[i]==strTocount:
			count+=1
	return count
#Задание 1 количество встречающих различных чисел
def returnMatchElementFromList(lenList):
	L=[randint(-lenList,lenList) for i in range(lenList)]
	myset=set()
	for i in range(lenList):myset.add(L[i])
	print("Список ",L ,"\n множество ",myset)
	return len(myset)
#Задание 2 объединение множеств
def UnionOfList(lenList1,lenList2):
	L1,L2=[randint(-lenList1,lenList1) for i in range(lenList1)],[randint(-lenList2,lenList2) for i in range(lenList2)]
	myset1,myset2=set(),set()
	for i in range(lenList1):myset1.add(L1[i])
	for j in range(lenList2):myset2.add(L2[j])
	print("set1 {} set2 {}".format(myset1,myset2))
	if len(myset1)>=len(myset2):
		return myset1.intersection(myset2) 
	else:
		return myset2.intersection(myset1)
# Задание 3: поиск подмножеств
def isSubSet(lenSet1,lenSet2):
	myset1={randint(-lenSet1,lenSet1) for i in range(lenSet1)}
	myset2={randint(-lenSet2,lenSet2) for i in range(lenSet2)}
	if(myset1.issubset(myset2) or myset2.issubset(myset1)):
		if (len(myset1)>len(myset2)):return str(myset2)+" является подмножеством множество "+str(myset1)
		else: return str(myset1)+" является подмножеством множество "+str(myset2)
	else:
		return str(myset2) +" и "+str(myset1)+" не являются подмножествамы"
#Работа с файлами
def fileTask(fileName):
	fileContent=""
	tempData=""
	with io.open(fileName,'r',encoding='UTF-8') as data:
		fileContent=data.read()
	data.close()
	data=fileContent[34:].split('\n')
	for i in range(len(data)-1):
		if(data[i][:].split(',')[1]!=" " and data[i][:].split(',')[2]!=" "):
			if (data[i][:].split(',')[3]!=" "):
				#print(email_gen([[data[i][:].split(',')[1].replace(" ", ""),data[i][:].split(',')[2].replace(" ", "")]])[0])
				tempData+=email_gen([[data[i][:].split(',')[1].replace(" ", ""),data[i][:].split(',')[2].replace(" ", "")]])[0]+data[i][:]+"\n"
			else:
				tempData+=" "+data[i][:]+"\n"
		else:
			tempData+=data[i][:]+"\n"
	data=open(fileName+"1","w")
	data.write(tempData)
def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter+=1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails

print("Четные индексы", evenNumber(15))
print("Сильна пароли ",isStrongPassword("мАар21."))
print("Элементы больше предыдущего ",biggerThan(5))
print("Менять местами мин. и макс. элем. ",changePlace(15))
print("Значение ",returnValueByKey(15,16))
print("Ключ ",returnKeyByValue(15,1))
print("Количсество повторяющих строк ",countStr(12,'звкивекежгзй'))
print("Количество встречающих различных чисел",returnMatchElementFromList(12))
print("Пересечения ",UnionOfList(5,6))
print(isSubSet(5,2))
fileTask('task_file.txt')