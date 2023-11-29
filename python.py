import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path="/home/onyxia/work/projet-python/"


def dataset_per_year(year):
    file_name1="caracteristiques_"+year+".csv"
    df= pd.read_csv(path+file_name1, sep=';')
    file_name2="lieux_"+year+".csv"
    df2= pd.read_csv(path+file_name2, sep=';',low_memory=False) 
    df=pd.concat([df,df2],axis=1)
    file_name3="usagers_"+year+".csv"

    file_name4="vehicules_"+year+".csv"

    return df

def complete_dataset():
    df=dataset_per_year("2005")
    for i in range (2006,2023):
        df=pd.concat([df,dataset_per_year(str(i))])
    return df


df_2022=dataset_per_year("2022")
df_2021=dataset_per_year("2021")
df_2020=dataset_per_year("2020")
df_2019=dataset_per_year("2019")
print(df_2022.columns)
print(df_2021.columns)
print(df_2019.columns)














