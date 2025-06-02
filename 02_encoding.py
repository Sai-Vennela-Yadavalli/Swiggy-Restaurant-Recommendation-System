import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import pickle
import os

# Load cleaned data
df = pd.read_csv("cleaned_data/cleaned_data.csv")

# Drop 'id', 'name', 'lic_no', 'link', 'address', 'menu'
df = df.drop(columns=['id', 'name', 'lic_no', 'link', 'address', 'menu'])

# Select categorical and numerical columns
categorical_cols = ['city', 'cuisine']
numerical_cols = ['rating', 'rating_count', 'cost']

# One-Hot Encoding
encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
encoded_cat = encoder.fit_transform(df[categorical_cols])

# Create DataFrame from encoded data
encoded_cat_df = pd.DataFrame(encoded_cat, columns=encoder.get_feature_names_out(categorical_cols))

# Combine with numerical data
encoded_df = pd.concat([encoded_cat_df.reset_index(drop=True), df[numerical_cols].reset_index(drop=True)], axis=1)

# Save encoded dataset
os.makedirs("cleaned_data", exist_ok=True)
encoded_df.to_csv("cleaned_data/encoded_data.csv", index=False)

# Save encoder
os.makedirs("encoder", exist_ok=True)
with open("encoder/encoder.pkl", "wb") as f:
    pickle.dump(encoder, f)

print("✅ Saved: cleaned_data/encoded_data.csv and encoder/encoder.pkl")