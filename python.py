import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path="/home/onyxia/projet-python/"

def caracteristiques():
    file_name1="caracteristiques_"+"2005"+".csv"
    df= pd.read_csv(path+file_name1, sep=',',low_memory=False)
    for i in range (2006,2023):
        file_name1="caracteristiques_"+str(year)+".csv"
        df2= pd.read_csv(path+file_name1, sep=',',low_memory=False)
        df=pd.concat([df,df2])
        print(i)
    return df

def dataset_per_year(year):
    file_name1="caracteristiques_"+year+".csv"
    df= pd.read_csv(path+file_name1, sep=',',low_memory=False)
    file_name2="lieux_"+year+".csv"
    df2= pd.read_csv(path+file_name2, sep=',',low_memory=False) 
    df=pd.merge(df,df2,on='Num_Acc')
    file_name3="usagers_"+year+".csv"
    df2= pd.read_csv(path+file_name3, sep=',',low_memory=False)
    if int(year)<2019:
        df2['grav'] = df2['grav'].replace({2: 4, 4: 2})
        df2['grav'] = df2['grav'].replace({'2': 4, '4': 2})
    grav_df = df2.groupby('Num_Acc')['grav'].max().reset_index()
    df=pd.merge(df,grav_df,on='Num_Acc')
    df=df.drop_duplicates()
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
df['catr'] = pd.to_numeric(df['catr'], errors='coerce')
df['grav'] = df['grav'].replace({'1':1,'2':2,'3':3,'4':4})

"""
graph_df = df.groupby(['grav', 'catr']).size().reset_index(name='accident_count')
graph_df = graph_df.pivot(index='grav', columns='catr', values='accident_count')

# Plot the lines for each gravity type
plt.figure(figsize=(10, 6))

for gravity_type in graph_df.index:
    plt.plot(graph_df.columns, graph_df.loc[gravity_type], label=f'Gravity {gravity_type}')

plt.xlabel('Type of Road (catr)')
plt.ylabel('Number of Accidents')
plt.title('Number of Accidents for Each Type of Road by Gravity Type')
plt.legend()
plt.show()
"""

num_rows = len(df)
midpoint = num_rows // 2
df_part1 = df.iloc[:midpoint]
df_part2 = df.iloc[midpoint:]

df_part1.to_csv(path+'dataset_complet_part_1.csv', index=False)
df_part2.to_csv(path+'dataset_complet_part_2.csv', index=False)

print((df.isna().mean() * 100).round(2))





