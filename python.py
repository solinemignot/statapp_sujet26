import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path="/home/onyxia/projet-python/"


def dataset_per_year(year):
    file_name_characteristics = f"caracteristiques_{year}.csv"
    df_characteristics = pd.read_csv(path + file_name_characteristics, sep=',', low_memory=False)

    file_name_locations = f"lieux_{year}.csv"
    df_locations = pd.read_csv(path + file_name_locations, sep=',', low_memory=False)
    df = pd.merge(df_characteristics, df_locations, on='Num_Acc')

    file_name_users = f"usagers_{year}.csv"
    df_users = pd.read_csv(path + file_name_users, sep=',', low_memory=False)
    df_users = df_users[df_users['grav'] != 'grav']

    if int(year) < 2019:
        df_users['grav'] = df_users['grav'].replace({2: 4, 4: 2, '2': 4, '4': 2, '1': 1, '3': 3}).infer_objects(copy=False)
        df_users['grav'] = pd.to_numeric(df_users['grav'], errors='coerce')  # Convert to numeric
    if int(year)>2018:
        df_users['grav'] = df_users['grav'].replace({'4': 4, '2': 2, '1': 1, '3': 3}).infer_objects(copy=False)
        df_users['grav'] = df_users['grav'].replace({2: 4, 4: 2})
        df_users['grav'] = pd.to_numeric(df_users['grav'], errors='coerce')  # Convert to numeric

    grav_df = df_users.groupby('Num_Acc')['grav'].max().reset_index()
    df = pd.merge(df, grav_df, on='Num_Acc')
    df = df.drop_duplicates()

    return df


def complete_dataset():
    df=dataset_per_year("2005")
    for i in range (2006,2019):
        df=pd.concat([df,dataset_per_year(i)])
        print(i)
    df=df.drop('env1',axis=1)
    for i in range (2019,2023):
        df=pd.concat([df,dataset_per_year(i)])
        print(i)
    return df

df=complete_dataset()
df['catr'] = pd.to_numeric(df['catr'], errors='coerce')

"""
graph_df = df.groupby(['grav', 'catr']).size().reset_index(name='accident_count')
graph_df = graph_df.pivot(index='grav', columns='catr', values='accident_count')

# Plot the lines for each gravity type
plt.figure(figsize=(10, 6))

for gravity_type in graph_df.index:
    plt.plot(graph_df.columns, graph_df.loc[gravity_type], label=f'Gravity {gravity_type}')

plt.xlabel('Type of Road (catr)')
plt.ylabel('Number of Accidents')
plt.title('Number of Accidents for Each Type of Road by Gravity Type')
plt.legend()
plt.show()
"""

num_rows = len(df)
midpoint = num_rows // 2
df_part1 = df.iloc[:midpoint]
df_part2 = df.iloc[midpoint:]

df_part1.to_csv(path+'dataset_complet_part_1.csv', index=False)
df_part2.to_csv(path+'dataset_complet_part_2.csv', index=False)

print((df.isna().mean() * 100).round(2))





