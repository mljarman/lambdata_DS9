"""
Utility functions for working specifically with DataFrames
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


# sample dataset:
SAMPLE_DF = pd.DataFrame(np.random.randint(0, 50, size=(10, 4)),
                                           columns=list('ABCD'))
SAMPLE_DF['E'] = pd.date_range('2019-11-1', periods=10, freq='D')


def date_splitter(df, column):
    """
    function to split dates into individual day, month, year columns.
    """
    pd.to_datetime(df[column], infer_datetime_format=True)
    df['year'] = df[column].dt.year
    df['month'] = df[column].dt.month
    df['day'] = df[column].dt.day


def set_splits(df, train_percent=.6, val_percent=.2, test_percent=.2,
               Random_State=None):
    """
    function to split data into train, test, val sets.
    """
    np.random.seed(Random_State)
    percent = train_percent + val_percent
    train, val, test = np.split(df.sample(frac=1), [int(train_percent*len(df)),
                                                    int(percent*len(df))])
    return train, val, test
