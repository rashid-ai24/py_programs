import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("emails.csv")

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

df['email_length'] = df['text'].apply(len)

plt.figure(figsize=(10, 6))
sns.histplot(df['email_length'], bins=50, kde=True)
plt.title('Distribution of Email Lengths')
plt.xlabel('Email Length')
plt.ylabel('Frequency')
plt.show()

category_counts = df['spam'].value_counts()
plt.figure(figsize=(10, 6))
category_counts.plot(kind='bar')
plt.title('Email Categories')
plt.xlabel('Category')
plt.ylabel('Number of Emails')
plt.show()
