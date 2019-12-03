"""
utility functions for working specifically with DataFrames
"""
# sample data:
SAMPLE_DF = pd.DataFrame(np.random.randint(0, 50, size=(10,4)), columns=list('ABCD'))
SAMPLE_DF['E'] = pd.date_range('2019-11-1', periods=10, freq='D')

# helper functions

# function to split dates into day, month, year columns:
def date_splitter(df, column):
  # make sure column is in datetime format:
  pd.to_datetime(df[column], infer_datetime_format=True)
  # make year column
  df['year'] = df[column].dt.year
  # make month column
  df['month'] = df[column].dt.month
  # make day column
  df['day'] = df[column].dt.day

 # function to split data into train, test, val sets:
 def set_splits(df, train_percent=.6, val_percent=.2, test_percent=.2, Random_State=None):
     np.random.seed(Random_State)
     percent = train_percent + val_percent
     train, val, test = np.split(df.sample(frac=1), [int(train_percent*len(df)),
     int(percent*len(df))])
     return train, val, test
