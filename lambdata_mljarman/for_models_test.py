import unittest
from for_models import Model_Prep
from __init__ import SAMPLE_DF


class Model_Prep_Test(unittest.TestCase):
    """
    Test train, val, test split method
    """
    def test_set_splits(self):
        mods = Model_Prep(SAMPLE_DF)
        train, val, test = mods.set_splits()
        target_sizes = [(SAMPLE_DF.shape[0]*.6, SAMPLE_DF.shape[1]),
                        (SAMPLE_DF.shape[0]*.2, SAMPLE_DF.shape[1]),
                        (SAMPLE_DF.shape[0]*.2, SAMPLE_DF.shape[1])]
        result_sizes = [train.shape, val.shape, test.shape]
        self.assertListEqual(target_sizes, result_sizes)


if __name__ == '__main__':
    unittest.main()
