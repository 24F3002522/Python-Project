import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("students.csv")

print("Original Shape:", df.shape)

# 1. Standardize column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# 2. Remove duplicate records
df.drop_duplicates(inplace=True)

# 3. Clean string columns
text_cols = df.select_dtypes(include="object").columns

for col in text_cols:
    df[col] = df[col].astype("string").str.strip().str.lower()

# 4. Replace invalid/missing values
invalid_values = ["?", "na", "n/a", "null", "none", "-", ""