import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('C:\Users\Yibabe\Desktop\10 academyAIM week_6\data\data.csv')

# Ensure 'TransactionStartTime' is in datetime format
df['TransactionStartTime'] = pd.to_datetime(df['TransactionStartTime'])

# Drop any unnecessary columns that have strings or irrelevant features
columns_to_drop = ['ProductCategory', 'TransactionId', 'BatchId', 'AccountId', 'SubscriptionId', 'CustomerId', 'CurrencyCode', 'CountryCode', 'ProviderId']
df_cleaned = df.drop(columns=columns_to_drop)

# Handle missing values
df_cleaned = df_cleaned.dropna()  # or use fillna() if you want to fill missing values

# Convert categorical features to appropriate types if necessary
df_cleaned['PricingStrategy'] = df_cleaned['PricingStrategy'].astype('category')
df_cleaned['FraudResult'] = df_cleaned['FraudResult'].astype('category')

# Save the cleaned data
df_cleaned.to_csv('cleaned_data.csv', index=False)

