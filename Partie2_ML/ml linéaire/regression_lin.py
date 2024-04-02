import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.impute import SimpleImputer

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

df.to_csv("/home/onyxia/work/statapp_sujet26/Partie2_ML/ml linéaire/"+'svm_dummies.csv', index=False)

y = df['grav']
X = df.drop(columns=['grav'])
features = X.columns

# Diviser le jeu de données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

"""#Inférer les valeurs non renseignées
imputer = SimpleImputer(strategy='mean')
X_train_imp = imputer.fit_transform(X_train)
X_test_imp = imputer.transform(X_test)

#Ajuster Y pour fitter avec la nouvelle base de features
# Convert NumPy arrays back to pandas DataFrames after imputation
X_train_imp_df = pd.DataFrame(X_train_imp, columns=X_train.columns, index=X_train.index)
X_test_imp_df = pd.DataFrame(X_test_imp, columns=X_test.columns, index=X_test.index)

# Adjust y_train and y_test to align with the new feature sets
y_train = y_train.loc[X_train_imp_df.index]
y_test = y_test.loc[X_test_imp_df.index]"""


#Créer le modèle linéaire et l'entrainer sur les bases test
model = LinearRegression()
model.fit(X_train, y_train)

#Tester le modèle sur la base de features test
y_pred = model.predict(X_test)

"""plt.scatter(X_test_imp[:,6], y_test, color='black', label='Actual Data')
plt.plot(X_test_imp[:,6], y_pred, color='blue', linewidth=3, label='Regression Line')
plt.xlabel('Feature')
plt.ylabel('Gravity')
plt.legend()
plt.show()"""

# Évaluer les performances du modèle
r2 = r2_score(y_test, y_pred)
print("R2:", r2)

# On récupère les coefficients
coefficients = model.coef_

# Les associer à leur feature 
feature_importance = list(zip(features, coefficients))

for feature, importance in feature_importance:
    print(f"{feature}: {importance}")


