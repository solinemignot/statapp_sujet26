

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

path="/home/onyxia/work/statapp_sujet26/"
file_name1="dataset_complet_part_1.csv"
file_name2="dataset_complet_part_2.csv"
df1= pd.read_csv(path+file_name1, sep=',',low_memory=False)
df2= pd.read_csv(path+file_name2, sep=',',low_memory=False)
df=pd.concat([df1,df2])
df['grav'] = df['grav'].replace({'1':1,'2':2,'3':3,'4':4})
df=df[df['grav']!='grav']
df['grav']=df['grav'].replace({1: 0, 2: 0, 3: 1, 4: 1})

france = gpd.read_file('/home/onyxia/work/statapp_sujet26/stat_des4_essaicarte/departements-version-simplifiee.geojson')

df['dep'] = df['dep'].apply(lambda x: int(float(x)/10) if isinstance(x, float) or "." in x else x)
df['dep']=df['dep'].astype(str)
df['dep']=df['dep'].replace({'1':'01','2':'02','3':'03','4':'04','5':'05','6':'06','7':'07','8':'08','9':'09'})

df_carte = df[['dep', 'grav']]
df_carte = df_carte.dropna()
df_carte = df_carte.groupby('dep')['grav'].count().reset_index()

merged_data = france.merge(df_carte, how='left', left_on='code', right_on='dep')

plt.figure(figsize=(10, 6))
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
merged_data.plot(column='grav', cmap='YlOrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
ax.set_title('Nombre d accidents par département en France')
ax.set_axis_off()
plt.savefig(path+'stat_des4_essaicarte/'+'carte .png')
plt.show()

