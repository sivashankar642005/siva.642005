import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Simulate a large dataset
np.random.seed(42)
data = pd.DataFrame({
    'Age': np.random.randint(0, 100, 100000),  # Ages from 0 to 99
    'Gender': np.random.choice(['Male', 'Female', 'Other'], 100000, p=[0.49, 0.49, 0.02])
})

# Plot 1: Distribution of Age (continuous variable)
plt.figure(figsize=(12, 6))
sns.histplot(data['Age'], bins=20, kde=False, color='skyblue')
plt.title('Distribution of Ages in Large Sample (n=100,000)')
plt.xlabel('Age')
plt.ylabel('Count')
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot 2: Distribution of Gender (categorical variable)
plt.figure(figsize=(6, 5))
sns.countplot(x='Gender', data=data, palette='Set2')
plt.title('Distribution of Genders in Large Sample (n=100,000)')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.grid(axis='y')
plt.tight_layout()
plt.show()
