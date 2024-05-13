import pandas as pd
import matplotlib.pyplot as plt

path = "/home/onyxia/work/statapp_sujet26/"
file_name1 = "dataset_complet_part_1.csv"
file_name2 = "dataset_complet_part_2.csv"
df1 = pd.read_csv(path + file_name1, sep=',', low_memory=False)
df2 = pd.read_csv(path + file_name2, sep=',', low_memory=False)
df = pd.concat([df1, df2])
df = df[df['an'] == 2019]  # Filter data for the year 2019
df['grav'] = df['grav'].replace({'1': 0, '2': 0, '3': 1, '4': 1, 1: 0, 2: 0, 3: 1, 4: 1}).astype(int)

# Select relevant columns and ensure 'lum' column is string and strip whitespaces
df = df[['an', 'grav', 'lum']]
df['lum'] = df['lum'].astype(str).str.strip()
df['lum'] = df['lum'].replace({"1.0": "1", "2.0": "2", "3.0": "3", "4.0": "4", "5.0": "5"})

# Define legend labels
legend_labels = ['Plein jour', 'Crépuscule ou aube', 'Nuit sans éclairage public', 
                 'Nuit avec éclairage public non allumé', 'Nuit avec éclairage public allumé']
"""
for gr in (0, 1):
    df_gravity = df[df['grav'] == gr].dropna(subset=['lum', 'an'])  # Filter by gravity and remove NaN values
    df_gravity = df_gravity[df_gravity['lum'] != '-1.0']  # Remove rows with invalid 'lum' values

    # Group data by year and lighting condition, then calculate percentages
    grouped_data = df_gravity.groupby(['an', 'lum']).size().unstack(fill_value=0)
    grouped_data_percentage = grouped_data.div(grouped_data.sum(axis=1), axis=0) * 100

    # Plot the stacked bar chart
    ax = grouped_data_percentage.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='viridis')

    # Add labels and title
    plt.title('Conditions d\'éclairage lors des accidents routiers pour la gravité ' + str(gr))
    plt.xlabel('Année')
    plt.ylabel('Pourcentage')
    plt.xticks(rotation=45)
    plt.yticks(fontsize=10)

    # Add legend with customized labels
    ax.legend(legend_labels, title='Condition d\'éclairage', title_fontsize=10, fontsize=8, bbox_to_anchor=(1.04, 1), loc='upper left')

    # Annotate percentages in the bars
    for i, (index, row) in enumerate(grouped_data_percentage.iterrows()):
        for lum, percentage in row.items():
            if percentage > 0.5:  # Threshold for displaying percentages
                ax.text(i, row[:lum].sum() + percentage / 2, f'{percentage:.1f}%', ha='center', va='center', color='white', fontsize=6)

    # Save the figure
    plt.savefig(path + 'stat_des2/eclairage_grav_' + str(gr) + '.png', dpi=300, bbox_inches='tight')
    plt.show()"""
import pandas as pd
import matplotlib.pyplot as plt
import textwrap

# Filter data and replace numeric codes with descriptive labels
df = df[df['lum'] != '-1.0']  # Remove rows with invalid 'lum' values
df['lum'] = df['lum'].replace({"1.0": "1", "2.0": "2", "3.0": "3", "4.0": "4", "5.0": "5"})
df['lum'] = df['lum'].replace({'1': 'Plein jour', '2': 'Crépuscule ou aube', '3': 'Nuit sans éclairage public',
                               '4': 'Nuit avec éclairage public non allumé', '5': 'Nuit avec éclairage public allumé'})

# Group data by gravity and lighting conditions, then count occurrences
graph_df = df.groupby(['grav', 'lum']).size().reset_index(name='accident_count')
graph_df = graph_df.pivot(index='lum', columns='grav', values='accident_count').fillna(0)

print(graph_df)
percentage_grav0= [round(graph_df.loc[i,0]/(graph_df.loc[i,0]+graph_df.loc[i,1])*100,2) for i in ['Plein jour','Crépuscule ou aube','Nuit sans éclairage public','Nuit avec éclairage public non allumé','Nuit avec éclairage public allumé']]
percentage_grav1= [round(graph_df.loc[i,1]/(graph_df.loc[i,0]+graph_df.loc[i,1])*100,2) for i in ['Plein jour','Crépuscule ou aube','Nuit sans éclairage public','Nuit avec éclairage public non allumé','Nuit avec éclairage public allumé']]

print(percentage_grav0)
print(percentage_grav1)

# Plot the bar chart
plt.figure(figsize=(10, 6))
ax = graph_df.plot(kind='bar', stacked=False)

# Customize labels and title
plt.xlabel('Condition d\'éclairage')
plt.ylabel('Nombre d\'accidents')
plt.title('Nombre d\'accidents par condition d\'éclairage selon la gravité')

# Add legend
plt.legend(title='Gravité')
labels = [textwrap.fill(label, 15) for label in graph_df.index]
plt.xticks(range(len(labels)), labels, rotation=0, fontsize=8)

# Save the figure
plt.savefig(path + 'stat_des2/' + 'condition_eclairage_2019.png', bbox_inches='tight')
plt.show()










































