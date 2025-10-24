import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

states = ['Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']

regions = ['South','Northeast','Northeast','North','Central','West','West','North','North','East','South','South','Central','West','Northeast','Northeast','Northeast','Northeast','East','North','West','Northeast','South','South','Northeast','North','North','East']

np.random.seed(42)
df = pd.DataFrame({
    'state': states,
    'first_dose': np.random.uniform(40, 80, len(states)),
})
df['fully_vaccinated'] = df['first_dose'] * np.random.uniform(0.8, 0.95, len(df))
df['booster_rate'] = df['fully_vaccinated'] * np.random.uniform(0.5, 0.8, len(df))
df['region'] = regions
df = df.sort_values('first_dose', ascending=False)

top_states = df.head(15).melt(id_vars=['state'], value_vars=['first_dose','fully_vaccinated'], var_name='type', value_name='rate')
sns.barplot(data=top_states, x='state', y='rate', hue='type', palette='Set2')
plt.title('First Dose vs Fully Vaccinated (Top 15 States)')
plt.xticks(rotation=60)
plt.show()

sns.scatterplot(data=df, x='first_dose', y='booster_rate', hue='region', s=100)
for x, y, label in zip(df['first_dose'], df['booster_rate'], df['state']):
    plt.text(x+0.3, y+0.3, label, fontsize=8)
plt.title('First Dose vs Booster Rate')
plt.show()

top_10 = df.head(10).set_index('state')[['first_dose','fully_vaccinated','booster_rate']]
sns.heatmap(top_10, annot=True, fmt='.1f', cmap='YlOrRd', linewidths=0.5)
plt.title('Vaccination Rates Heatmap - Top 10 States')
plt.show()
