import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
def readCsv(fileName,sep):
    return pd.read_csv(fileName,sep=sep)
bank=readCsv('C:/Users/camar/OneDrive/Desktop/Master/Crypto/Crypto-master/Crypto-master/bank-full.csv',';')
def deleteToTestAndTarget():
    y=bank['y']
    y.replace(['no','yes'],[0,1],inplace=True)
    y=y[0:len(bank)//2]
    yTest=y[len(bank)//2:len(bank)]
    x=bank.drop(columns=['y'])
    x=x[0:len(bank)//2]
    xTest=x[len(bank)//2:len(bank)]

    return [x,xTest,y,yTest]
def lenearModel(x,xTest,y,yTest):
    model=LinearRegression()
    model.fit(xTest,yTest)
    model.score(x,y)
    predict=model.predict(x)
    return predict

myModel=deleteToTestAndTarget()
#deapLearning=lenearModel(myModel[0],myModel[1],myModel[2],myModel[3])
print(myModel[0].nunique())
#plt.plot(myModel[0:100],myModel[0:100])
#print(myModel[2:100])
#print(y[0:5])



    
