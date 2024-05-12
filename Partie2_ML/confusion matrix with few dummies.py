import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

path = "/home/onyxia/work/statapp_sujet26/"
file_name1 = "dataset_complet_part_1.csv"
file_name2 = "dataset_complet_part_2.csv"
df1 = pd.read_csv(path + file_name1, sep=',', low_memory=False)
df2 = pd.read_csv(path + file_name2, sep=',', low_memory=False)
df = pd.concat([df1, df2])
df['an'] = df['an'].astype(int)

# Convertir la colonne "grav" en valeurs binaires (0 ou 1)
df['grav'] = df['grav'].replace({'1': 0, '2': 0, '3': 1, '4': 1, 1: 0, 2: 0, 3: 1, 4: 1}).astype(int)

# Filtrer les données pour l'année 2019
df = df[df['an'] == 2019]

# Dummy heure de pointe
def is_peak_hour(hour_minute):
    hour, minute = map(int, hour_minute.split(':'))
    total_minutes = hour * 60 + minute
    peak_hours = [(7, 0), (9, 30), (16, 30), (19,0)]
    for start, end in zip(peak_hours[:-1], peak_hours[1:]):
        start_minutes = start[0] * 60 + start[1]
        end_minutes = end[0] * 60 + end[1]
        if start_minutes <= total_minutes < end_minutes:
            return 1
    return 0
df['Heure de pointe (D)'] = df['hrmn'].apply(is_peak_hour)

#Dummy jour de semaine
df['date'] = pd.to_datetime({'year': 2019, 'month': df['mois'], 'day': df['jour']})
df['Jour de semaine (D)'] = df['date'].dt.day_name()
df = pd.get_dummies(df, columns=['Jour de semaine (D)'], prefix='jour', dtype=int)

# Dummy jour férié
jours_feries_2019 = [
    '2019-01-01', '2019-04-22', '2019-05-01', '2019-05-08', '2019-05-30', 
    '2019-06-10', '2019-07-14', '2019-08-15', '2019-11-01', '2019-11-11', '2019-12-25'
]
df['Jours fériés (D)'] = df['date'].isin(pd.to_datetime(jours_feries_2019)).astype(int)

# Dummy vacances scolaires
vacances_2019 = [
    ('2019-02-16', '2019-03-03'),
    ('2019-02-09', '2019-02-24'),
    ('2019-02-23', '2019-03-10'),
    ('2019-04-13', '2019-04-28'),
    ('2019-04-06', '2019-04-22'),
    ('2019-04-20', '2019-05-05'),
    ('2019-07-06', '2019-09-01'),
    ('2019-10-19', '2019-11-04'),
    ('2019-12-21', '2019-12-31')
]
df['Vacances scolaires (D)'] = 0
for start, end in vacances_2019:
    df.loc[(df['date'] >= start) & (df['date'] <= end), 'Vacances scolaires (D)'] = 1


# Créer un dictionnaire de mapping des anciens noms aux nouveaux noms
nouveaux_noms = {
    'lum': 'Luminosité',
    'agg': 'Agglomération',
    'int': 'Intersection',
    'atm': 'Météo',
    'col': 'Collision',
    'dep': 'Département',
    'catr': 'TypeR',
    'circ': 'Circulation',
    'nbv': 'Nb voies',
    'vosp': 'Voie réservée',
    'prof': 'Pente',
    'plan': 'FormeR',
    'surf': 'SurfaceR',
    'infra': 'AménagementR',
    'situ': 'SituationAcc',
    'vma': 'VitesseMax'
}

# Utiliser le dictionnaire pour changer les noms des variables
df.rename(columns=nouveaux_noms, inplace=True)


columns_to_drop = ['Num_Acc', 'an', 'com', 'adr', 'gps', 'lat', 'long', 'voie', 'v1', 'v2', 'pr', 'pr1', 'lartpc', 'larrout', 'date']
df.drop(columns=columns_to_drop, inplace=True)



# Sélectionner les variables numériques
df_num = df.select_dtypes(include=['float64', 'int64'])

# Calculer la matrice de corrélation
corr = df_num.corr()

# Tracer la heatmap de la matrice de corrélation
plt.figure(figsize=(12, 10))
plt.subplots_adjust(left=0.25)
sns.set_theme(style="white")
mask = np.triu(np.ones_like(corr, dtype=bool))

sns.heatmap(corr, mask=mask, cmap="vlag", vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})

plt.title('Matrice de corrélation pour 2019 avec variables indicatrices')
plt.savefig(path + 'Partie2_ML/' + 'confusion_matrix_with_dummies.png')  # Enregistrer la matrice de corrélation en tant qu'image
plt.show()
