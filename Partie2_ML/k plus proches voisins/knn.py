from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import f1_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


path = "/home/onyxia/work/statapp_sujet26/"
file_name1 = "dataset_complet_avec_dummies_part_1.csv"
file_name2 = "dataset_complet_avec_dummies_part_2.csv"
file_name3 = "dataset_complet_avec_dummies_part_3.csv"
file_name4 = "dataset_complet_avec_dummies_part_4.csv"
df1 = pd.read_csv(path + file_name1, sep=',', low_memory=False)
df2 = pd.read_csv(path + file_name2, sep=',', low_memory=False)
df3 = pd.read_csv(path + file_name2, sep=',', low_memory=False)
df4 = pd.read_csv(path + file_name2, sep=',', low_memory=False)

df = pd.concat([df1, df2, df3, df4])
df.replace(-1, np.nan, inplace=True)
df['grav'] = df['grav'].replace({1:0,2:0,3:1,4:1})

y = df['grav']
X = df.drop(columns=['grav'])
features = X.columns

# Divisez les données en ensembles de formation et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Impute missing values
imputer = SimpleImputer(strategy='mean')
X_train_imputed = imputer.fit_transform(X_train)
X_test_imputed = imputer.transform(X_test)

# Normalisez les fonctionnalités pour une meilleure performance de KNN
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_imputed)
X_test_scaled = scaler.transform(X_test_imputed)
"""
# Initialisez le classificateur KNN
knn = KNeighborsClassifier(n_neighbors=5)  # Vous pouvez spécifier le nombre de voisins à utiliser

# Entraînez le modèle sur l'ensemble d'entraînement
knn.fit(X_train_scaled, y_train)

# Faites des prédictions sur l'ensemble de test
y_pred = knn.predict(X_test_scaled)

# Évaluez les performances du modèle
f1 = f1_score(y_test, y_pred, average='binary')  
print("F1 Score:", f1)
"""

from sklearn.model_selection import cross_val_score
import numpy as np

# Définir une liste de valeurs de k à tester
neighbors = list(range(1, 21))  # Tester k de 1 à 20

# Initialiser une liste pour stocker les scores F1 moyens pour chaque valeur de k
f1_scores = []

# Boucler à travers les valeurs de k
# Loop through the values of k
for k in neighbors:
    # Initialize the KNN classifier with the current value of k
    knn = KNeighborsClassifier(n_neighbors=k)
    
    # Perform cross-validation with 5 folds
    cv_scores = cross_val_score(knn, X_train_imputed, y_train, cv=5, scoring='f1')
    
    # Calculate the mean F1 score for this value of k
    mean_f1 = np.mean(cv_scores)
    
    # Add the mean F1 score to the list of scores
    f1_scores.append(mean_f1)

# Trouver la valeur de k avec le meilleur score F1
best_k = neighbors[np.argmax(f1_scores)]
best_f1_score = max(f1_scores)

print("Meilleur nombre de voisins (k) :", best_k)
print("Meilleur score F1 :", best_f1_score)


plt.plot(neighbors,f1_scores, color='blue', linewidth=3, label='f1 scores')
plt.xlabel('nombre de voisins')
plt.ylabel('f1 score selon le nombre de voisins')
plt.title('f1')
plt.ylim(0.5, 1)
plt.legend()
plt.show()
plt.savefig(path+'Partie2_ML/k plus proches voisins/'+'f1 score selon le nombre de voisins.png')
plt.show()

