"""
Utility functions for preparing to run models on data.
"""
import pandas as pd
import numpy as np


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
