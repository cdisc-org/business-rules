import pandas
from . import TestCase
from business_rules.operators import DataframeType

class NumericComparisonTests(TestCase):
    def test_less_than(self):
        df = pandas.DataFrame.from_dict({
            "var1": [1,2,4],
            "var2": [3,5,6],
            "var3": [1,3,8],
            "var4": [1,2,4],
            "var5": ["1", "3", "5"],
            "var6": ["ad", "ab", "al"]
        })
        self.assertTrue(DataframeType({"value": df}).less_than({
            "target": "var1",
            "comparator": "var4"
        }).equals(pandas.Series([False, False, False])))
        self.assertTrue(DataframeType({"value": df}).less_than({
            "target": "var1",
            "comparator": "var3"
        }).equals(pandas.Series([False, True, True])))
        self.assertTrue(DataframeType({"value": df}).less_than({
            "target": "var4",
            "comparator": "var5"
        }).equals(pandas.Series([False, True, True])))
        self.assertTrue(DataframeType({"value": df}).less_than({
            "target": "var5",
            "comparator": "var6"
        }).equals(pandas.Series([False, False, False])))
        self.assertTrue(DataframeType({"value": df, "column_prefix_map": {"--": "va"}}).less_than({
            "target": "--r1",
            "comparator": "var3"
        }).equals(pandas.Series([False, True, True])))
        self.assertTrue(DataframeType({"value": df}).less_than({
            "target": "var2",
            "comparator": 2
        }).equals(pandas.Series([False, False, False])))
        self.assertTrue(DataframeType({"value": df}).less_than({
            "target": "var1",
            "comparator": 3
        }).equals(pandas.Series([True, True, False])))

        another_df = pandas.DataFrame.from_dict(
            {
                "LBDY": [4, None, None, None, None]
            }
        )
        self.assertTrue(DataframeType({"value": another_df}).less_than({
            "target": "LBDY",
            "comparator": 5
        }).equals(pandas.Series([True, False, False, False, False, ])))
    
    def test_less_than_or_equal_to(self):
        df = pandas.DataFrame.from_dict({
            "var1": [1,2,4],
            "var2": [3,5,6],
            "var3": [1,3,8],
            "var4": [1,2,4],
            "var5": ["1", "3", "5"],
            "var6": ["ad", "ab", "al"]
        })
        self.assertTrue(DataframeType({"value": df}).less_than_or_equal_to({
            "target": "var1",
            "comparator": "var4"
        }).equals(pandas.Series([True, True, True])))
        self.assertTrue(DataframeType({"value": df, "column_prefix_map": {"--": "va"}}).less_than_or_equal_to({
            "target": "--r1",
            "comparator": "var4"
        }).equals(pandas.Series([True, True, True])))
        self.assertTrue(DataframeType({"value": df}).less_than_or_equal_to({
            "target": "var2",
            "comparator": "var1"
        }).equals(pandas.Series([False, False, False])))
        self.assertTrue(DataframeType({"value": df}).less_than_or_equal_to({
            "target": "var2",
            "comparator": 2
        }).equals(pandas.Series([False, False, False])))
        self.assertTrue(DataframeType({"value": df}).less_than_or_equal_to({
            "target": "var2",
            "comparator": "var3"
        }).equals(pandas.Series([False, False, True])))

        another_df = pandas.DataFrame.from_dict(
            {
                "LBDY": [4, 5, None, None, None]
            }
        )
        self.assertTrue(DataframeType({"value": another_df}).less_than_or_equal_to({
            "target": "LBDY",
            "comparator": 5
        }).equals(pandas.Series([True, True, False, False, False, ])))
        self.assertTrue(DataframeType({"value": df}).less_than_or_equal_to({
            "target": "var4",
            "comparator": "var5"
        }).equals(pandas.Series([True, True, True])))
        self.assertTrue(DataframeType({"value": df}).less_than_or_equal_to({
            "target": "var5",
            "comparator": "var6"
        }).equals(pandas.Series([False, False, False])))
    
    def test_greater_than(self):
        df = pandas.DataFrame.from_dict({
            "var1": [1,2,4],
            "var2": [3,5,6],
            "var3": [1,3,8],
            "var4": [1,2,4],
            "var5": ["1", "3", "5"],
            "var6": ["ad", "ab", "al"]
        })
        self.assertTrue(DataframeType({"value": df}).greater_than({
            "target": "var1",
            "comparator": "var4"
        }).equals(pandas.Series([False, False, False])))
        self.assertTrue(DataframeType({"value": df}).greater_than({
            "target": "var1",
            "comparator": "var3"
        }).equals(pandas.Series([False, False, False])))
        self.assertTrue(DataframeType({"value": df, "column_prefix_map": {"--": "va"}}).greater_than({
            "target": "var1",
            "comparator": "--r3"
        }).equals(pandas.Series([False, False, False])))
        self.assertTrue(DataframeType({"value": df}).greater_than({
            "target": "var2",
            "comparator": 2
        }).equals(pandas.Series([True, True, True])))
        self.assertTrue(DataframeType({"value": df}).greater_than({
            "target": "var1",
            "comparator": 5000
        }).equals(pandas.Series([False, False, False])))

        another_df = pandas.DataFrame.from_dict(
            {
                "LBDY": [4, None, None, None, None]
            }
        )
        self.assertTrue(DataframeType({"value": another_df}).greater_than({
            "target": "LBDY",
            "comparator": 3
        }).equals(pandas.Series([True, False, False, False, False, ])))
        self.assertTrue(DataframeType({"value": df}).greater_than({
            "target": "var5",
            "comparator": "var4"
        }).equals(pandas.Series([False, True, True])))
        self.assertTrue(DataframeType({"value": df}).greater_than({
            "target": "var5",
            "comparator": "var6"
        }).equals(pandas.Series([False, False, False])))
    
    def test_greater_than_or_equal_to(self):
        df = pandas.DataFrame.from_dict({
            "var1": [1,2,4],
            "var2": [3,5,6],
            "var3": [1,3,8],
            "var4": [1,2,4],
            "var5": ["1", "3", "5"],
            "var6": ["ad", "ab", "al"]
        })
        self.assertTrue(DataframeType({"value": df}).greater_than_or_equal_to({
            "target": "var1",
            "comparator": "var4"
        }).equals(pandas.Series([True, True, True])))
        self.assertTrue(DataframeType({"value": df, "column_prefix_map": {"--": "va"}}).greater_than_or_equal_to({
            "target": "var1",
            "comparator": "--r4"
        }).equals(pandas.Series([True, True, True])))
        self.assertTrue(DataframeType({"value": df}).greater_than_or_equal_to({
            "target": "var2",
            "comparator": "var3"
        }).equals(pandas.Series([True, True, False])))
        self.assertTrue(DataframeType({"value": df}).greater_than_or_equal_to({
            "target": "var2",
            "comparator": 2
        }).equals(pandas.Series([True, True, True])))

        another_df = pandas.DataFrame.from_dict(
            {
                "LBDY": [4, 3, None, None, None]
            }
        )
        self.assertTrue(DataframeType({"value": another_df}).greater_than_or_equal_to({
            "target": "LBDY",
            "comparator": 3
        }).equals(pandas.Series([True, True, False, False, False, ])))
        
        self.assertTrue(DataframeType({"value": df}).greater_than_or_equal_to({
            "target": "var5",
            "comparator": "var4"
        }).equals(pandas.Series([True, True, True])))
        self.assertTrue(DataframeType({"value": df}).greater_than_or_equal_to({
            "target": "var5",
            "comparator": "var6"
        }).equals(pandas.Series([False, False, False])))
        self.assertTrue(DataframeType({"value": df}).greater_than_or_equal_to({
            "target": "var6",
            "comparator": "var6"
        }).equals(pandas.Series([False, False, False])))
