from sklearn.preprocessing import LabelEncoder
import pandas as pd
# Load cleaned data
df_cleaned = pd.read_csv('cleaned.csv')

# Encode categorical variables
encoder = LabelEncoder()

# Apply encoding to categorical columns
df_cleaned['FraudResult_Encoded'] = encoder.fit_transform(df_cleaned['FraudResult'])
df_cleaned['PricingStrategy_Encoded'] = encoder.fit_transform(df_cleaned['PricingStrategy'])

# Save the encoded dataset
df_cleaned.to_csv('encoded_data.csv', index=False)
