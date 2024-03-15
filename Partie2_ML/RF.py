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
file_name = "dataset_2019_dummy.csv"
df = pd.read_csv(path + file_name, sep=',', low_memory=False)

# Modifier la colonne 'grav' pour un problème de classification binaire
df['grav'] = df['grav'].replace({1: 0, 2: 0, 3: 1, 4: 1})

# Diviser le jeu de données en ensembles d'entraînement et de test
y = df['grav']
X = df.drop(columns=['grav'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# Normaliser les fonctionnalités
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Créer un classifieur Random Forest
rf_classifier = RandomForestClassifier(random_state=42)

# Entraîner le modèle
rf_classifier.fit(X_train, y_train)

# Faire des prédictions sur l'ensemble de test
y_pred = rf_classifier.predict(X_test)

# Évaluer les performances du modèle
accuracy = accuracy_score(y_test, y_pred)
print("Précision du modèle sans ajustement des hyperparamètres:", accuracy)
