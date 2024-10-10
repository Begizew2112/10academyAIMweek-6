from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import woe

# Load RFMS scores
rfms_df = pd.read_csv('rfms_scores.csv')

# Create a binary label for classification (Good/Bad)
# Example: Classify as 'Good' if RFMS_Score > median
rfms_df['Risk_Label'] = np.where(rfms_df['RFMS_Score'] > rfms_df['RFMS_Score'].median(), 1, 0)

# Prepare data for WoE binning
X = rfms_df[['Recency', 'Frequency', 'Monetary']]
y = rfms_df['Risk_Label']

# WoE Binning (Assuming 'woe' library is installed)
binning = woe.binning.WOE()
woe_bins = binning.fit_transform(X, y)

# Convert bins into a DataFrame and display
woe_df = pd.DataFrame(woe_bins, columns=['Recency_WoE', 'Frequency_WoE', 'Monetary_WoE'])

# Save the WoE binned data
woe_df.to_csv('woe_binned_data.csv', index=False)
