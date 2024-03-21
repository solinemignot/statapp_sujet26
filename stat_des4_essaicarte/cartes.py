

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

path="/home/onyxia/statapp_sujet26/"
file_name1="dataset_complet_part_1.csv"
file_name2="dataset_complet_part_2.csv"
df1= pd.read_csv(path+file_name1, sep=',',low_memory=False)
df2= pd.read_csv(path+file_name2, sep=',',low_memory=False)
df=pd.concat([df1,df2])
df['grav'] = df['grav'].replace({'1':1,'2':2,'3':3,'4':4})
df=df[df['grav']!='grav']
df['grav']=df['grav'].replace({1: 0, 2: 0, 3: 1, 4: 1})

france = gpd.read_file('/home/onyxia/statapp_sujet26/stat_des4_essaicarte/departements-version-simplifiee.geojson')



df['dep'] = df['dep'].apply(lambda x: int(float(x)/10) if isinstance(x, float) or "." in x else x)
df['dep']=df['dep'].astype(str)
df['dep']=df['dep'].replace({'1':'01','2':'02','3':'03','4':'04','5':'05','6':'06','7':'07','8':'08','9':'09'})
df['régions']=df['dep']
df['régions']=df['dep'].replace({
        '1': 'Auvergne-Rhône-Alpes',
        '2': 'Hauts-de-France',
        '3': 'Auvergne-Rhône-Alpes',
        '4': 'PACA',
        '5': 'PACA',
        '6': 'PACA',
        '7': 'Auvergne-Rhône-Alpes',
        '8': 'Grand Est',
        '9': 'Occitanie',
        '01': 'Auvergne-Rhône-Alpes',
        '02': 'Hauts-de-France',
        '03': 'Auvergne-Rhône-Alpes',
        '04': 'PACA',
        '05': 'PACA',
        '06': 'PACA',
        '07': 'Auvergne-Rhône-Alpes',
        '08': 'Grand Est',
        '09': 'Occitanie',
        '10': 'Grand Est',
        '11': 'Occitanie',
        '12': 'Occitanie',
        '13': 'PACA',
        '14': 'Normandie',
        '15': 'Auvergne-Rhône-Alpes',
        '16': 'Nouvelle-Aquitaine',
        '17': 'Nouvelle-Aquitaine',
        '18': 'Centre-Val de Loire',
        '19': 'Nouvelle-Aquitaine',
        '20':'Corse',
        '20A': 'Corse',
        '20B': 'Corse',
        '21': 'Bourgogne-Franche-Comté',
        '22': 'Bretagne',
        '23': 'Nouvelle-Aquitaine',
        '24': 'Nouvelle-Aquitaine',
        '25': 'Bourgogne-Franche-Comté',
        '26': 'Auvergne-Rhône-Alpes',
        '27': 'Normandie',
        '28': 'Centre-Val de Loire',
        '29': 'Bretagne',
        '30': 'Occitanie',
        '31': 'Occitanie',
        '32': 'Occitanie',
        '33': 'Nouvelle-Aquitaine',
        '34': 'Occitanie',
        '35': 'Bretagne',
        '36': 'Centre-Val de Loire',
        '37': 'Centre-Val de Loire',
        '38': 'Auvergne-Rhône-Alpes',
        '39': 'Bourgogne-Franche-Comté',
        '40': 'Nouvelle-Aquitaine',
        '41': 'Centre-Val de Loire',
        '42': 'Auvergne-Rhône-Alpes',
        '43': 'Auvergne-Rhône-Alpes',
        '44': 'Pays de la Loire',
        '45': 'Centre-Val de Loire',
        '46': 'Occitanie',
        '47': 'Nouvelle-Aquitaine',
        '48': 'Occitanie',
        '49': 'Pays de la Loire',
        '50': 'Normandie',
        '51': 'Grand Est',
        '52': 'Grand Est',
        '53': 'Pays de la Loire',
        '54': 'Grand Est',
        '55': 'Grand Est',
        '56': 'Bretagne',
        '57': 'Grand Est',
        '58': 'Bourgogne-Franche-Comté',
        '59': 'Hauts-de-France',
        '60': 'Hauts-de-France',
        '61': 'Normandie',
        '62': 'Hauts-de-France',
        '63': 'Auvergne-Rhône-Alpes',
        '64': 'Nouvelle-Aquitaine',
        '65': 'Occitanie',
        '66': 'Occitanie',
        '67': 'Grand Est',
        '68': 'Grand Est',
        '69': 'Auvergne-Rhône-Alpes',
        '70': 'Bourgogne-Franche-Comté',
        '71': 'Bourgogne-Franche-Comté',
        '72': 'Pays de la Loire',
        '73': 'Auvergne-Rhône-Alpes',
        '74': 'Auvergne-Rhône-Alpes',
        '75': 'Île-de-France',
        '76': 'Normandie',
        '77': 'Île-de-France',
        '78': 'Île-de-France',
        '79': 'Nouvelle-Aquitaine',
        '80': 'Hauts-de-France',
        '81': 'Occitanie',
        '82': 'Occitanie',
        '83': 'PACA',
        '84': 'PACA',
        '85': 'Pays de la Loire',
        '86': 'Nouvelle-Aquitaine',
        '87': 'Nouvelle-Aquitaine',
        '88': 'Grand Est',
        '89': 'Bourgogne-Franche-Comté',
        '90': 'Bourgogne-Franche-Comté',
        '91': 'Île-de-France',
        '92': 'Île-de-France',
        '93': 'Île-de-France',
        '94': 'Île-de-France',
        '95': 'Île-de-France',
        '97':'Outre Mer',
        '971': 'Outre Mer',
        '972': 'Outre Mer',
        '973': 'Outre Mer',
        '974': 'Outre Mer',
        '975':'Outre Mer',
        '976': 'Outre Mer',
        '977' : 'Collectivité Outre Mer', 
        '978' : 'Collectivité Outre Mer', 
        '986' : 'Collectivité Outre Mer', 
        '987' : 'Collectivité Outre Mer', 
        '988' : 'Collectivité Outre Mer',
        '2A' : 'Corse',
        '2B' : 'Corse',
    })

