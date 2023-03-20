import pandas
from . import TestCase
from business_rules.operators import DataframeType

class StringPartTests(TestCase):
    def test_equals_string_part(self):
        df = pandas.DataFrame.from_dict({
            "RDOMAIN": ["AE", "AE", "DX"],
            "dataset_name": ["SUPPAEQUAL","SUPPAEQUAL","SUPPAEQUAL"],
        })
        self.assertTrue(DataframeType({"value": df}).equals_string_part({
            "target": "RDOMAIN",
            "comparator": "dataset_name",
            "regex": ".{4}(..).*" # Get characters five and six of dataset name
        }).equals(pandas.Series([True, True, False])))
        self.assertTrue(DataframeType({"value": df}).equals_string_part({
            "target": "RDOMAIN",
            "comparator": "SUDXLL",
            "regex": ".{2}(..).*" # Get characters five and six of dataset name
        }).equals(pandas.Series([False, False, True])))
    
    def test_does_not_equal_string_part(self):
        df = pandas.DataFrame.from_dict({
            "RDOMAIN": ["AE", "AE", "DX"],
            "dataset_name": ["SUPPAEQUAL","SUPPAEQUAL","SUPPAEQUAL"],
        })
        self.assertTrue(DataframeType({"value": df}).does_not_equal_string_part({
            "target": "RDOMAIN",
            "comparator": "dataset_name",
            "regex": ".{4}(..).*" # Get characters five and six of dataset name
        }).equals(pandas.Series([False, False, True])))
        self.assertTrue(DataframeType({"value": df}).does_not_equal_string_part({
            "target": "RDOMAIN",
            "comparator": "SUDXLL",
            "regex": ".{2}(..).*" # Get characters five and six of dataset name
        }).equals(pandas.Series([True, True, False])))
