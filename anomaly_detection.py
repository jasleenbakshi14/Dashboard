import pandas as pd

df = pd.read_csv('../data/cleaned_logs.csv')

#Flag failed login spikes
df['failed_login'] = ((df['event_type'] == 'login') & (df['status'] == 'fail')).astype(int)

#Group by day
daily_fails = df.groupby(df['timestamp'].str[:10])['failed_login'].sum()

#Threshold for anomaly (mean + 2*std)
threshold = daily_fails.mean() + 2 * daily_fails.std()

anomalies = daily_fails[daily_fails > threshold]
print("Anomalous days:\n", anomalies)
