import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("data.csv")

print("Original Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())

# 1. Remove duplicate rows
df = df.drop_duplicates()

# 2. Remove leading/trailing spaces from column names
df.columns = df.columns.str.strip()

# 3. Remove extra spaces from text columns
text_columns = df.select_dtypes(include="object").columns

for col in text_columns:
    df[col] = df[col].str.strip()

# 4. Convert empty strings to NaN
df.replace(r'^\s*$', np.nan, regex=True, inplace=True)

# 5. Fill missing numerical values with median
numeric_columns = df.select_dtypes(include=np.number).columns

for col in numeric_columns:
    df[col] = df[col].fillna(df[col].median())

# 6. Fill missing categorical values with mode
categorical_columns = df.select_dtypes(include="object").columns

for col in categorical_columns:
    if df[col].notna().any():
        df[col] = df[col].fillna(df[col].mode()[0])

# 7. Convert numeric-looking columns to numbers
for col in df.columns:
    if df[col].dtype == "object":
        converted = pd.to_numeric(df[col], errors="coerce")

        # Convert only if most values can be interpreted as numbers
        if converted.notna().mean() > 0.8:
            df[col] = converted

# 8. Remove extreme outliers using IQR
numeric_columns = df.select_dtypes(include=np.number).columns

for col in numeric_columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    df = df[
        (df[col] >= lower_bound) &
        (df[col] <= upper_bound)
    ]

# 9. Reset index
df.reset_index(drop=True, inplace=True)

# 10. Check cleaned data
print("\nCleaned Shape:", df.shape)
print("\nRemaining Missing Values:")
print(df.isnull().sum())

print("\nCleaned Data:")
print(df.head())

# 11. Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

print("\nData cleaning completed successfully!")