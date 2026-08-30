import pandas as pd
import numpy as np

# ==============================
# 1. LOAD DATA
# ==============================

df = pd.read_csv("customers.csv")

print("Initial Shape:", df.shape)
print("\nData Types:\n", df.dtypes)


# ==============================
# 2. STANDARDIZE COLUMN NAMES
# ==============================

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(r"[^a-z0-9]+", "_", regex=True)
    .str.strip("_")
)


# ==============================
# 3. REMOVE DUPLICATES
# ==============================

before = len(df)

df.drop_duplicates(inplace=True)

print("\nDuplicates Removed:", before - len(df))


# ==============================
# 4. HANDLE MISSING VALUES
# ==============================

# Replace common invalid values
missing_values = [
    "", " ", "na", "n/a", "null",
    "none", "unknown", "?", "-",