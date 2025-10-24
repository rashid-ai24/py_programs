import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(42)
student_data = pd.DataFrame({
    'Gender': np.random.choice(['Male', 'Female'], 100, replace=True),
    'Math_Score': np.random.normal(65, 15, 100),
    'Reading_Score': np.random.normal(70, 10, 100),
    'Writing_Score': np.random.normal(68, 12, 100),
    'Prep_Course': np.random.choice(['Completed', 'None'], 100, replace=True)
})

print("Sample Data:")
print(student_data.head())

# Plot 1: Histogram
sns.histplot(student_data['Math_Score'], bins=10, kde=True, color='steelblue')
plt.title('Distribution of Math Scores')
plt.show()

# Plot 2: Boxplot by Gender
sns.boxplot(data=student_data, x='Gender', y='Math_Score')
plt.title('Math Scores by Gender')
plt.show()

# Plot 3: Violin plot for Reading Score by Prep Course
sns.violinplot(data=student_data, x='Prep_Course', y='Reading_Score', inner='quartile')
plt.title('Reading Scores by Test Preparation Course')
plt.show()

# Plot 4: Scatter plot for Math vs Reading Score
sns.scatterplot(data=student_data, x='Math_Score', y='Reading_Score', hue='Gender')
plt.title('Math vs Reading Scores')
plt.show()

# Average Score
student_data['Average_Score'] = student_data[['Math_Score', 'Reading_Score', 'Writing_Score']].mean(axis=1)
sns.boxplot(data=student_data, x='Prep_Course', y='Average_Score')
plt.title('Average Scores by Test Preparation Course')
plt.show()
