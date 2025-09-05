import pandas as pd

# Load CSV
df = pd.read_csv("List of Orders.csv")

# Preview data
print("Initial data preview:")
print(df.head())

# -------------------------
# 1. Remove duplicates
# -------------------------
df = df.drop_duplicates()
print("\nDuplicates removed.")

# -------------------------
# 2. Handle missing values
# -------------------------
# Fill missing CustomerName, State, City with 'Unknown'
df['CustomerName'] = df['CustomerName'].fillna('Unknown')
df['State'] = df['State'].fillna('Unknown')
df['City'] = df['City'].fillna('Unknown')

# Drop rows with missing Order ID or Order Date
df = df.dropna(subset=['Order ID', 'Order Date'])

# -------------------------
# 3. Correct data types
# -------------------------
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True, errors='coerce')

# -------------------------
# 4. Standardize text columns
# -------------------------
df['CustomerName'] = df['CustomerName'].str.strip().str.title()
df['State'] = df['State'].str.strip().str.title()
df['City'] = df['City'].str.strip().str.title()

# -------------------------
# 5. Create additional columns
# -------------------------
df['Month'] = df['Order Date'].dt.month
df['Year'] = df['Order Date'].dt.year

# -------------------------
# 6. Save cleaned CSV
# -------------------------
df.to_csv("List_of_Orders_Cleaned.csv", index=False)
print("\nData cleaned and saved as 'List_of_Orders_Cleaned.csv'")
