import pandas
from . import TestCase
from business_rules.operators import DataframeType

class PrefixSuffixContainedByTests(TestCase):
    def test_prefix_is_contained_by(self):
        df = pandas.DataFrame.from_dict({
            "var1": ["AETEST", "AETESTCD", "LBTEST"],
            "var2": ["AETEST", "AFTESTCD", "RRTEST"],
            "study_domains": [
                ["DM","AE","LB","TV"],
                ["DM","AE","LB","TV"],
                ["DM","AE","LB","TV"],
            ]
        })
        self.assertTrue(DataframeType({"value": df}).prefix_is_contained_by({
            "target": "var1",
            "comparator": "study_domains",
            "prefix": 2
        }).equals(pandas.Series([True, True, True])))

        self.assertTrue(DataframeType({"value": df}).prefix_is_contained_by({
            "target": "var2",
            "comparator": "study_domains",
            "prefix": 2
        }).equals(pandas.Series([True, False, False])))
    
    def test_suffix_is_contained_by(self):
        df = pandas.DataFrame.from_dict({
            "var1": ["AETEST", "AETESTCD", "LBTEGG"],
            "var2": ["AETEST", "AFTESTCD", "RRTELE"],
            "study_domains": [
                ["ST","CD","GG","TV"],
                ["ST","CD","GG","TV"],
                ["ST","CD","GG","TV"],
            ]
        })
        self.assertTrue(DataframeType({"value": df}).suffix_is_contained_by({
            "target": "var1",
            "comparator": "study_domains",
            "suffix": 2
        }).equals(pandas.Series([True, True, True])))

        self.assertTrue(DataframeType({"value": df}).suffix_is_contained_by({
            "target": "var2",
            "comparator": "study_domains",
            "suffix": 2
        }).equals(pandas.Series([True, True, False])))
 
    def test_suffix_is_not_contained_by(self):
        df = pandas.DataFrame.from_dict({
            "var1": ["AETEST", "AETESTCD", "LBTEGG"],
            "var2": ["AETEST", "AFTESTCD", "RRTELE"],
            "study_domains": [
                ["ST","CD","GG","TV"],
                ["ST","CD","GG","TV"],
                ["ST","CD","GG","TV"],
            ]
        })
        self.assertTrue(DataframeType({"value": df}).suffix_is_not_contained_by({
            "target": "var1",
            "comparator": "study_domains",
            "suffix": 2
        }).equals(pandas.Series([False, False, False])))

        self.assertTrue(DataframeType({"value": df}).suffix_is_not_contained_by({
            "target": "var2",
            "comparator": "study_domains",
            "suffix": 2
        }).equals(pandas.Series([False, False, True])))
 
    def test_prefix_is_not_contained_by(self):
        df = pandas.DataFrame.from_dict({
            "var1": ["AETEST", "AETESTCD", "LBTEST"],
            "var2": ["AETEST", "AFTESTCD", "RRTEST"],
            "study_domains": [
                ["DM","AE","LB","TV"],
                ["DM","AE","LB","TV"],
                ["DM","AE","LB","TV"],
            ]
        })
        self.assertTrue(DataframeType({"value": df}).prefix_is_not_contained_by({
            "target": "var1",
            "comparator": "study_domains",
            "prefix": 2
        }).equals(pandas.Series([False, False, False])))

        self.assertTrue(DataframeType({"value": df}).prefix_is_not_contained_by({
            "target": "var2",
            "comparator": "study_domains",
            "prefix": 2
        }).equals(pandas.Series([False, True, True])))
 