"""
df_carte = df_carte_grav0[['dep', 'grav']]
df_carte = df_carte.dropna()
mediane_par_departement = df_carte.groupby('dep')['grav'].count().reset_index()
merged_data = france.merge(mediane_par_departement, how='left', left_on='code', right_on='dep')


plt.figure(figsize=(10, 6))
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
merged_data.plot(column='grav', cmap='YlOrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
ax.set_title('Nombre d accidents pas grave par département en France')
ax.set_axis_off()
plt.savefig(path+'stat_des4_essaicarte/'+'carte grav 0.png')
plt.show()


df_carte = df_carte_grav1[['dep', 'grav']]
df_carte = df_carte.dropna()
mediane_par_departement = df_carte.groupby('dep')['grav'].count().reset_index()
merged_data = france.merge(mediane_par_departement, how='left', left_on='code', right_on='dep')
merged_data.head(5)


plt.figure(figsize=(10, 6))
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
merged_data.plot(column='grav', cmap='YlOrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
ax.set_title('Nombre d accidents grave par département en France')
ax.set_axis_off()
plt.savefig(path+'stat_des4_essaicarte/'+'carte_grav1.png')
plt.show()

"""
df_carte_grav0=df[df['grav']==0]
df_carte_grav1=df[df['grav']==1]
df_carte = df_carte_grav0[['dep','régions', 'grav']]
df_carte = df_carte.dropna()
mediane_par_departement = df_carte.groupby('régions')['grav'].count().reset_index()
df_carte = df_carte.groupby('dep')['grav'].count().reset_index()
df_carte['régions']=df_carte['dep'].replace({
        '1': 'Auvergne-Rhône-Alpes',
        '2': 'Hauts-de-France',
        '3': 'Auvergne-Rhône-Alpes',
        '4': 'PACA',
        '5': 'PACA',
        '6': 'PACA',
        '7': 'Auvergne-Rhône-Alpes',
        '8': 'Grand Est',
        '9': 'Occitanie',
        '01': 'Auvergne-Rhône-Alpes',
        '02': 'Hauts-de-France',
        '03': 'Auvergne-Rhône-Alpes',
        '04': 'PACA',
        '05': 'PACA',
        '06': 'PACA',
        '07': 'Auvergne-Rhône-Alpes',
        '08': 'Grand Est',
        '09': 'Occitanie',
        '10': 'Grand Est',
        '11': 'Occitanie',
        '12': 'Occitanie',
        '13': 'PACA',
        '14': 'Normandie',
        '15': 'Auvergne-Rhône-Alpes',
        '16': 'Nouvelle-Aquitaine',
        '17': 'Nouvelle-Aquitaine',
        '18': 'Centre-Val de Loire',
        '19': 'Nouvelle-Aquitaine',
        '20':'Corse',
        '20A': 'Corse',
        '20B': 'Corse',
        '21': 'Bourgogne-Franche-Comté',
        '22': 'Bretagne',
        '23': 'Nouvelle-Aquitaine',
        '24': 'Nouvelle-Aquitaine',
        '25': 'Bourgogne-Franche-Comté',
        '26': 'Auvergne-Rhône-Alpes',
        '27': 'Normandie',
        '28': 'Centre-Val de Loire',
        '29': 'Bretagne',
        '30': 'Occitanie',
        '31': 'Occitanie',
        '32': 'Occitanie',
        '33': 'Nouvelle-Aquitaine',
        '34': 'Occitanie',
        '35': 'Bretagne',
        '36': 'Centre-Val de Loire',
        '37': 'Centre-Val de Loire',
        '38': 'Auvergne-Rhône-Alpes',
        '39': 'Bourgogne-Franche-Comté',
        '40': 'Nouvelle-Aquitaine',
        '41': 'Centre-Val de Loire',
        '42': 'Auvergne-Rhône-Alpes',
        '43': 'Auvergne-Rhône-Alpes',
        '44': 'Pays de la Loire',
        '45': 'Centre-Val de Loire',
        '46': 'Occitanie',
        '47': 'Nouvelle-Aquitaine',
        '48': 'Occitanie',
        '49': 'Pays de la Loire',
        '50': 'Normandie',
        '51': 'Grand Est',
        '52': 'Grand Est',
        '53': 'Pays de la Loire',
        '54': 'Grand Est',
        '55': 'Grand Est',
        '56': 'Bretagne',
        '57': 'Grand Est',
        '58': 'Bourgogne-Franche-Comté',
        '59': 'Hauts-de-France',
        '60': 'Hauts-de-France',
        '61': 'Normandie',
        '62': 'Hauts-de-France',
        '63': 'Auvergne-Rhône-Alpes',
        '64': 'Nouvelle-Aquitaine',
        '65': 'Occitanie',
        '66': 'Occitanie',
        '67': 'Grand Est',
        '68': 'Grand Est',
        '69': 'Auvergne-Rhône-Alpes',
        '70': 'Bourgogne-Franche-Comté',
        '71': 'Bourgogne-Franche-Comté',
        '72': 'Pays de la Loire',
        '73': 'Auvergne-Rhône-Alpes',
        '74': 'Auvergne-Rhône-Alpes',
        '75': 'Île-de-France',
        '76': 'Normandie',
        '77': 'Île-de-France',
        '78': 'Île-de-France',
        '79': 'Nouvelle-Aquitaine',
        '80': 'Hauts-de-France',
        '81': 'Occitanie',
        '82': 'Occitanie',
        '83': 'PACA',
        '84': 'PACA',
        '85': 'Pays de la Loire',
        '86': 'Nouvelle-Aquitaine',
        '87': 'Nouvelle-Aquitaine',
        '88': 'Grand Est',
        '89': 'Bourgogne-Franche-Comté',
        '90': 'Bourgogne-Franche-Comté',
        '91': 'Île-de-France',
        '92': 'Île-de-France',
        '93': 'Île-de-France',
        '94': 'Île-de-France',
        '95': 'Île-de-France',
        '97':'Outre Mer',
        '971': 'Outre Mer',
        '972': 'Outre Mer',
        '973': 'Outre Mer',
        '974': 'Outre Mer',
        '975':'Outre Mer',
        '976': 'Outre Mer',
        '977' : 'Collectivité Outre Mer', 
        '978' : 'Collectivité Outre Mer', 
        '986' : 'Collectivité Outre Mer', 
        '987' : 'Collectivité Outre Mer', 
        '988' : 'Collectivité Outre Mer',
        '2A' : 'Corse',
        '2B' : 'Corse',
    })
