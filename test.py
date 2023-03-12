import pandas as pd
import numpy as np


filename = "replace.csv" # "validus_tas_crypto_ETH-31MAR23.csv"

df = pd.read_csv(filename, parse_dates=['Timestamp'])

df.replace("NA", np.nan, inplace=True) # This needs numpy

df.head(20)

df.shape

df.info()


df[['Timestamp', 'Symbol', 'Side', 'BidPrice', 'AskPrice']]

df.iloc[0]  # First row of a data frame


df.iloc[9]  #(i+1)th row 

df.iloc[-1] # Last row 

df.iloc[:, 0]  # First column

df.iloc[:, -1] # Last column 

df.iloc[0:7]       #First 7 rows 

df.iloc[:, 0:2]    #First 2 columns

df.iloc[1:3, 0:2]  #Second through third rows and first 2 columns

df.iloc[[0,5], [1,3]]  #1st and 6th rows and 2nd and 4th columns

#Select rows by their labels:
df.loc[10:20,['Timestamp','Symbol','BidPrice', 'AskPrice']]

#Select rows by their labels:
df.iloc[10:20,[0, 2, 3, 7, 8]]

#Select only those rows that contain female professors:
#Preferred notation
df = df.loc[lambda df: df['Type'] == 'replace' ]  # fill, order, cancel, replace, 

df = df.loc[lambda df: df['Type'] == 'order' ]  # fill, order, cancel, replace, 

# print unique values from a column
print(df['Type'].unique())

# write all values from column to list
list = df['Type'].tolist()

print(list)

#Old notation
df[df['Type'] == 'cancel' ]

#Calculate mean salary for each professor rank:
df.groupby('Side')[['TradePrice']].mean()

# Select the rows that have at least one missing value
df[df.isnull().any(axis=1)].head()

# Select the rows that have at least none missing value
df[df.notnull().any(axis=1)].head()

df = df.loc[lambda df: df['Type'] == 'fill' ]

# Remove columns where name is 'BidPrice' and 'BidQty' etc.
df = df.drop(['BidPrice', 'BidQty', 'AskPrice', 'AskQty', 'Venue', 'DisplayVenue', 'SenderSubID', 'TargetSubID', 'ManualOrder'], axis=1)

# Remove columns with NaN values
# Whether to drop labels from the index (0 or ‘index’) or columns (1 or ‘columns’).
# Optional, default 'any'. Specifies whether to remove the row or column when ALL values are NULL, or if ANY value is NULL.
df.dropna(axis='columns', how='all', inplace=True)

# Remove rows with NaN values
# Whether to drop labels from the index (0 or ‘index’) or columns (1 or ‘columns’).
# Optional, default 'any'. Specifies whether to remove the row or column when ALL values are NULL, or if ANY value is NULL.
df.dropna(axis='index', how='any')

# EXPORT TO FILE
# Export data from dataframe into a CSV file.
df.to_csv("replace.csv", index=False, header=True)

# Max on every row
df.max(axis = 0, skipna = True)


df.sort_values('TradePrice')

df.max(axis = 0)

df.isna()

df.fillna(0)

df.dtypes

df.loc[0, 'Timestamp']

# df.loc[0, 'Timestamp'].day_name()

df['Timestamp'] = pd.to_datetime(df['Timestamp'])

df['Timestamp'].min()

df['Timestamp'].max()

# df['Timestamp'].max() - df['Timestamp'].min()


# Voorbeeld van het omzetten van uur data naar week data
df.resample('W').agg({'Close': 'mean', 'High': 'max', 'Low': 'min', 'Volume': 'sum'})


# EXPORT TO DATABASE
# write dataframe to table in sql database
from sqlalchemy import create_engine
import psycopg2

engine = create_engine("postgresql+psycopg2://0x01:@localhost:5432/sample_db")

# dataframe to table command
df.to_sql('sample_tbl' , engine)
