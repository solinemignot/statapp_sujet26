"""import pandas as pd
import matplotlib.pyplot as plt

path = "/home/onyxia/work/statapp_sujet26/"
file_name1 = "dataset_complet_part_1.csv"
file_name2 = "dataset_complet_part_2.csv"
df1 = pd.read_csv(path + file_name1, sep=',', low_memory=False)
df2 = pd.read_csv(path + file_name2, sep=',', low_memory=False)
df = pd.concat([df1, df2])

# Convertir la colonne "grav" en valeurs binaires (0 ou 1)
df['grav'] = df['grav'].replace({'1': 0, '2': 0, '3': 1, '4': 1,1: 0, 2: 0, 3: 1, 4: 1}).astype(int)

# Filtrer les données pour l'année 2019
df = df[df['an'] == 2019]

# Convertir les mois en format chaîne de caractères
df['mois'] = df['mois'].astype(int).apply(lambda x: '{:02d}'.format(x))

# Créer un DataFrame pour le graphique
graph_df = df.groupby(['grav', 'mois']).size().unstack(fill_value=0)

# Renommer les colonnes pour les étiquettes de l'axe x
months = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
graph_df.columns = months

# Tracer le graphique
plt.figure(figsize=(10, 6))
plt.plot(graph_df.columns, graph_df.iloc[0], label='gravité 0', marker='o', linestyle='-')
plt.plot(graph_df.columns, graph_df.iloc[1], label='gravité 1', marker='o', linestyle='-')

plt.xticks(rotation=45, ha='right')
plt.ylabel('Nombre d\'accidents')
plt.xlabel('Mois')
plt.title('Nombre total d\'accidents par mois en 2019')
plt.ylim(0, 3600)
plt.legend()
plt.tight_layout()
plt.savefig(path + 'stat_des1/' + 'mois_en_2019.png')
plt.show()





# Par an

df['an']=df['an'].replace({5.0:2005.0,6.0:2006.0,7.0:2007.0,8.0:2008.0,9.0:2009.0,10.0:2010.0,11.0:2011.0,12.0:2012.0,12.0:2012.0,13.0:2013.0,14.0:2014.0,15.0:2015.0,16.0:2016.0,17.0:2017.0,18.0:2018.0})

graph_df = df.groupby(['grav', 'an']).size().reset_index(name='accident_count')
graph_df = graph_df.pivot(index='grav', columns='an', values='accident_count')

plt.figure(figsize=(10, 6))
for gravity_type in graph_df.index:
    plt.plot(graph_df.columns, graph_df.loc[gravity_type], label=f'Gravity {gravity_type}', marker='o', linestyle='-')

plt.ylabel('Nombre d accidents')
plt.xlabel('An')
plt.title('Nombre d accidents selon l année')
plt.legend()
plt.savefig(path+'capucine/'+'an.png')
plt.show()


#Par heure

df['hrmn'] = pd.to_numeric(df['hrmn'].str.replace(':', ''), errors='coerce')

graph_df = df.groupby(['grav', 'hrmn']).size().reset_index(name='accident_count')
graph_df = graph_df.pivot(index='grav', columns='hrmn', values='accident_count')

plt.figure(figsize=(10, 6))
for gravity_type in graph_df.index:
    plt.plot(graph_df.columns.astype(str).str.zfill(4).str[:2] + ':' + graph_df.columns.astype(str).str.zfill(4).str[2:],
             graph_df.loc[gravity_type], label=f'Gravity {gravity_type}')

plt.ylabel('Nombre d accidents')
plt.xlabel('Heure')
plt.title('Nombre d accidents selon l heure de la journée')


plt.xticks(rotation=45, ha='right')
num_columns = graph_df.shape[1]
specific_hours = ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00']
tick_positions = [int(i*300*num_columns/2359)for i in range (8)]
plt.xticks(tick_positions, specific_hours, rotation=45, ha='right')


plt.legend()
plt.tight_layout() 
plt.savefig(path + 'stat_des1/' + 'heure en 2019.png')
plt.show()


"""

