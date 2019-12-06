"""Lambdata is a collection of data science helper functions"""

import pandas as pd
import numpy as np

#import different pages so don't need to do it separately.
# import lambdata_mljarman.df_utils
# import lambdata_mljarman.for_models

# sample data:
ONES = pd.DataFrame(np.ones(10))
ZEROS = pd.DataFrame(np.zeros(50))
# sample dataset:
SAMPLE_DF = pd.DataFrame(np.random.randint(0, 50, size=(10, 4)),
                                           columns=list('ABCD'))
SAMPLE_DF['E'] = pd.date_range('2019-11-1', periods=10, freq='D')


# sample functions:
def increment(x):
    return (x + 1)

# sample class as given for assignment:
class Complex:
    """
    Consider the following class as a way to represent complex numbers.
    """
    def __init__(self, realpart, imagpart):
      self.r = realpart
      self.i = imagpart
    def sum_nums(self):
      """
      Find sum of realpart and imagpart.
      """
      return self.r+self.i
