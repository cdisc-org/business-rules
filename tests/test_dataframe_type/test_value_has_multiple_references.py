import pandas as pd
from . import TestCase
from business_rules.operators import DataframeType

class ValueHasMultipleReferencesTests(TestCase):
    def test_value_has_multiple_references(self):
        df = pd.DataFrame.from_dict({
            "LNKGRP": ["A", "B", "A", "A", "A"],
            "$VALUE_COUNTS": [
                {"A": 2, "B": 1},
                {"A": 2, "B": 1},
                {"A": 2, "B": 1},
                {"A": 2, "B": 1},
                {"A": 2, "B": 1},
            ]
        })
        result = DataframeType({"value": df}).value_has_multiple_references({"target": "LNKGRP", "comparator": "$VALUE_COUNTS"})
        self.assertTrue(result.equals(pd.Series([True, False, True, True, True])))

    def test_value_does_not_have_multiple_references(self):
        df = pd.DataFrame.from_dict({
            "LNKGRP": ["A", "B", "A", "A", "A"],
            "$VALUE_COUNTS": [
                {"A": 2, "B": 1},
                {"A": 2, "B": 1},
                {"A": 2, "B": 1},
                {"A": 2, "B": 1},
                {"A": 2, "B": 1},
            ]
        })
        result = DataframeType({"value": df}).value_does_not_have_multiple_references({"target": "LNKGRP", "comparator": "$VALUE_COUNTS"})
        self.assertTrue(result.equals(pd.Series([False, True, False, False, False])))