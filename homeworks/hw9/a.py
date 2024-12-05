import pandas as pd

# Step 1: Load the CSV file
file_path = 'netflix_titles.csv'  # Replace with the correct file path
df = pd.read_csv(file_path)

# Step 2: Clean the 'date_added' column by removing leading/trailing spaces
df['date_added'] = df['date_added'].str.strip()

# Step 3: Convert 'date_added' to datetime format, handling any invalid dates with 'coerce'
df['date_added'] = pd.to_datetime(df['date_added'], format="%B %d, %Y", errors="coerce")

# Step 4: Check for rows where 'date_added' is NaT (Not a Time) and handle them
invalid_dates = df[df['date_added'].isna()]
if not invalid_dates.empty:
    print("Invalid date entries found:")
    print(invalid_dates)

# Step 5: Print the cleaned dataframe or save to a new CSV
print(df.head())  # Preview the cleaned dataframe
# Optionally, save to a new CSV file
# df.to_csv('cleaned_netflix_titles.csv', index=False)