import pandas as pd
import matplotlib.pyplot as plt

path = "/home/onyxia/work/statapp_sujet26/"
file_name1 = "dataset_complet_part_1.csv"
file_name2 = "dataset_complet_part_2.csv"
df1 = pd.read_csv(path + file_name1, sep=',', low_memory=False)
df2 = pd.read_csv(path + file_name2, sep=',', low_memory=False)
df = pd.concat([df1, df2])

# Convertir la colonne "grav" en valeurs binaires (0 ou 1)
df['grav'] = df['grav'].replace({'1': 0, '2': 0, '3': 1, '4': 1,1: 0, 2: 0, 3: 1, 4: 1}).astype(int)

# Filtrer les données pour l'année 2019
df = df[df['an'] == 2019]

# Convertir les mois en format chaîne de caractères
df['mois'] = df['mois'].astype(int).apply(lambda x: '{:02d}'.format(x))

# Créer un DataFrame pour le graphique
graph_df = df.groupby(['grav', 'mois']).size().unstack(fill_value=0)

# Renommer les colonnes pour les étiquettes de l'axe x
months = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
graph_df.columns = months

# Tracer le graphique
plt.figure(figsize=(10, 6))
plt.plot(graph_df.columns, graph_df.iloc[0], label='gravité 0', marker='o', linestyle='-')
plt.plot(graph_df.columns, graph_df.iloc[1], label='gravité 1', marker='o', linestyle='-')

plt.xticks(rotation=45, ha='right')
plt.ylabel('Nombre d\'accidents')
plt.xlabel('Mois')
plt.title('Nombre total d\'accidents par mois en 2019')
plt.ylim(0, 3600)
plt.legend()
plt.tight_layout()
plt.savefig(path + 'stat_des1/' + 'mois_en_2019.png')
plt.show()





"""# Par an

df['an']=df['an'].replace({5.0:2005.0,6.0:2006.0,7.0:2007.0,8.0:2008.0,9.0:2009.0,10.0:2010.0,11.0:2011.0,12.0:2012.0,12.0:2012.0,13.0:2013.0,14.0:2014.0,15.0:2015.0,16.0:2016.0,17.0:2017.0,18.0:2018.0})

graph_df = df.groupby(['grav', 'an']).size().reset_index(name='accident_count')
graph_df = graph_df.pivot(index='grav', columns='an', values='accident_count')

plt.figure(figsize=(10, 6))
for gravity_type in graph_df.index:
    plt.plot(graph_df.columns, graph_df.loc[gravity_type], label=f'Gravity {gravity_type}', marker='o', linestyle='-')

plt.ylabel('Nombre d accidents')
plt.xlabel('An')
plt.title('Nombre d accidents selon l année')
plt.legend()
plt.savefig(path+'capucine/'+'an.png')
plt.show()"""


#Par heure

df['hrmn'] = pd.to_numeric(df['hrmn'].str.replace(':', ''), errors='coerce')

graph_df = df.groupby(['grav', 'hrmn']).size().reset_index(name='accident_count')
graph_df = graph_df.pivot(index='grav', columns='hrmn', values='accident_count')

plt.figure(figsize=(10, 6))
for gravity_type in graph_df.index:
    plt.plot(graph_df.columns.astype(str).str.zfill(4).str[:2] + ':' + graph_df.columns.astype(str).str.zfill(4).str[2:],
             graph_df.loc[gravity_type], label=f'Gravity {gravity_type}')

plt.ylabel('Nombre d accidents')
plt.xlabel('Heure')
plt.title('Nombre d accidents selon l heure de la journée')


plt.xticks(rotation=45, ha='right')
num_columns = graph_df.shape[1]
specific_hours = ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00']
tick_positions = [int(i*300*num_columns/2359)for i in range (8)]
plt.xticks(tick_positions, specific_hours, rotation=45, ha='right')


plt.legend()
plt.tight_layout() 
plt.savefig(path + 'stat_des1/' + 'heure en 2019.png')
plt.show()





