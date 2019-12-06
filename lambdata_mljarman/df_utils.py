"""
Utility functions for cleaning DataFrames
"""
import pandas as pd
import numpy as np

# helper functions:
def date_splitter(df, column):
    """
    Function to split dates into individual day, month, year columns.
    """
    pd.to_datetime(df[column], infer_datetime_format=True)
    df['year'] = df[column].dt.year
    df['month'] = df[column].dt.month
    df['day'] = df[column].dt.day
