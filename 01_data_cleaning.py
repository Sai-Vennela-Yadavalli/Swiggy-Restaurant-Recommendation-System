import pandas as pd
import os

# Load dataset using absolute path (update if needed)
df = pd.read_csv(r"C:\Users\Sai Vennela Jagadesh\OneDrive\Documents\Guvi Capstone Projects\Swiggy_recommendation_system\data\swiggy.csv")

# Drop rows with missing values in key columns
df.dropna(subset=["name", "rating", "rating_count", "cost", "cuisine"], inplace=True)

# Clean 'rating' column
df['rating'] = df['rating'].replace('--', None)
df.dropna(subset=['rating'], inplace=True)
df['rating'] = df['rating'].astype(float)

# Clean 'rating_count' column (e.g., "100+ ratings" → 100)
df['rating_count'] = df['rating_count'].str.extract(r'(\d+)')
df.dropna(subset=['rating_count'], inplace=True)
df['rating_count'] = df['rating_count'].astype(float)

# Clean 'cost' column (remove ₹ and convert to float)
df['cost'] = df['cost'].str.replace('₹', '', regex=False).str.strip()
df.dropna(subset=['cost'], inplace=True)
df['cost'] = df['cost'].astype(float)

# Reset index
df.reset_index(drop=True, inplace=True)

# Ensure output directory exists
os.makedirs("cleaned_data", exist_ok=True)

# Save cleaned data
df.to_csv("cleaned_data/cleaned_data.csv", index=False)
print("✅ Cleaned data saved to cleaned_data/cleaned_data.csv")
