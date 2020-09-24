import re
from random import randint
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
def evenNumber(number):
	a=[]
	for i in range(number):
		if(i%2==0):
			a.append(i)
	return a
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
def changePlace(ListLen):
	L=[randint(-ListLen,ListLen) for i in range(ListLen)]
	print("generated List ",L)
	maxL,minL=max(L),min(L)
	maxIndex,minIndex=L.index(maxL),L.index(minL)
	L[maxIndex],L[minIndex]=minL,maxL
	return L
def getDict():
	text=input()
	d={}
	index=0
	T=[]
	for i in range(len(text)):
		x=re.findall("[()`{|}',' ':]",text[i])
		if not x:
			T.append(text[i])
			index+=1
	d={T[i]:T[i+1] for i in range(index-1)}
	print(type(d))
	return d
def printDict():
	d={}
	d,key=dict(input()),int(input())
	print(type(d))
	return d[key]
print(evenNumber(15))
print(isStrongPassword("мАар21."))
print(biggerThan(5))
print(changePlace(15))
print(getDict())
