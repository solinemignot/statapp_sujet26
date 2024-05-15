import pandas as pd

path = "/home/onyxia/work/statapp_sujet26/"
file_name1 = "dataset_complet_part_1.csv"
file_name2 = "dataset_complet_part_2.csv"
df1 = pd.read_csv(path + file_name1, sep=',', low_memory=False)
df2 = pd.read_csv(path + file_name2, sep=',', low_memory=False)
df = pd.concat([df1, df2])
df = df.loc[df['an'] == 2022]
df.replace(-1, pd.NA, inplace=True)

#Dummy heure de pointe
def is_peak_hour(hour_minute):
    hour, minute = map(int, hour_minute.split(':'))
    total_minutes = hour * 60 + minute
    peak_hours = [(7, 0), (10, 0), (16, 30), (19, 30)]
    for start, end in zip(peak_hours[:-1], peak_hours[1:]):
        start_minutes = start[0] * 60 + start[1]
        end_minutes = end[0] * 60 + end[1]
        if start_minutes <= total_minutes < end_minutes:
            return 1
    return 0
df['HP_ind'] = df['hrmn'].apply(is_peak_hour)

#Dummy jour de semaine
df['date'] = pd.to_datetime({'year': 2022, 'month': df['mois'], 'day': df['jour']})
df['jour_de_semaine'] = df['date'].dt.day_name()
df = pd.get_dummies(df, columns=['jour_de_semaine'], prefix='jour', dtype=int)


#Dummy plage horaire
'''def plage_horaire(heure):
    if 5 <= heure < 12:
        return 'matin'
    elif 12 <= heure < 14:
        return 'midi'
    elif 14 <= heure < 18:
        return 'après-midi'
    elif 18 <= heure < 22:
        return 'soir'
    else:
        return 'nuit'

df['plage_horaire'] = df['hrmn'].apply(plage_horaire)
df = pd.get_dummies(df, columns=['plage_horaire'], prefix='plage_horaire', dtype=int)'''
 

# Conversion des colonnes 'mois' et 'jour' en dates
df['date'] = pd.to_datetime({'year': 2022, 'month': df['mois'], 'day': df['jour']})

# Jours fériés en 2022
jours_feries_2022 = [
    '2022-01-01', '2022-04-22', '2022-05-01', '2022-05-08', '2022-05-30', 
    '2022-06-10', '2022-07-14', '2022-08-15', '2022-11-01', '2022-11-11', '2022-12-25'
]

# Création de la colonne 'jour_ferie'
df['jour_ferie'] = df['date'].isin(pd.to_datetime(jours_feries_2022)).astype(int)

# Vacances scolaires en 2022
vacances_2022 = [
    # Vacances d'hiver
    ('2022-02-19', '2022-03-06'),
    ('2022-02-12', '2022-02-27'),
    ('2022-02-26', '2022-03-13'),
    # Vacances de printemps
    ('2022-04-16', '2022-05-02'),
    ('2022-04-09', '2022-04-24'),
    ('2022-04-23', '2022-05-08'),
    # Vacances d'été
    ('2022-07-09', '2022-09-04'),
    # Vacances de la Toussaint
    ('2022-10-22', '2022-11-07'),
    # Vacances de Noël
    ('2022-12-24', '2022-12-31')
]

# Création de la colonne 'vacances_scolaires'
df['vacances_scolaires'] = 0
for start, end in vacances_2022:
    df.loc[(df['date'] >= start) & (df['date'] <= end), 'vacances_scolaires'] = 1

#Dummy mois
df['mois'] = df['mois'].replace({1.:'janvier',2.:'février',3.:'mars',4.:'avril',5.:'mai',6.:'juin',7.:'juillet',8.:'août',9.:'septembre',10.:'octobre',11.:'novembre',12.:'décembre'})
df = pd.get_dummies(df, columns=['mois'], prefix='mois', dtype=int)

# Dummy pour les variables spécifiées, en excluant les valeurs égales à -1 : celles qui ont pas de sens (valeur num )
columns_to_dummy = ['lum', 'agg', 'int', 'atm', 'catr', 'circ', 'prof', 'plan', 'surf', 'situ', 'infra']
print(df.columns)
for column in columns_to_dummy:
        df = pd.get_dummies(df, columns=[column], prefix=[column], dtype=int)

# Dummy département
def assign_region(dep_code):
    regions = {
        '1': 'Auvergne-Rhône-Alpes',
        '2': 'Hauts-de-France',
        '3': 'Auvergne-Rhône-Alpes',
        '4': 'PACA',
        '5': 'PACA',
        '6': 'PACA',
        '7': 'Auvergne-Rhône-Alpes',
        '8': 'Grand Est',
        '9': 'Occitanie',
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
        '2A': 'Corse',
        '2B': 'Corse',
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
        '971': 'Outre Mer',
        '972': 'Outre Mer',
        '973': 'Outre Mer',
        '974': 'Outre Mer',
        '976': 'Outre Mer',
        '977' : 'Collectivité Outre Mer', 
        '978' : 'Collectivité Outre Mer', 
        '986' : 'Collectivité Outre Mer', 
        '987' : 'Collectivité Outre Mer', 
        '988' : 'Collectivité Outre Mer',
        '2A' : 'Corse',
        '2B' : 'Corse',

    }
    return regions.get(dep_code[:2], 'Autre')

df['region'] = df['dep'].apply(assign_region)
#j'ai verif tout a été fill out avec les régions (pas de valeurs manquantes ds région)

df = pd.get_dummies(df, columns=['region'], prefix='region', dtype=int)

# Enlever les colonnes spécifiées
columns_to_drop = ['Num_Acc', 'an', 'jour', 'hrmn', 'col', 'dep','com', 'adr', 'gps', 'lat', 'long', 'voie', 'v1', 'v2', 'pr', 'pr1', 'vosp', 'lartpc', 'larrout', 'date']
df.drop(columns=columns_to_drop, inplace=True)

num_rows = len(df)
quart=num_rows // 4
midpoint = num_rows // 2
troisquarts=3* (num_rows // 4)
df_part1 = df.iloc[:quart]
df_part2 = df.iloc[quart:midpoint]
df_part3 = df.iloc[midpoint: troisquarts]
df_part4 = df.iloc[troisquarts]

df_part1.to_csv(path+'dataset_complet_avec_dummies_2022_part_1.csv', index=False)
df_part2.to_csv(path+'dataset_complet_avec_dummies_2022_part_2.csv', index=False)
df_part3.to_csv(path+'dataset_complet_avec_dummies_2022_part_3.csv', index=False)
df_part4.to_csv(path+'dataset_complet_avec_dummies_2022_part_4.csv', index=False)

# Afficher les premières lignes avec toutes les colonnes visibles
with pd.option_context('display.max_columns', None):
    print(df.head())