import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path="/home/onyxia/work/projet-python/"


def dataset_per_year(year):
    file_name1="carcteristiques-"+year+".csv"
    df= pd.read_csv(path+file_name1, sep=';')
    file_name2="lieux-"+year+".csv"
    df2= pd.read_csv(path+file_name2, sep=';',low_memory=False) 
    df=pd.concat([df,df2],axis=1)
    file_name3="usagers-"+year+".csv"

    file_name4="vehicules-"+year+".csv"

    return df

df_2022=dataset_per_year("2022")

def accidents_per_month(df):
    res=[0 for i in range (12)]
    for i in range (1,13):
        res[i-1]= df.loc[df.mois == '0'+str(i) , 'mois'].count()
    return res

plt.plot([i for i in range (1,13)],accidents_per_month(df_2022))
plt.show()














