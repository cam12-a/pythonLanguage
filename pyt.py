import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import random
def readCsv(fileName,sep):
    return pd.read_csv(fileName,sep=sep)
bank=readCsv('C:/Users/camar/OneDrive/Desktop/Master/Crypto/Crypto-master/Crypto-master/bank-full.csv',';')
def deleteToTestAndTarget():
    Y=bank['y']
    x=bank.drop(columns=['y'])
    xTrain,xTest,yTrain,yTest=train_test_split(x,Y,test_size=0.2,random_state=100000)
    xTrain=xTrain.drop(columns=['job','marital','education','contact','poutcome','month'])
    xTrain.replace(['no','yes','nan'],[0,1,''],inplace=True)  
    xTest=xTest.drop(columns=['job','marital','education','contact','poutcome','month'])
    '''xTrain=x.drop(columns=['job','marital','education','contact','poutcome','month'])
    xTest=x.drop(columns=['job','marital','education','contact','poutcome','month'])
    xTest.replace(['no','yes','nan'],[0,1,''],inplace=True)  
    yTrain=Y
    yTrain.replace(['no','yes'],[0,1],inplace=True)
    yTest=Y.replace(['no','yes'],[0,1],inplace=True)'''
    yTrain.replace(['no','yes'],[0,1],inplace=True)
    xTest.replace(['no','yes','nan'],[0,1,''],inplace=True)
    yTest.replace(['no','yes'],[0,1],inplace=True)
    #print("xTrain ",xTrain)
    #y.replace(['no','yes'],[0,1],inplace=True) #Заменим все no и yes на 0 и 1
    #y=y[0:len(bank)//2]
    #yTest=y[len(bank)//2:len(bank)]
    #yTest=yTest['y']
    #x=bank.drop(columns=['y'])
    #x=x.drop(columns=['y'])
    x.replace(np.nan,' ',inplace=True) #удаление всех nan
    #xTest=xTest.drop(columns=['y'])
    # для обучение нам необходимо все строковые значения заменить на числовые
    '''x['duration'].apply(lambda x:float(x))
    x['campaign'].apply(lambda x:float(x))
    x['pdays'].apply(lambda x:float(x))
    x['previous'].apply(lambda x:float(x))
    x['age'].apply(lambda x:float(x))
    x['day'].apply(lambda x:float(x))
    x['balance'].apply(lambda x:float(x))'''
   
    #x=x.nunique()
    #x=x[0:len(bank)//2]
    #xTest=x[len(bank)//2:len(bank)]

    return [xTrain,xTest,yTrain,yTest]
def lenearModel(xTrain,yTrain,xTest,yTest):
    '''model=LinearRegression()
    model.fit(xTest,yTest)
    model.score(x,y)
    predict=model.predict(x)
    return predict'''
    model=KNeighborsClassifier(n_neighbors=3)
    #model=LinearRegression()
    model.fit(xTrain,yTrain)
    scp=model.score(xTrain,yTrain)
    pre= model.predict(xTest)
    print("Train ",scp )
    print("Средняя ош\n",np.abs(pre-yTest))
    testModel(model)
    #print("Train ",model.score(xTrain,yTrain))
    #print("Text ",model.score(xTest,yTest))

def testModel(model,age=70,default=0,balance=4572,housing=0,loan=0,day=11,duration=115,compaign=2,pdays=95,previous=16):
    individual=np.array([age,default,balance,housing,loan,day,duration,compaign,pdays,previous]).reshape(1,10)
    print(model.predict(individual))
    #print(model.predict_proba(individual))

myModel=deleteToTestAndTarget()
lenearModel(myModel[0],myModel[2],myModel[1],myModel[3])

#print(myModel[0])
#print(myModel[0]['job'].unique())
#plt.plot(myModel[0:100],myModel[0:100])
#print(myModel[2:100])
#print(y[0:5])



    
