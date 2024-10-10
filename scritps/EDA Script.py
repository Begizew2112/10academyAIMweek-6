import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# Load cleaned data
df_cleaned = pd.read_csv('cleaned.csv')

# Basic statistics
print(df_cleaned.describe())

# Distribution of the numerical columns
df_cleaned.hist(bins=30, figsize=(10, 8))
plt.tight_layout()
plt.show()

# Correlation matrix for numerical variables
plt.figure(figsize=(10, 8))
sns.heatmap(df_cleaned.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# Countplot for categorical columns (e.g., FraudResult, PricingStrategy)
plt.figure(figsize=(10, 6))
sns.countplot(data=df_cleaned, x='FraudResult')
plt.title('Fraud Result Distribution')
plt.show()

