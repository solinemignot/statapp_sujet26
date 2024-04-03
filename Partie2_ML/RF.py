#%%
# Import des bibliothèques nécessaires
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Charger le jeu de données
path = "/home/onyxia/work/statapp_sujet26/"
file_name1="dataset_complet_avec_dummies_part_1.csv"
file_name2="dataset_complet_avec_dummies_part_2.csv"
df1= pd.read_csv(path+file_name1, sep=',',low_memory=False)
df2= pd.read_csv(path+file_name2, sep=',',low_memory=False)
df=pd.concat([df1,df2])
colonnes_specifiques = ['grav','nbv']
df= df.loc[:, colonnes_specifiques]

# Modifier la colonne 'grav' pour un problème de classification binaire
df['grav'] = df['grav'].replace({1: 0, 2: 0, 3: 1, 4: 1})

# Diviser le jeu de données en ensembles d'entraînement et de test
y = df['grav']
X = df.drop(columns=['grav'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# Créer un classifieur Random Forest
rf_classifier = RandomForestClassifier(random_state=42)

# Entraîner le modèle
rf_classifier.fit(X_train, y_train)

# Extraire l'importance des features
importances = rf_classifier.feature_importances_

# Calculer le pourcentage d'importance de chaque feature
total_importance = np.sum(importances)
percentage_importance = (importances / total_importance) * 100

# Créer un DataFrame pour stocker les noms des features et leur pourcentage d'importance
feature_names = X.columns
indices = np.argsort(importances)[::-1]
feature_df = pd.DataFrame({'Feature': feature_names[indices], 'Importance (%)': percentage_importance})


# %%
