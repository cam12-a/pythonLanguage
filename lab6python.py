import pandas as pd
import numpy as np
from random import sample
def readCsv(fileName,sep):
    return pd.read_csv(fileName,sep=sep)

def task1(df):
    dataFr=df.sample(100,random_state=242)
    print(len(dataFr))
    print(dataFr)
    return dataFr.loc[dataFr.tr_description.str.lower().str.contains('плата')].count()[1]/len(dataFr)

def task2(df):
    countTransaction=df.groupby(by='tr_description',as_index=False).agg({'tr_type':pd.Series.nunique}).sort_values(by='tr_type',ascending=False)
    return countTransaction

def task3(df):
    maxElement,indexMaxElement=df['amount'].max(),df['amount'].idxmax()
    benefit,perte=0,0
    text=""
    for index,row in df.iterrows():
        if index==indexMaxElement:
            if row['amount']<0:
                perte+=1
            else:
                benefit+=1
    if benefit>perte:
        countItem=benefit
        text="Приход больше"
    else:
        countItem=perte
        text="расход больше"
    #countItem= df['amount'][0:15]
    return [maxElement,indexMaxElement,countItem,text]
#df=readCsv("/home/kali/dataLearg/tr_types.csv",";")
#print(task2(df))
#df=readCsv("/home/kali/dataLearning/transactions.csv",",")
df=pd.read_csv("/home/kali/dataLearning/transactions.csv",sep=",",index_col='customer_id')
print(df)
print(task3(df))
#print(task1(df))

#print(f"{task1(df):.2f}")
