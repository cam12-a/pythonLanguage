import re
def isStrongPassword(textToVerify):
	x=re.findall("[а-я]", textToVerify)
	y=re.findall("[А-Я]",textToVerify)
	z=re.findall("[0-9]",textToVerify)
	t=re.findall("['!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~']",textToVerify)
	b=0
	if x:
		b+=1
	if y:
		b+=1
	if z:
		b+=1
	if t:
		b+=1
	if b==4:
		print("Strong password")
	elif b>1 and b<=3:
		print("medium password")
	else:
		print("Low password")
isStrongPassword("мар21.")