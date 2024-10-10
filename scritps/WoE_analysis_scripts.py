import pandas as pd

# Load the encoded data
df_cleaned = pd.read_csv('final_cleaned.csv')

# Ensure 'TransactionStartTime' is in datetime format
df_cleaned['TransactionStartTime'] = pd.to_datetime(df_cleaned['TransactionStartTime'])

def compute_rfms(df):
    # Set the reference date (e.g., today’s date or max transaction date in the dataset)
    today_date = df['TransactionStartTime'].max()
    
    # Calculate Recency: difference between today's date and the last transaction for each customer
    recency = (today_date - df.groupby('CustomerId_Encoded')['TransactionStartTime'].max()).dt.days
    
    # Calculate Frequency: count of transactions per customer
    frequency = df.groupby('CustomerId_Encoded')['TransactionId'].count()
    
    # Calculate Monetary: sum of amounts spent per customer
    monetary = df.groupby('CustomerId_Encoded')['Amount'].sum()
    
    # Create a new DataFrame for RFMS scores
    rfms = pd.DataFrame({
        'Recency': recency,
        'Frequency': frequency,
        'Monetary': monetary
    }).reset_index()
    
    return rfms

# Apply the RFMS computation
rfms_df = compute_rfms(df_cleaned)

# Assign RFMS scores
rfms_df['RFMS_Score'] = rfms_df['Recency'] + rfms_df['Frequency'] + rfms_df['Monetary']

# Save the RFMS scores
rfms_df.to_csv('rfms_scores.csv', index=False)
