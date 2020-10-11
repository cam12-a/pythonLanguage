import pandas as pd
import numpy as np 
#Задание 1
s=pd.Series(np.linspace(0,20,15))
s1=pd.Series(np.linspace(0,30,15))

s1=s/s.shift(1)

s3=pd.Series([s1[i] for i in range(s1.size) if s1[i]<=1.5]).mean()
s4=s1[s1 <= 1.5].mean()
print(s1)
print(s3,s4)
print(float(s[3])+float(s[5]))
#Задание 3

data = ['1', 2, 3.1, 'hi!', 5, -512, 12.42, 'sber', 10.10, 98]
 
s = pd.Series(data, index=range(2, 12))

try:
    print(float(s[3]) + float(s[5]))
    
except ValueError:
    print('не может быть определён')

a = s[s.apply(lambda x: isinstance(x, int))]
if a.all():
    print(round(np.var(a), 2))
else:
    print('не может быть определён')
#Задания 4
Ss=pd.Series(np.random.normal(1.05,0.1,100))
print(Ss)
Ss=Ss.apply(lambda x: x*x*x)
Sp=pd.Series([Ss[i] for i in range(Ss.size)],index=[i*3 for i in range(0,Ss.size,1)])
print(Sp)
print(Ss)
SUM=0
lessThanZero=0
for i in range(0,300,3):
    if Sp[i]<2.6 and (i*2+1)%2==1:
        lessThanZero+=Sp[i]
    if Sp[i]<0:
        SUM+=1
print(SUM)
print(lessThanZero)