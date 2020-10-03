from scipy import interpolate
import matplotlib.pyplot as plt
import random as rd
import sys as sys
import math as mth
from scipy.signal import argrelextrema
import numpy as np
from sympy import diff,symbols,integrate,Sum,oo
from sympy.solvers import solve
from sympy.abc import k
class interpol:
    #Конструктор
    def __init__(self,x,y,a,b):
        self.x_arr,self.y_arr,self.a,self.b=x,y,a,b
        self.x_arr1=[]
        self.SP=[]
        i=self.x_arr[0] # количество разбиений
        i1=0 #Издекс
        while True:
            self.x_arr1.insert(i1,i)
            self.SP.insert(i1,1)
            i+=0.1
            i1+=1
            if i>=self.x_arr[len(self.x_arr)-1]:break
    #Интерполяция сплайна 
    def spInterpolation(self):
        sp=interpolate.splrep(self.x_arr,self.y_arr)
        #Label(frame3,text=interpolate.splev(b,sp)).pack()
        for point in range(len(self.x_arr1)):
            sp=interpolate.splrep(self.x_arr,self.y_arr)
            self.SP[point]=interpolate.splev(self.x_arr1[point],sp)
        return self.SP
    
    def spInterpolationP(self,a):
        sp=interpolate.splrep(a,self.y_arr)
        sp=interpolate.splev(a,self.y_arr)
        return sp
    #Построение интеполированной функции 
    def drawFn(self):
        Sp=self.spInterpolation()
        plt.plot(self.x_arr,self.y_arr,self.x_arr1,Sp,'--')
        plt.legend(['Исходная функция','Сплайн'],loc='best')
        plt.grid()
        plt.show()
    #Функции для вычисления
    def myFn(self,x):
        return x**4-4*x**2
    #Нахождение нулей функции методом дихотоми в интервале [a b] с точностью epsilon
    def zeroofFunction(self,a,b,epsilon):
        i,c=0,sys.maxsize
        C=set() #Множество решении
        x1,xr=a,b 
        for i in range(round(abs(b-a)/0.1)-1):
            c=sys.maxsize
            try:
                #print("a b ",a,b,i)
                if(self.myFn(a)*self.myFn(b)>0):
                    a=x1+0.1*i
                    b=xr
                while abs(a-b)>=epsilon:
                    c=(a+b)/2
                    if self.myFn(c)*self.myFn(a)>epsilon:
                        a=c
                    else:
                        b=c
                    i+=1
                    if i>100000:break
                if(c!=sys.maxsize and round(self.myFn(c))==0 ):
                    C.add(round(c,2))
                a,b=x1+i*0.1,xr
            except ValueError:
                return ("Функция не определенна в интервал ["+str(x1)+" "+str(xr)+"]")
        if(len(C)==0):
            return ("Уравнение не имеет решение в интервал ["+str(x1)+" "+str(xr)+"]")

        return C
    #нахождение первой производной в точке а      
    def dFn(self,a):
        y=sys.maxsize
        i=a-0.1
        try:
            y=(self.myFn(i)-self.myFn(a))/(i-a)
        except (ValueError, ZeroDivisionError):
            return ("Функция прерывна в точке "+str(a)+" поэтому она не имеет проиводную")
        return round(y)
    #Нахождение точек перегиба
    def sdFn(self,a,b,epsilon):
        x=symbols('x')
        y=diff(diff(self.myFn(x)))
        a=solve(y,x)
       
        return y,a
    #Генерация значение функции для дальнейшего использования
    def generateFunction(self,n):
        y=[]
        for i in range(-n,n):
            try:
                y.append(self.myFn(i))
            except (ValueError, ZeroDivisionError):
                continue
        return y
    #Нахождение локальных минимумов
    def localMin(self,y):
        y=np.array(y)
        return argrelextrema(y,np.less)
    #Нахождение локальных максимумов
    def localMax(self,y):
        y=np.array(y)
        return argrelextrema(y,np.greater)
    #Нахождение площадь кривой между двумя нулями функции
    def area(self):
        x=symbols('x')
        y=self.myFn(x)
        a=solve(y,x)
        if len(a)>=2:
            Integrate=integrate(y,(x,a[0],a[1]))
        return Integrate

        
x_arr=[-5.6,-4.2,-2.8,-1.4,0,1.4,2.8,4.2,5.6,7,8.4] 
y_arr=[-106,-14,358,397,-100,396,348,-54,-983,-3,1548]
s=interpol(x_arr,y_arr,1,2)
y=s.generateFunction(100)
print("Локальные мимимумы x,y")
for i in range(np.size(s.localMin(y_arr))):
    print(x_arr[s.localMin(y_arr)[0][i]]," ",y_arr[s.localMin(y_arr)[0][i]])
print("Локальные максимум x,y")
for i in range(np.size(s.localMax(y_arr))):
    print(x_arr[s.localMax(y_arr)[0][i]]," ",y_arr[s.localMax(y_arr)[0][i]])
print("Вторая производная и точка перегиба ",s.sdFn(1,2,1e-6))
print("Площадь фигуры ",s.area())
print("Нуль функции ",s.zeroofFunction(0,5,1e-9))
#Сумм последовательности
summ=Sum(((-1)**(k-1))/k,(k,1,oo)).doit()
print("Сумма последовательности равна ",summ)
s.drawFn()

#print(s.dFn(0))


