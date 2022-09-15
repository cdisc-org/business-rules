import pandas as pd
from . import TestCase
from business_rules.operators import DataframeType

class VariableMetadataEqualityTests(TestCase):
    def test_variable_metadata_equal_to(self):
        df = pd.DataFrame.from_dict({
            "STUDYID": [1, 1, 1, 1],
            "$CORE_VALUES": [
                {"STUDYID": "Req", "DOMAIN": "Req"},
                {"STUDYID": "Req", "DOMAIN": "Req"},
                {"STUDYID": "Req", "DOMAIN": "Req"},
                {"STUDYID": "Req", "DOMAIN": "Req"}
            ]
        })
        result = DataframeType({"value": df}).variable_metadata_equal_to({"target": "STUDYID", "comparator": "Exp", "metadata": "$CORE_VALUES"})
        self.assertTrue(result.equals(pd.Series([False, False, False, False])))
        result = DataframeType({"value": df}).variable_metadata_equal_to({"target": "STUDYID", "comparator": "Req", "metadata": "$CORE_VALUES"})
        self.assertTrue(result.equals(pd.Series([True, True, True, True])))
    
    def test_variable_metadata_equal_to(self):
        df = pd.DataFrame.from_dict({
            "STUDYID": [1, 1, 1, 1],
            "$CORE_VALUES": [
                {"STUDYID": "Req", "DOMAIN": "Req"},
                {"STUDYID": "Req", "DOMAIN": "Req"},
                {"STUDYID": "Req", "DOMAIN": "Req"},
                {"STUDYID": "Req", "DOMAIN": "Req"}
            ]
        })
        result = DataframeType({"value": df}).variable_metadata_not_equal_to({"target": "STUDYID", "comparator": "Exp", "metadata": "$CORE_VALUES"})
        self.assertTrue(result.equals(pd.Series([True, True, True, True])))
        result = DataframeType({"value": df}).variable_metadata_not_equal_to({"target": "STUDYID", "comparator": "Req", "metadata": "$CORE_VALUES"})
        self.assertTrue(result.equals(pd.Series([False, False, False, False])))