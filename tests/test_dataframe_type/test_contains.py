import pandas
from . import TestCase
from business_rules.operators import DataframeType

class ContainsTests(TestCase):
    def test_contains(self):
        df = pandas.DataFrame.from_dict({
            "var1": [1,2,4],
            "var2": [3,5,6],
            "var3": [1,3,8],
            "var4": [1,2,4],
            "string_var": ["h/j", "word", "c"],
            "var5": [[1,3,5],[1,3,5], [1,3,5]]
        })
        self.assertTrue(DataframeType({"value": df}).contains({
            "target": "var1",
            "comparator": 2
        }).equals(pandas.Series([False, True, False])))
        self.assertTrue(DataframeType({"value": df}).contains({
            "target": "var1",
            "comparator": "var3"
        }).equals(pandas.Series([True, False, False])))
        self.assertTrue(DataframeType({"value": df, "column_prefix_map": {"--": "va"}}).contains({
            "target": "var1",
            "comparator": "--r3"
        }).equals(pandas.Series([True, False, False])))
        self.assertTrue(DataframeType({"value": df}).contains({
            "target": "var1",
            "comparator": "var2"
        }).equals(pandas.Series([False, False, False])))
        self.assertTrue(DataframeType({"value": df}).contains({
            "target": "string_var",
            "comparator": "string_var"
        }).equals(pandas.Series([True, True, True])))
        self.assertTrue(DataframeType({"value": df}).contains({
            "target": "string_var",
            "comparator": "string_var",
            "value_is_literal": True
        }).equals(pandas.Series([False, False, False])))
        self.assertTrue(DataframeType({"value": df}).contains({
            "target": "var5",
            "comparator": "var1"
        }).equals(pandas.Series([True, False, False])))
        self.assertTrue(DataframeType({"value": df}).contains({
            "target": "string_var",
            "comparator": "/",
            "value_is_literal": True
        }).equals(pandas.Series([True, False, False])))

    def test_does_not_contain(self):
        df = pandas.DataFrame.from_dict({
            "var1": [1,2,4],
            "var2": [3,5,6],
            "var3": [1,3,8],
            "var4": [1,2,4],
            "string_var": ["hj", "word", "c"],
            "var5": [[1,3,5],[1,3,5], [1,3,5]]
        })
        self.assertTrue(DataframeType({"value": df}).does_not_contain({
            "target": "var1",
            "comparator": 5
        }).equals(pandas.Series([True, True, True])))
        self.assertTrue(DataframeType({"value": df}).does_not_contain({
            "target": "var1",
            "comparator": "var3"
        }).equals(pandas.Series([False, True, True])))
        self.assertTrue(DataframeType({"value": df, "column_prefix_map": {"--": "va"}}).does_not_contain({
            "target": "var1",
            "comparator": "--r3"
        }).equals(pandas.Series([False, True, True])))
        self.assertTrue(DataframeType({"value": df}).does_not_contain({
            "target": "var1",
            "comparator": "var2"
        }).equals(pandas.Series([True, True, True])))
        self.assertTrue(DataframeType({"value": df}).does_not_contain({
            "target": "string_var",
            "comparator": "string_var",
            "value_is_literal": True
        }).equals(pandas.Series([True, True, True])))
        self.assertTrue(DataframeType({"value": df}).does_not_contain({
            "target": "string_var",
            "comparator": "string_var"
        }).equals(pandas.Series([False, False, False])))
        self.assertTrue(DataframeType({"value": df}).does_not_contain({
            "target": "var5",
            "comparator": "var1"
        }).equals(pandas.Series([False, True, True])))


    def test_contains_case_insensitive(self):
        df = pandas.DataFrame.from_dict({
            "var1": ["pikachu", "charmander", "squirtle"],
            "var2": ["PIKACHU", "CHARIZARD", "BULBASAUR"],
            "var3": ["POKEMON", "CHARIZARD", "BULBASAUR"],
            "var4": [
                        ["pikachu", "charizard", "bulbasaur"],
                        ["chikorita", "cyndaquil", "totodile"],
                        ["chikorita", "cyndaquil", "totodile"]
                    ]
        })
        self.assertTrue(DataframeType({"value": df}).contains_case_insensitive({
            "target": "var1",
            "comparator": "PIKACHU"
        }).equals(pandas.Series([True, False, False])))
        self.assertTrue(DataframeType({"value": df}).contains_case_insensitive({
            "target": "var1",
            "comparator": "var2"
        }).equals(pandas.Series([True, False, False])))
        self.assertTrue(DataframeType({"value": df, "column_prefix_map": {"--": "va"}}).contains_case_insensitive({
            "target": "--r1",
            "comparator": "--r2"
        }).equals(pandas.Series([True, False, False])))
        self.assertTrue(DataframeType({"value": df}).contains_case_insensitive({
            "target": "var1",
            "comparator": "var3"
        }).equals(pandas.Series([False, False, False])))
        self.assertTrue(DataframeType({"value": df}).contains_case_insensitive({
            "target": "var3",
            "comparator": "var3"
        }).equals(pandas.Series([True, True, True])))
        self.assertTrue(DataframeType({"value": df}).contains_case_insensitive({
            "target": "var3",
            "comparator": "var3",
            "value_is_literal": True
        }).equals(pandas.Series([False, False, False])))
        self.assertTrue(DataframeType({"value": df}).contains_case_insensitive({
            "target": "var4",
            "comparator": "var2"
        }).equals(pandas.Series([True, False, False])))

    def test_does_not_contain_case_insensitive(self):
        df = pandas.DataFrame.from_dict({
            "var1": ["pikachu", "charmander", "squirtle"],
            "var2": ["PIKACHU", "CHARIZARD", "BULBASAUR"],
            "var3": ["pikachu", "charizard", "bulbasaur"],
            "var4": [
                        ["pikachu", "charizard", "bulbasaur"],
                        ["chikorita", "cyndaquil", "totodile"],
                        ["chikorita", "cyndaquil", "totodile"]
                    ]
        })
        self.assertTrue(DataframeType({"value": df}).does_not_contain_case_insensitive({
            "target": "var1",
            "comparator": "IVYSAUR"
        }).equals(pandas.Series([True, True, True])))
        self.assertTrue(DataframeType({"value": df}).does_not_contain_case_insensitive({
            "target": "var3",
            "comparator": "var2"
        }).equals(pandas.Series([False, False, False])))
        self.assertTrue(DataframeType({"value": df}).does_not_contain_case_insensitive({
            "target": "var3",
            "comparator": "var3",
            "value_is_literal": True
        }).equals(pandas.Series([True, True, True])))
        self.assertTrue(DataframeType({"value": df}).does_not_contain_case_insensitive({
            "target": "var3",
            "comparator": "var3"
        }).equals(pandas.Series([False, False, False])))
        self.assertTrue(DataframeType({"value": df}).does_not_contain_case_insensitive({
            "target": "var4",
            "comparator": "var2"
        }).equals(pandas.Series([False, True, True])))

    def test_contains_all(self):
        df = pandas.DataFrame.from_dict(
            {
                "var1": ['test', 'value', 'word'],
                "var2": ["test", "value", "test"],
                "variable_names": ["STUDYID", "USUBJID", "COOLVAR"],
                "required_variables": [["STUDYID", "USUBJID"], ["STUDYID", "USUBJID"], ["STUDYID", "USUBJID"]]
            }
        )
        self.assertTrue(DataframeType({"value": df}).contains_all({
            "target": "var1",
            "comparator": "var2",
        }))
        self.assertTrue(DataframeType({"value": df, "column_prefix_map": {"--": "va"}}).contains_all({
            "target": "--r1",
            "comparator": "--r2",
        }))
        self.assertFalse(DataframeType({"value": df}).contains_all({
            "target": "var2",
            "comparator": "var1",
        }))
        self.assertTrue(DataframeType({"value": df}).contains_all({
            "target": "var2",
            "comparator": ["test", "value"],
        }))

        self.assertTrue(DataframeType({"value": df}).contains_all({
            "target": "variable_names",
            "comparator": ["required_variables"]
        }))

    def test_not_contains_all(self):
        df = pandas.DataFrame.from_dict(
            {
                "var1": ['test', 'value', 'word'],
                "var2": ["test", "value", "test"],
                "variable_names": ["STUDYID", "USUBJID", "COOLVAR"],
                "required_variables": [["STUDYID", "USUBJID", "TEST"], ["STUDYID", "USUBJID", "TEST"], ["STUDYID", "USUBJID", "TEST"]]
            }
        )
        
        self.assertTrue(DataframeType({"value": df}).not_contains_all({
            "target": "variable_names",
            "comparator": ["required_variables"]
        }))
