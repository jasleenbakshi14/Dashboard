import pandas as pd

df = pd.read_csv('../data/sample_logs.csv')

#Clean and preprocess
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['user'] = df['user'].str.lower()
df.dropna(inplace=True)

#Save cleaned data
df.to_csv('../data/cleaned_logs.csv', index=False)
print("Data cleaned and saved.")
