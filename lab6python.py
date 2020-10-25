import pandas as pd
import numpy as np
from random import sample
def readCsv(fileName):
    return pd.read_csv(fileName,sep=";")

def task1(df):
    dataFr=df.sample(100,random_state=242)
    print(len(dataFr))
    print(dataFr)
    return dataFr.loc[dataFr.tr_description.str.lower().str.contains('плата')].count()[1]/len(dataFr)

def task2(df):
    countTransaction=df.groupby('tr_description').tr_type.nunique()
    L=['Выдача наличных в АТМ Сбербанк России','Комиссия за обслуживание ссудного счета',
    'Списание по требованию ','Оплата услуги. Банкоматы СБ РФ','Погашение кредита (в пределах одного филиала)',
    'Покупка. POS ТУ СБ РФ']
    #TransCheck=countTransaction['tr_type'].apply(lambda x: L in x)
    
    return countTransaction['tr_type']

df=readCsv("C:/Users/camar/OneDrive/Desktop/Master/Crypto/Crypto-master/Crypto-master/tr_types.csv")
#print(df[0:50])
print(task2(df))
#print(task1(df))

#print(f"{task1(df):.2f}")


