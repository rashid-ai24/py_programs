import pandas as pd

# Create sample dataset
feedback_df = pd.DataFrame({
    'CustomerID': [101, 102, 103, None, 105, 106],
    'Feedback': ['Good service', 'bad Service!!', None, '  excellent!! ', 'Average ', ''],
    'Rating': [5, 1, None, 5, 3, 2],
    'Gender': ['Male', 'Female', 'F', 'female', 'MALE', 'M']
})

print("Original Data:")
print(feedback_df)

# Clean column names
feedback_df = feedback_df.rename(columns={'CustomerID': 'Customer_ID'})

# Clean feedback text
feedback_df['Feedback'] = feedback_df['Feedback'].fillna('').str.strip().str.capitalize().str.replace(r'[^\w\s]', '', regex=True)

# Normalize gender values
feedback_df['Gender'] = feedback_df['Gender'].str.lower().replace({'m': 'male', 'f': 'female'})
feedback_df['Gender'] = feedback_df['Gender'].apply(lambda g: 'Male' if g == 'male' else ('Female' if g == 'female' else 'Other'))

# Filter out missing and invalid data
feedback_df = feedback_df.dropna(subset=['Customer_ID'])
feedback_df = feedback_df[feedback_df['Feedback'] != '']
feedback_df = feedback_df.dropna(subset=['Rating'])
feedback_df = feedback_df[feedback_df['Rating'] >= 3]

print("\nCleaned Data:")
print(feedback_df)
