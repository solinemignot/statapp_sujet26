"""import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

path="/home/onyxia/work/statapp_sujet26/"
file_name1="dataset_complet_part_1.csv"
file_name2="dataset_complet_part_2.csv"
df1= pd.read_csv(path+file_name1, sep=',',low_memory=False)
df2= pd.read_csv(path+file_name2, sep=',',low_memory=False)
df=pd.concat([df1,df2])
df['grav'] = df['grav'].replace({'1':1,'2':2,'3':3,'4':4})
df=df[df['grav']!='grav']


# Graphique selon le type de route

df = df[df['catr'] < 5]
df=df.sort_values(by='catr')
df['catr'] = df['catr'].replace({1: 'Autoroute', 3: 'Route Nationale',2:'Route Départementale',4:'Voie communale'})
graph_df = df.groupby(['grav', 'catr']).size().reset_index(name='accident_count')
graph_df = graph_df.pivot(index='grav', columns='catr', values='accident_count')
graph_df = graph_df.transpose()

plt.figure(figsize=(10, 6))
for gravity_type in graph_df.index:
    plt.plot(graph_df.columns, graph_df.loc[gravity_type], label=f'Gravity {gravity_type}')

ax=graph_df.plot(kind='bar', stacked=False, figsize=(10, 6))
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)

plt.xlabel('Type de route')
plt.ylabel('Nombre d accidents')
plt.title('Nombre d accidents par type de route selon la gravité')
plt.legend()
plt.savefig(path+'soline/'+'type de route.png')
plt.show()


#Graphique selon la vitesse max de la route - Useless car trop de valeurs non renseignées
df = df[df['vma'].notna()]
allowed_values = ['30', '50', '70', '80', '90', '110', '130']
df.drop(df[~df['vma'].isin(allowed_values)].index, inplace=True)
df['vma']=df['vma'].replace({'30':30,'50':50,'70':70,'80':80,'90':90,'110':110,'130':130})


graph_df = df.groupby(['grav', 'vma']).size().reset_index(name='accident_count')
graph_df = graph_df.pivot(index='grav', columns='vma', values='accident_count')
graph_df = graph_df.transpose()

plt.figure(figsize=(10, 6))
for gravity_type in graph_df.index:
    plt.plot(graph_df.columns, graph_df.loc[gravity_type], label=f'Gravity {gravity_type}')

ax=graph_df.plot(kind='bar', stacked=False, figsize=(10, 6))

plt.xlabel('Vitesse max de la route')
plt.ylabel('Nombre d accidents')
plt.title('Nombre d accidents selon la vitesse max de la route ')
plt.legend()
plt.savefig(path+'soline/'+'vitesse max.png')
plt.show()

# En agglomération ou hors?

df['agg'] = df['agg'].astype(float)
df = df[df['agg'].notna()]
graph_df = df.groupby(['grav', 'agg']).size().reset_index(name='accident_count')
graph_df = graph_df.pivot(index='grav', columns='agg', values='accident_count')

graph_df = graph_df.transpose()
ax=graph_df.plot(kind='bar', stacked=True, figsize=(10, 6))

ax.set_xticks(range(len(graph_df.index)))
ax.set_xticklabels(['Hors agglomération', 'En agglomération'], rotation=0)
plt.ylabel('Nombre d accidents')
ax.set_xlabel('')
plt.title('Nombre d accidents selon si c était en agglomération ou non')
plt.legend()
plt.savefig(path+'soline/'+'agg.png')
plt.show()
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

path="/home/onyxia/work/statapp_sujet26/"
file_name1="dataset_complet_part_1.csv"
file_name2="dataset_complet_part_2.csv"
df1= pd.read_csv(path+file_name1, sep=',',low_memory=False)
df2= pd.read_csv(path+file_name2, sep=',',low_memory=False)
df=pd.concat([df1,df2])
df['grav'] = df['grav'].replace({'1': 0, '2': 0, '3': 1, '4': 1,1: 0, 2: 0, 3: 1, 4: 1}).astype(int)
df = df[ df['an']== 2019]

# Graphique selon le type de route

df = df[df['catr'] < 5]
df=df.sort_values(by='catr')
df['catr'] = df['catr'].replace({1: 'Autoroute', 3: 'Route Nationale',2:'Route Départementale',4:'Voie communale'})
graph_df = df.groupby(['grav', 'catr']).size().reset_index(name='accident_count')
graph_df = graph_df.pivot(index='grav', columns='catr', values='accident_count')
graph_df = graph_df.transpose()


plt.figure(figsize=(10, 6))
for gravity_type in graph_df.index:
    plt.plot(graph_df.columns, graph_df.loc[gravity_type], label=f'Gravity {gravity_type}')

ax=graph_df.plot(kind='bar', stacked=False, figsize=(10, 6))
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)

plt.xlabel('Type de route')
plt.ylabel('Nombre d accidents')
plt.title('Nombre d accidents par type de route selon la gravité')
plt.legend()
plt.savefig(path+'stat_des3/'+'type de route 2019.png')
plt.show()

#Vitesse max
df=pd.concat([df1,df2])
df['grav'] = df['grav'].replace({'1': 0, '2': 0, '3': 1, '4': 1,1: 0, 2: 0, 3: 1, 4: 1}).astype(int)
df = df[ df['an']== 2019]
df['vma']=df['vma'].replace({1.:10, 2.:20 , 3.:30, 4.:40,5.:50,6.:60,7.:70,8.:80,9.:90,500:50,12:120,560:-1,700:70,800:80,600:60,300:30,900:90,520:50,901:90,501:50,502:50,770:70,42:-1,0:-1,140:-1,180:-1})
df['vma']=df['vma'].replace({15:20,25:30,45:50,55:50,65:70,75:80,35:30,120:110 })
df['vma']=df['vma'].replace({10:-1, 20:-1,40:-1,60:-1,100:-1})
df = df[ df['vma']!= -1]

graph_df = df.groupby(['grav', 'vma']).size().reset_index(name='accident_count')
graph_df = graph_df.pivot(index='grav', columns='vma', values='accident_count')
graph_df = graph_df.transpose()

print(graph_df)

percentage_grav0= [round(graph_df.loc[i,0]/(graph_df.loc[i,0]+graph_df.loc[i,1])*100,2) for i in [30.0,50.0,70.0,80.0,90.0,110.0,130.0]]
percentage_grav1= [round(graph_df.loc[i,1]/(graph_df.loc[i,0]+graph_df.loc[i,1])*100,2) for i in [30.0,50.0,70.0,80.0,90.0,110.0,130.0]]

print(percentage_grav0)
print(percentage_grav1)

plt.figure(figsize=(10, 6))
for gravity_type in graph_df.index:
    plt.plot(graph_df.columns, graph_df.loc[gravity_type], label=f'Gravity {gravity_type}')

ax=graph_df.plot(kind='bar', stacked=False, figsize=(10, 6))

plt.xlabel('Vitesse max de la route')
plt.ylabel('Nombre d accidents')
plt.title('Nombre d accidents selon la vitesse max de la route ')
plt.legend()

"""i = 0
for p in graph:
    width = p.get_width()
    height = p.get_height()
    x, y = p.get_xy()
    plt.text(x+width/2,
             y+height*1.01,
             str(data.Percentage[i])+'%',
             ha='center',
             weight='bold')
    i+=1"""



plt.savefig(path+'stat_des3/'+'vitesse max 2019.png')

#Agglomération?
df=pd.concat([df1,df2])
df['grav'] = df['grav'].replace({'1': 0, '2': 0, '3': 1, '4': 1,1: 0, 2: 0, 3: 1, 4: 1}).astype(int)
df = df[ df['an']== 2019]

df['agg'] = df['agg'].astype(float)
df = df[df['agg'].notna()]
graph_df = df.groupby(['grav', 'agg']).size().reset_index(name='accident_count')
graph_df = graph_df.pivot(index='grav', columns='agg', values='accident_count')

graph_df = graph_df.transpose()
ax=graph_df.plot(kind='bar', stacked=True, figsize=(10, 6))

ax.set_xticks(range(len(graph_df.index)))
ax.set_xticklabels(['Hors agglomération', 'En agglomération'], rotation=0)
plt.ylabel('Nombre d accidents')
ax.set_xlabel('')
plt.title('Nombre d accidents selon si c était en agglomération ou non')
plt.legend()
plt.savefig(path+'stat_des3/'+'agg 2019.png')
plt.show()

