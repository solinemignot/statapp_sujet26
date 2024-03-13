#%%
# Import des bibliothèques nécessaires
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

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

# Suppression des colonnes non nécessaires
df = df.drop(columns=['Num_Acc', 'an', 'adr', 'lat', 'long', 'lartpc', 'larrout', 'com', 'gps', 'voie', 'dep', 'v2', 'pr', 'pr1'])
df['hrmn'] = df['hrmn'].str.split(':').str[0]

# Enregistrement des données préparées dans un fichier CSV
df.to_csv('random_forest.csv', index=False)

# Diviser le jeu de données en ensembles d'entraînement et de test
y = df['grav']
X = df.drop(columns=['grav'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# Normaliser les fonctionnalités
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Définir les hyperparamètres à tester
param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['auto', 'sqrt']
}

# Créer un classifieur Random Forest
rf_classifier = RandomForestClassifier(random_state=42)

# Recherche par grille pour trouver les meilleurs hyperparamètres
grid_search = GridSearchCV(estimator=rf_classifier, param_grid=param_grid, cv=3, n_jobs=-1, scoring='accuracy')
grid_search.fit(X_train, y_train)

# Afficher les meilleurs hyperparamètres
print("Meilleurs hyperparamètres:", grid_search.best_params_)

# Entraîner le modèle avec les meilleurs hyperparamètres
best_rf_classifier = grid_search.best_estimator_
best_rf_classifier.fit(X_train, y_train)

# Faire des prédictions sur l'ensemble de test
y_pred = best_rf_classifier.predict(X_test)

# Évaluer les performances du modèle
accuracy = accuracy_score(y_test, y_pred)
print("Précision avec les meilleurs hyperparamètres:", accuracy)


# Afficher l'importance de chaque feature avec les meilleurs hyperparamètres
importances = best_rf_classifier.feature_importances_
indices = np.argsort(importances)[::-1]

plt.figure(figsize=(8, 6))
plt.title("Importance des variables dans le modèle Random Forest (avec meilleurs hyperparamètres)")
plt.bar(range(X_train.shape[1]), importances[indices], align="center")
plt.xticks(range(X_train.shape[1]), [X.columns[i] for i in indices], rotation=45)
plt.xlabel('Variables')
plt.ylabel('Importance')
plt.show()

#Meilleurs hyperparamètres: {'max_depth': 10, 'max_features': 'sqrt', 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 100}
#Précision avec les meilleurs hyperparamètres: 0.7628030818037617
