import pandas as pd

path = "/home/onyxia/work/statapp_sujet26/"
file_name1 = "dataset_complet_part_1.csv"
file_name2 = "dataset_complet_part_2.csv"
df1 = pd.read_csv(path + file_name1, sep=',', low_memory=False)
df2 = pd.read_csv(path + file_name2, sep=',', low_memory=False)
df = pd.concat([df1, df2])
df = df.loc[df['an'] == 2019]


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
df['date'] = pd.to_datetime({'year': 2019, 'month': df['mois'], 'day': df['jour']})
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


#Dummy jour férié : 
df['date'] = pd.to_datetime({'year': 2019, 'month': df['mois'], 'day': df['jour']})

jours_feries_2019 = [
    '2019-01-01', '2019-04-22', '2019-05-01', '2019-05-08', '2019-05-30', 
    '2019-06-10', '2019-07-14', '2019-08-15', '2019-11-01', '2019-11-11', '2019-12-25'
]

df['jour_ferie'] = df['date'].isin(pd.to_datetime(jours_feries_2019)).astype(int)

#Vacances scolaires en 2019
vacances_2019 = [
    # Vacances d'hiver
    ('2019-02-16', '2019-03-03'),
    ('2019-02-09', '2019-02-24'),
    ('2019-02-23', '2019-03-10'),
    # Vacances de printemps
    ('2019-04-13', '2019-04-28'),
    ('2019-04-06', '2019-04-22'),
    ('2019-04-20', '2019-05-05'),
    # Vacances d'été
    ('2019-07-06', '2019-09-01'),
    # Vacances de la Toussaint
    ('2019-10-19', '2019-11-04'),
    # Vacances de Noël
    ('2019-12-21', '2019-12-31')
]

#Dummy vacances scolaires
df['vacances_scolaires'] = 0
for start, end in vacances_2019:
    df.loc[(df['date'] >= start) & (df['date'] <= end), 'vacances_scolaires'] = 1

#Dummy mois
df['mois'] = df['mois'].replace({1.:'janvier',2.:'février',3.:'mars',4.:'avril',5.:'mai',6.:'juin',7.:'juillet',8.:'août',9.:'septembre',10.:'octobre',11.:'novembre',12.:'décembre'})
df = pd.get_dummies(df, columns=['mois'], prefix='mois', dtype=int)

#Dummy departement
df = pd.get_dummies(df, columns=['dep'], prefix='dep', dtype=int)


#Dummy pour les autres colonnes spécifiques
columns_to_dummy = ['lum', 'agg', 'int', 'atm', 'catr', 'circ', 'nbv', 'prof', 'plan', 'surf', 'situ', 'infra', 'vma']
df = pd.get_dummies(df, columns=columns_to_dummy, prefix=columns_to_dummy, dtype=int)

print(df)
# Afficher le dataframe avec la nouvelle colonne ajoutée
#print(df)

