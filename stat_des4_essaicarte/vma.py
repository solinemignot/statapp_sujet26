import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

#Premièrement, fixons les vmas qui sont mal renseignées
path="/home/onyxia/statapp_sujet26/"
file_name1="dataset_complet_part_1.csv"
file_name2="dataset_complet_part_2.csv"
df1= pd.read_csv(path+file_name1, sep=',',low_memory=False)
df2= pd.read_csv(path+file_name2, sep=',',low_memory=False)
df=pd.concat([df1,df2])
df['grav'] = df['grav'].replace({'1':1,'2':2,'3':3,'4':4})
df=df[df['grav']!='grav']
df['grav']=df['grav'].replace({1: 0, 2: 0, 3: 1, 4: 1})

print(df['vma'].isna().sum())

df['vma']=df['vma'].replace({1.:10, 2.:20 , 3.:30, 4.:40,5.:50,6.:60,7.:70,8.:80,9.:90,500:50,12:120,560:-1,700:70,800:80,600:60,300:30,900:90,520:50,901:90,501:50,502:50,770:70,42:-1,0:-1,140:-1,180:-1})
df['vma']=df['vma'].replace({15:20,25:30,45:50,55:50,65:70,75:80,35:30,120:110 })

#rafistolons pour le reste grâce aux identifiants de route

df_recents = df[df['an'].isin([2019, 2020, 2021, 2022])]
df_recents = df_recents[['dep','catr','voie','vma']]

df = df.drop('vma', axis=1)
df = pd.merge(df, df_recents, on=['voie'],how='left')
print(df['vma'].isna().sum())
print(df.head(50))




"""
path="/home/onyxia/statapp_sujet26/"
file_name1="dataset_complet_part_1.csv"
file_name2="dataset_complet_part_2.csv"
df1= pd.read_csv(path+file_name1, sep=',',low_memory=False)
df2= pd.read_csv(path+file_name2, sep=',',low_memory=False)
df=pd.concat([df1,df2])
df['grav'] = df['grav'].replace({'1':1,'2':2,'3':3,'4':4})
df=df[df['grav']!='grav']
df['grav']=df['grav'].replace({1: 0, 2: 0, 3: 1, 4: 1})

def dataset_per_year(year):
    file_name_characteristics = f"caracteristiques_{year}.csv"
    df_characteristics = pd.read_csv(path + file_name_characteristics, sep=',', low_memory=False)

    file_name_locations = f"lieux_{year}.csv"
    df_locations = pd.read_csv(path + file_name_locations, sep=',', low_memory=False)
    df = pd.merge(df_characteristics, df_locations, on='Num_Acc')

    file_name_users = f"usagers_{year}.csv"
    df_users = pd.read_csv(path + file_name_users, sep=',', low_memory=False)
    df_users = df_users[df_users['grav'] != 'grav']

    if int(year) < 2019:
        df_users['grav'] = df_users['grav'].replace({2: 4, 4: 2, '2': 4, '4': 2, '1': 1, '3': 3}).infer_objects(copy=False)
        df_users['grav'] = pd.to_numeric(df_users['grav'], errors='coerce')  # Convert to numeric
    if int(year)>2018:
        df_users['grav'] = df_users['grav'].replace({'4': 4, '2': 2, '1': 1, '3': 3}).infer_objects(copy=False)
        df_users['grav'] = df_users['grav'].replace({2: 4, 4: 2})
        df_users['grav'] = pd.to_numeric(df_users['grav'], errors='coerce')  # Convert to numeric

    grav_df = df_users.groupby('Num_Acc')['grav'].max().reset_index()
    df = pd.merge(df, grav_df, on='Num_Acc')
    df = df.drop_duplicates()

    return df

df_2019 = dataset_per_year(2019)
df_2019 = df_2019[['dep','voie','vma']]
print(df_2019.head(5))

df_2005 = dataset_per_year(2005)
print(df_2019['vma'].isna().sum())
"""
