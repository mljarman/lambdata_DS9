"""
Utility functions for preparing to run models on data.
"""
import pandas as pd
import numpy as np

#
# def set_splits(df, train_percent=.6, val_percent=.2, test_percent=.2,
#                Random_State=None):
#     """
#     function to split data into train, test, val sets.
#     """
#     np.random.seed(Random_State)
#     percent = train_percent + val_percent
#     train, val, test = np.split(df.sample(frac=1), [int(train_percent*len(df)),
#                                                     int(percent*len(df))])
#     return train, val, test

class Model_Prep:
    """
    Preparing dataset to run predictive models.
    """
    def __init__(self, df, train_percent, val_percent, test_percent, random_state):
        self.df = df
        self.train_percent = train_percent
        self.val_percent = val_percent
        self.test_percent = test_percent
        self.random_state = random_state

    def set_splits(self):
        """
        method to split data into train, test, val sets.
        """
        np.random.seed(self.random_state)
        percent = self.train_percent + self.val_percent
        train, val, test = np.split(df.sample(frac=1), [int(self.train_percent*len(self.df)),
                                                        int(percent*len(df))])
        return train, val, test
