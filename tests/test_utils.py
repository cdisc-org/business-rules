from . import TestCase
from business_rules.utils import flatten_list
import pandas as pd

class UtilitiyTests(TestCase):
    """ Test utility functions
    """
    def test_flatten_list_array_in_dataframe(self):
        """ Flatten list should return the array values if a value in the list argument is:
                1. A column in the dataset
                2. The column in is a column of arrays
        """
        data = pd.DataFrame.from_dict({
            "ARRAYDATA": [[1,2,4], [1,2,4], [1,2,4]],
            "STRINGDATA": ["A", "B", "C"]
        })
        
        assert list(flatten_list(data, ["ARRAYDATA"])) == [1,2,4]
    
    def test_flatten_list(self):
        """ Flatten list should return the column name, if a value in the list argument is:
                1. A column in the dataset
                2. Not a column of arrays
        """
        data = pd.DataFrame.from_dict({
            "ARRAYDATA": [[1,2,4], [1,2,4], [1,2,4]],
            "STRINGDATA": ["A", "B", "C"]
        })
        
        assert list(flatten_list(data, ["STRINGDATA"])) == ["STRINGDATA"]
