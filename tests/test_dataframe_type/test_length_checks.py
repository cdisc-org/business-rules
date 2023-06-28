from . import TestCase
import pandas as pd
from business_rules.operators import DataframeType

class LengthCheckTests(TestCase):
    def test_has_equal_length(self):
        df = pd.DataFrame.from_dict(
            {
                "var_1": ['test', 'value'],
                "col": ["alex", "val"],
                "int_col": [4, 5],
            }
        )
        df_operator = DataframeType({"value": df, "column_prefix_map": {"--": "va"}})
        result = df_operator.has_equal_length({"target": "--r_1", "comparator": 4})
        self.assertTrue(result.equals(pd.Series([True, False])))

        result = df_operator.has_equal_length({"target": "var_1", "comparator": "col"})
        self.assertTrue(result.equals(pd.Series([True, False])))
        
        result = df_operator.has_equal_length({"target": "var_1", "comparator": "int_col"})
        self.assertTrue(result.equals(pd.Series([True, True])))

    def test_has_not_equal_length(self):
        df = pd.DataFrame.from_dict(
            {
                "var_1": ['test', 'value'],
                "col": ["alex", "val"],
                "int_col": [4, 7]
            }
        )
        df_operator = DataframeType({"value": df, "column_prefix_map": {"--": "va"}})
        result = df_operator.has_not_equal_length({"target": "--r_1", "comparator": 4})
        self.assertTrue(result.equals(pd.Series([False, True])))

        result = df_operator.has_not_equal_length({"target": "var_1", "comparator": "col"})
        self.assertTrue(result.equals(pd.Series([False, True])))
        
        result = df_operator.has_not_equal_length({"target": "var_1", "comparator": "int_col"})
        self.assertTrue(result.equals(pd.Series([False, True])))

    def test_longer_than(self):
        df = pd.DataFrame.from_dict(
            {
                "var_1": ['test', 'value'],
                "col": ["a", "long text"],
                "int_col": [18, 2]
            }
        )
        df_operator = DataframeType({"value": df, "column_prefix_map": {"--": "va"}})
        self.assertTrue(df_operator.longer_than({"target": "--r_1", "comparator": 3}).equals(pd.Series([True, True])))
        self.assertTrue(df_operator.longer_than({"target": "--r_1", "comparator": "col"}).equals(pd.Series([True, False])))
        self.assertTrue(df_operator.longer_than({"target": "--r_1", "comparator": "int_col"}).equals(pd.Series([False, True])))

    def test_longer_than_or_equal_to(self):
        df = pd.DataFrame.from_dict(
            {
                "var_1": ['test', 'alex'],
                "col": ["sh", "test"],
                "int_col": [4, 17]           
            }
        )
        df_operator = DataframeType({"value": df, "column_prefix_map": {"--": "va"}})
        self.assertTrue(df_operator.longer_than_or_equal_to({"target": "--r_1", "comparator": 3}).equals(pd.Series([True, True])))
        self.assertTrue(df_operator.longer_than_or_equal_to({"target": "var_1", "comparator": 4}).equals(pd.Series([True, True])))
        self.assertTrue(df_operator.longer_than_or_equal_to({"target": "var_1", "comparator": "col"}).equals(pd.Series([True, True])))
        self.assertTrue(df_operator.longer_than_or_equal_to({"target": "--r_1", "comparator": "int_col"}).equals(pd.Series([True, False])))

    def test_shorter_than(self):
        df = pd.DataFrame.from_dict(
            {
                "var_1": ['test', 'val'],
                "col": ["longg", "abc"],
                "int_col": [25, 3],
            }
        )
        df_operator = DataframeType({"value": df, "column_prefix_map": {"--": "va"}})
        self.assertTrue(df_operator.shorter_than({"target": "--r_1", "comparator": 5}).equals(pd.Series([True, True])))
        self.assertTrue(df_operator.shorter_than({"target": "--r_1", "comparator": "col"}).equals(pd.Series([True, False])))
        self.assertTrue(df_operator.shorter_than({"target": "--r_1", "comparator": "int_col"}).equals(pd.Series([True, False])))

    def test_shorter_than_or_equal_to(self):
        df = pd.DataFrame.from_dict(
            {
                "var_1": ['test', 'alex'],
                "col": ["longg", "test"],
                "int_col": [25, 2],
            }
        )
        df_operator = DataframeType({"value": df, "column_prefix_map": {"--": "va"}})
        self.assertTrue(df_operator.shorter_than_or_equal_to({"target": "--r_1", "comparator": 5}).equals(pd.Series([True, True])))
        self.assertTrue(df_operator.shorter_than_or_equal_to({"target": "var_1", "comparator": 4}).equals(pd.Series([True, True])))
        self.assertTrue(df_operator.shorter_than_or_equal_to({"target": "var_1", "comparator": "col"}).equals(pd.Series([True, True])))
        self.assertTrue(df_operator.shorter_than_or_equal_to({"target": "var_1", "comparator": "int_col"}).equals(pd.Series([True, False])))
