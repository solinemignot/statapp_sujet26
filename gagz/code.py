#%%
import pandas as pd
import matplotlib.pyplot as plt

def caracteristiques():
    path="/home/onyxia/work/projet-python/"
    file_name1="caracteristiques_"+"2005"+".csv"
    df= pd.read_csv(path+file_name1, sep=',',low_memory=False)
    for year in range (2006,2023):
        file_name1="caracteristiques_"+str(year)+".csv"
        df2= pd.read_csv(path+file_name1, sep=',',low_memory=False)
        df=pd.concat([df,df2])
    return df

df=caracteristiques()
df=df.drop(['hrmn', 'agg', 'int','col', 'com', 'adr', 'gps', 'lat', 'long' , 'dep'],axis=1)

def lieux():
    path="/home/onyxia/work/projet-python/"
    file_name1="lieux_"+"2005"+".csv"
    df= pd.read_csv(path+file_name1, sep=',',low_memory=False)
    for year in range (2006,2023):
        file_name1="lieux_"+str(year)+".csv"
        df2= pd.read_csv(path+file_name1, sep=',',low_memory=False)
        df=pd.concat([df,df2])
    return df

df2=lieux()
df2=df2.drop(['catr', 'voie', 'v1', 'v2', 'circ', 'nbv', 'pr', 'pr1', 'vosp', 'prof', 'plan', 'lartpc', 'larrout', 'infra', 'situ', 'env1', 'vma'],axis=1)
df_merge=pd.merge(df,df2,on='Num_Acc')


# Assurez-vous que la colonne 'lum' est de type chaîne de caractères et supprimez les espaces blancs
df_merge['lum'] = df_merge['lum'].astype(str).str.strip()

# Normalisez les valeurs dans la colonne 'lum'
df_merge['lum'] = df_merge['lum'].replace({"1.0": "1", "2.0": "2", "3.0": "3", "4.0": "4", "5.0": "5"})

# Vérifiez les 10 premières lignes pour confirmer les modifications
print(df_merge.head(10))


import matplotlib.pyplot as plt

# Supposons que votre DataFrame s'appelle df et contient les colonnes 'an' et 'lum'

# Grouper les données par année et lumière, puis compter le nombre d'occurrences
grouped_data = df_merge.groupby(['an', 'lum']).size().unstack().fillna(0)

# Calculer les pourcentages pour chaque catégorie
grouped_data_percentage = grouped_data.div(grouped_data.sum(axis=1), axis=0) * 100

# Créer un graphique en barres empilées
grouped_data_percentage.plot(kind='bar', stacked=True, figsize=(12, 8))

# Ajouter des étiquettes et un titre
plt.title('Pourcentage des conditions d\'éclairage par année')
plt.xlabel('Année')
plt.ylabel('Pourcentage')
plt.legend(title='Lumière', bbox_to_anchor=(1.05, 1), loc='upper left')

# Afficher le graphique
plt.show()
# %%
