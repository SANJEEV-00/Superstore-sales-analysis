import pandas as pd
df = pd.read_csv('Sample - Superstore.csv')
# Sales by category
df.groupby('Category')['Sales'].sum().plot(kind='bar')