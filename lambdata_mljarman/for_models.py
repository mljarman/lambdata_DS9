"""
Utility functions for preparing to run models on data.
"""
import pandas as pd
import numpy as np


class Model_Prep:
    """
    Preparing dataset to run predictive models.
    """
    def __init__(self, df, train_percent =.6, val_percent =.2, test_percent =.2,
                random_state = 42):
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
        train, val, test = np.split(df.sample(frac=1), [int(self.train_percent*
                                                        len(self.df)),int(percent*len(df))])
        return train, val, test
