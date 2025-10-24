import pandas as pd
import seaborn as sns
from scipy.stats import skew

df_red = pd.read_csv("winequality-red.csv", delimiter=";")
df_white = pd.read_csv("winequality-white.csv", delimiter=";")

print(df_red.dtypes)
print(df_red.describe())
print(df_red.info())

sns.countplot(df_red, x="quality")
sns.histplot(df_red['alcohol'], kde=True)
print("Skewness of alcohol:", skew(df_red['alcohol']))
