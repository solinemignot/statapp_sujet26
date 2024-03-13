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
df = df.loc[df['an'] == 2019]
df['grav'] = df['grav'].replace({1: 0, 2: 0, 3: 1, 4: 1})

counts = df['grav'].value_counts()
percentage_0 = (counts[0] / len(df)) * 100
percentage_1 = (counts[1] / len(df)) * 100

print("Pourcentage de gravité 0:", percentage_0)
print("Pourcentage de gravité 1:", percentage_1)

#Pourcentage de gravité 0: 63.93439836845683
#Pourcentage de gravité 1: 36.06560163154317

# MIssing value : Compter les valeurs manquantes, y compris les valeurs -1
missing_percentage = ((df.isna() | (df == -1)).sum() / len(df)) * 100
print("Pourcentage de valeurs manquantes par variable (N/A + non renseigné -1 ) :")
print(missing_percentage)

print(df.head())