df_carte=df_carte[['dep','régions']]
df_carte=df_carte.merge(mediane_par_departement, how='left', left_on='régions', right_on='régions')
print(df_carte.head(5))
df_carte = df_carte[['dep','régions', 'grav']]

merged_data = france.merge(df_carte, how='left', left_on='code', right_on='dep')


plt.figure(figsize=(10, 6))
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
merged_data.plot(column='grav', cmap='YlOrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
ax.set_title('Nombre d accidents pas grave par département en France')
ax.set_axis_off()
plt.savefig(path+'stat_des4_essaicarte/'+'carte grav 0.png')
plt.show()


df_carte = df_carte_grav1[['dep','régions', 'grav']]
df_carte = df_carte.dropna()
mediane_par_departement = df_carte.groupby('régions')['grav'].count().reset_index()
df_carte = df_carte.groupby('dep')['grav'].count().reset_index()
df_carte['régions']=df_carte['dep'].replace({
        '1': 'Auvergne-Rhône-Alpes',
        '2': 'Hauts-de-France',
        '3': 'Auvergne-Rhône-Alpes',
        '4': 'PACA',
        '5': 'PACA',
        '6': 'PACA',
        '7': 'Auvergne-Rhône-Alpes',
        '8': 'Grand Est',
        '9': 'Occitanie',
        '01': 'Auvergne-Rhône-Alpes',
        '02': 'Hauts-de-France',
        '03': 'Auvergne-Rhône-Alpes',
        '04': 'PACA',
        '05': 'PACA',
        '06': 'PACA',
        '07': 'Auvergne-Rhône-Alpes',
        '08': 'Grand Est',
        '09': 'Occitanie',
        '10': 'Grand Est',
        '11': 'Occitanie',
        '12': 'Occitanie',
        '13': 'PACA',
        '14': 'Normandie',
        '15': 'Auvergne-Rhône-Alpes',
        '16': 'Nouvelle-Aquitaine',
        '17': 'Nouvelle-Aquitaine',
        '18': 'Centre-Val de Loire',
        '19': 'Nouvelle-Aquitaine',
        '20':'Corse',
        '20A': 'Corse',
        '20B': 'Corse',
        '21': 'Bourgogne-Franche-Comté',
        '22': 'Bretagne',
        '23': 'Nouvelle-Aquitaine',
        '24': 'Nouvelle-Aquitaine',
        '25': 'Bourgogne-Franche-Comté',
        '26': 'Auvergne-Rhône-Alpes',
        '27': 'Normandie',
        '28': 'Centre-Val de Loire',
        '29': 'Bretagne',
        '30': 'Occitanie',
        '31': 'Occitanie',
        '32': 'Occitanie',
        '33': 'Nouvelle-Aquitaine',
        '34': 'Occitanie',
        '35': 'Bretagne',
        '36': 'Centre-Val de Loire',
        '37': 'Centre-Val de Loire',
        '38': 'Auvergne-Rhône-Alpes',
        '39': 'Bourgogne-Franche-Comté',
        '40': 'Nouvelle-Aquitaine',
        '41': 'Centre-Val de Loire',
        '42': 'Auvergne-Rhône-Alpes',
        '43': 'Auvergne-Rhône-Alpes',
        '44': 'Pays de la Loire',
        '45': 'Centre-Val de Loire',
        '46': 'Occitanie',
        '47': 'Nouvelle-Aquitaine',
        '48': 'Occitanie',
        '49': 'Pays de la Loire',
        '50': 'Normandie',
        '51': 'Grand Est',
        '52': 'Grand Est',
        '53': 'Pays de la Loire',
        '54': 'Grand Est',
        '55': 'Grand Est',
        '56': 'Bretagne',
        '57': 'Grand Est',
        '58': 'Bourgogne-Franche-Comté',
        '59': 'Hauts-de-France',
        '60': 'Hauts-de-France',
        '61': 'Normandie',
        '62': 'Hauts-de-France',
        '63': 'Auvergne-Rhône-Alpes',
        '64': 'Nouvelle-Aquitaine',
        '65': 'Occitanie',
        '66': 'Occitanie',
        '67': 'Grand Est',
        '68': 'Grand Est',
        '69': 'Auvergne-Rhône-Alpes',
        '70': 'Bourgogne-Franche-Comté',
        '71': 'Bourgogne-Franche-Comté',
        '72': 'Pays de la Loire',
        '73': 'Auvergne-Rhône-Alpes',
        '74': 'Auvergne-Rhône-Alpes',
        '75': 'Île-de-France',
        '76': 'Normandie',
        '77': 'Île-de-France',
        '78': 'Île-de-France',
        '79': 'Nouvelle-Aquitaine',
        '80': 'Hauts-de-France',
        '81': 'Occitanie',
        '82': 'Occitanie',
        '83': 'PACA',
        '84': 'PACA',
        '85': 'Pays de la Loire',
        '86': 'Nouvelle-Aquitaine',
        '87': 'Nouvelle-Aquitaine',
        '88': 'Grand Est',
        '89': 'Bourgogne-Franche-Comté',
        '90': 'Bourgogne-Franche-Comté',
        '91': 'Île-de-France',
        '92': 'Île-de-France',
        '93': 'Île-de-France',
        '94': 'Île-de-France',
        '95': 'Île-de-France',
        '97':'Outre Mer',
        '971': 'Outre Mer',
        '972': 'Outre Mer',
        '973': 'Outre Mer',
        '974': 'Outre Mer',
        '975':'Outre Mer',
        '976': 'Outre Mer',
        '977' : 'Collectivité Outre Mer', 
        '978' : 'Collectivité Outre Mer', 
        '986' : 'Collectivité Outre Mer', 
        '987' : 'Collectivité Outre Mer', 
        '988' : 'Collectivité Outre Mer',
        '2A' : 'Corse',
        '2B' : 'Corse',
    })
df_carte=df_carte[['dep','régions']]
df_carte=df_carte.merge(mediane_par_departement, how='left', left_on='régions', right_on='régions')
print(df_carte.head(5))
df_carte = df_carte[['dep','régions', 'grav']]

merged_data = france.merge(df_carte, how='left', left_on='code', right_on='dep')


plt.figure(figsize=(10, 6))
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
merged_data.plot(column='grav', cmap='YlOrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
ax.set_title('Nombre d accidents pas grave par département en France')
ax.set_axis_off()
plt.savefig(path+'stat_des4_essaicarte/'+'carte grav 1.png')
plt.show()
