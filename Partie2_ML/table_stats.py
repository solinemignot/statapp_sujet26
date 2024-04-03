import pandas as pd

path = "/home/onyxia/work/statapp_sujet26/"
file_name1 = "dataset_complet_part_1.csv"
file_name2 = "dataset_complet_part_2.csv"
df1 = pd.read_csv(path + file_name1, sep=',', low_memory=False)
df2 = pd.read_csv(path + file_name2, sep=',', low_memory=False)
df = pd.concat([df1, df2])
df = df.loc[df['an'] == 2019]
df = df[['mois', 'jour', 'hrmn', 'lum', 'agg', 'int', 'atm', 'col', 'dep',
             'catr', 'circ', 'nbv', 'vosp', 'prof', 'plan', 'surf', 'infra', 
             'situ', 'vma']]

df['nbv'] = df['nbv'].astype(float)



# Calculer les statistiques descriptives
stats_count = df.count()
stats_min = df.apply(lambda x: min(x[x != -1]), axis=0)
stats_max = df.max()
stats_mode = df.mode().iloc[0]  # Mode peut retourner plusieurs valeurs, prenons la première
stats_missing = df.isnull().sum()
stats_non_renseigne = df.apply(lambda x: (x == -1.0).sum())
mode_counts = df.apply(lambda x: x.value_counts().iloc[0])


# Créer un DataFrame pour stocker les statistiques descriptives
stats_df = pd.DataFrame({
    'nb observations': stats_count,
    'min': stats_min,
    'max': stats_max,
    'mode': stats_mode,
    'mode_counts' : mode_counts,
    'missing_value': stats_missing,
    'non renseigné' : stats_non_renseigne
})

# Afficher les statistiques descriptives
print(stats_df)