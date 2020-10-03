#from tkinter import *
from tkinter import messagebox
from scipy import interpolate
import matplotlib.pyplot as plt
#root=Tk(className="Интерполяционные методы")
x_arr=[-5.6,-4.2,-2.8,-1.4,0,1.4,2.8,4.2,5.6,7,8.4] 
y_arr=[-106,-14,358,397,-100,396,348,-54,-983,-3,1548]

x1=1
a=2
def methods():
    'Интерполяция Лагранжа ..................................'
    b=float(a)
    c=0
    n=len(x_arr)
    L=[1 for i in range(len(x_arr))]
    #L1=[1,1,1,1,1,1,1,1,1,1,1]
    #L2=""
    #C1=""
    #xx="x"
    for i in range(n):
        for j in range(n):
            if(i!=j):
                L[i]=L[i]*(b-x_arr[j])/(x_arr[i]-x_arr[j])
                #L2=L2+' '.join(map(str,[L[i], "*(","x -",x_arr[j] ,")/(",x_arr[i],"-",x_arr[j],")"]))+str("/n")
    for i in range(n):
        c=c+y_arr[i]*L[i]
        #C1=C1+' '.join(map(str,[y_arr[i],"*",L2]))
                        
    #Label(frame1,text=c).pack()
    #Label(frame1,text=C1).pack()
    c=0
    i=x_arr[0]
    i1=0
    L11=[]
    x_arr1=[]
    N1=[]
    SP=[]
    while True:
        x_arr1.insert(i1,i)
        L11.insert(i1,1)
        N1.insert(i1,1)
        SP.insert(i1,1)
        i+=0.1
        i1+=1
        if i>=x_arr[len(x_arr)-1]:break
    i=0
    point=0
    mult=1
    while True:
        c=0
        for i in range(n):
            mult=1.0
            for j in range(n):
                if(i!=j):
                    mult=mult*(x_arr1[point]-x_arr[j])/(x_arr[i]-x_arr[j])
            c=c+y_arr[i]*mult
        #L11[point]=c
        point+=1
        if point==len(x_arr1): break
    'Интерполяция Ньютона ..................................'
    
    f=y_arr[:]
    for j in range(n-1):
        for i in range(n-1,j,-1):
            if i>j:
                f[i]=(f[i]-f[i-1])/(x_arr[i]-x_arr[i-j-1])
                'print("i {}".format(i))'
        'print("j {}".format(j))'
    sum1=0
    i=n-1
    L2=""
    SUM1=""
    while i>=0:
        prod=1
        j=0
        while j<i:
            prod*=(b-x_arr[j])
            j+=1
            L2=L2+'*'.join(map(str,["x-",x_arr[j]]))
        prod*=f[j]
        L2=L2+'*'.join(map(str,[f[j]]))
        sum1=sum1+prod
        SUM1=SUM1+L2
        i-=1
        'print(j," ",f[j]," ",prod," ",sum1)'
    #Label(frame2,text=sum1).pack()
    #Label(frame2,text=SUM1).pack()
    #print(SUM1)
    
    #N=[1 for i in range(len(x_arr))]
    for point in range(len(x_arr1)):
        
        for j in range(n-1):
            for i in range(n-1,j,-1):
                if i>j:
                    f[i]=(f[i]-f[i-1])/(x_arr[i]-x_arr[i-j-1])
                'print("i {}".format(i))'
        'print("j {}".format(j))'
        sum1=0
        i=n-1
        while i>=0:
            prod=1
            j=0
            while j<i:
                prod*=(x_arr1[point]-x_arr[j])
                j+=1
            prod*=f[j]
            sum1=sum1+prod
            N1[point]=sum1
            i-=1
    
    
    'Кубический интерполяция ..................................'
    
    sp=interpolate.splrep(x_arr,y_arr)
    #Label(frame3,text=interpolate.splev(b,sp)).pack()
    for point in range(len(x_arr1)):
        sp=interpolate.splrep(x_arr,y_arr)
        SP[point]=interpolate.splev(x_arr1[point],sp)
    plt.plot(x_arr,y_arr,x_arr1,L11,x_arr1,N1,x_arr1,SP,'--')
    plt.legend(['Исходная функция','Лагранж','Ньютон','Сплайн'],loc='best')
    plt.show()
methods()
'''btn_all=Button(frame4,text="Вычислить",command=methods)
btn_all.pack(padx=10,pady=10)
Label(text="Метод Ньютона").pack()
frame1 = Frame(height=100, bd=0, relief=SUNKEN)
frame1.pack(fill=X, padx=5, pady=5)
Label(text="Метод Лагранжа").pack()
frame2 = Frame(height=100, bd=0, relief=GROOVE)
frame2.pack(fill=X, padx=5, pady=5)
Label(text="Метод Сплайна").pack()
frame3 = Frame(height=100, bd=0, relief=RAISED)
frame3.pack(fill=X, padx=5, pady=5)

root.mainloop()'''
