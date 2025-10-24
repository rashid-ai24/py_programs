import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
data = {
    "Week": pd.date_range(start="2023-01-01", periods=12, freq="W"),
    "Store_ID": np.random.choice([101, 102, 103], size=12),
    "Weekly_Sales": np.random.randint(10000, 30000, size=12),
    "Promotion": np.random.choice([0, 1], size=12),
    "Holiday_Week": np.random.choice([0, 1], size=12)
}
df = pd.DataFrame(data)

df.groupby("Week")["Weekly_Sales"].sum().plot(marker='o')
plt.title("Total Weekly Sales Over Time")
plt.show()

df.groupby("Store_ID")["Weekly_Sales"].mean().plot(kind='bar')
plt.title("Average Weekly Sales by Store")
plt.show()

df.groupby("Promotion")["Weekly_Sales"].mean().plot(kind='bar', color=['red', 'green'])
plt.xticks([0, 1], ['No Promotion', 'Promotion Active'])
plt.show()

sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
