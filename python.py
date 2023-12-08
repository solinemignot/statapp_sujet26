import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path="/home/onyxia/work/projet-python/"


def dataset_per_year(year):
    file_name1="caracteristiques_"+year+".csv"
    df= pd.read_csv(path+file_name1, sep=',',low_memory=False)
    file_name2="lieux_"+year+".csv"
    df2= pd.read_csv(path+file_name2, sep=',',low_memory=False) 
    df=pd.merge(df,df2,on='Num_Acc')
    file_name3="usagers_"+year+".csv"

    file_name4="vehicules_"+year+".csv"

    return df

def complete_dataset():
    df=dataset_per_year("2005")
    for i in range (2006,2019):
        df=pd.concat([df,dataset_per_year(str(i))])
        print(i)
    df=df.drop('env1',axis=1)
    for i in range (2019,2023):
        df=pd.concat([df,dataset_per_year(str(i))])
        print(i)
    return df



df=complete_dataset()
print(df.head(10))





