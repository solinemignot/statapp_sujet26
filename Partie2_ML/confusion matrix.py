import statsmodels.api as sm
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy
from scipy.stats import norm
import pandas as pd

path = "/home/onyxia/work/statapp_sujet26/"
file_name1 = "dataset_complet_part_1.csv"
file_name2 = "dataset_complet_part_2.csv"
df1 = pd.read_csv(path + file_name1, sep=',', low_memory=False)
df2 = pd.read_csv(path + file_name2, sep=',', low_memory=False)
df = pd.concat([df1, df2])
df['an'] = df['an'].astype(int)

# Convertir la colonne "grav" en valeurs binaires (0 ou 1)
df['grav'] = df['grav'].replace({'1': 0, '2': 0, '3': 1, '4': 1,1: 0, 2: 0, 3: 1, 4: 1}).astype(int)

# Filtrer les données pour l'année 2019
df = df[df['an'] == 2019]

df_num = df.select_dtypes(include = ['float64', 'int64'])
df_num.head()
plt.figure(figsize=(8, 6))
sns.set_theme(style="white")
corr = df_num.corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
f, ax = plt.subplots(figsize=(11, 9))
cmap = sns.color_palette("vlag", as_cmap=True)

sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})


plt.title('Confusion Matrix en 2019')
plt.savefig(path+'Partie2_ML/'+'confusion_matrix.png')  # Save the confusion matrix as an image
plt.show()