import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

print("Original Data:")
print(df)

# 1. Remove duplicate rows
df = df.drop_duplicates()

# 2. Remove leading/trailing spaces from text columns
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

# 3. Replace common missing-value representations
df = df.replace(["?", "NA", "N/A", "null", ""], pd.NA)

# 4. Fill missing numeric values with median
numeric_cols = df.select_dtypes(include="number").columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# 5. Fill missing categorical values with mode
categorical_cols = df.select_dtypes(include="object").columns
for col in categorical_cols:
    if not df[col].mode().empty:
        df[col] = df[col].fillna(df[col].mode()[0])

# 6. Convert Age to numeric
if "Age" in df.columns:
    df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
    df["Age"] = df["Age"].fillna(df["Age"].median())

# 7. Remove invalid ages
if "Age" in df.columns:
    df = df[(df["Age"] >= 0) & (df["Age"] <= 100)]

# 8. Reset index
df = df.reset_index(drop=True)

# Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned Data:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nData Cleaning Completed!")