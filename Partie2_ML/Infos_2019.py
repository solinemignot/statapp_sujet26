import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Charger le jeu de données
path = "/home/onyxia/work/statapp_sujet26/"
file_name1 = "dataset_complet_part_1.csv"
file_name2 = "dataset_complet_part_2.csv"
df1 = pd.read_csv(path + file_name1, sep=',', low_memory=False)
df2 = pd.read_csv(path + file_name2, sep=',', low_memory=False)
df = pd.concat([df1, df2])

# Filtre pour l'année 2019 et remplacement des valeurs de 'grav'
df = df.loc[df['an'] == 2019]
df['grav'] = df['grav'].replace({1: 0, 2: 0, 3: 1, 4: 1})

# Compter les occurrences de chaque valeur dans la colonne 'grav'
counts = df['grav'].value_counts()

# Calculer les pourcentages
percentage_0 = (counts[0] / len(df)) * 100
percentage_1 = (counts[1] / len(df)) * 100

print("Pourcentage de gravité 0:", percentage_0)
print("Pourcentage de gravité 1:", percentage_1)