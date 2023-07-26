import pandas
from . import TestCase
from business_rules.operators import DataframeType

class PresentOnMultipleRowsWithin(TestCase):
    def test_present_on_multiple_rows_within(self):
        """
        Unit test for present_on_multiple_rows_within operator.
        """
        valid_df = pandas.DataFrame.from_dict(
            {
                "USUBJID": [1, 1, 1, 2, 2, 2, ],
                "SEQ": [1, 2, 3, 4, 5, 6],
                "RELID": ["AEHOSP1", "AEHOSP1", "AEHOSP1", "AEHOSP2", "AEHOSP2", "AEHOSP2"]
            }
        )
        result = DataframeType({"value": valid_df}).present_on_multiple_rows_within(
            {"target": "RELID", "within": "USUBJID", "comparator": 1}
        )
        self.assertTrue(result.equals(pandas.Series([True, True, True, True, True, True])))

        valid_df_1 = pandas.DataFrame.from_dict(
            {
                "USUBJID": [5, 5, 5, 7, 7, 7, ],
                "SEQ": [1, 2, 3, 4, 5, 6],
                "RELID": ["AEHOSP1", "AEHOSP1", "AEHOSP1", "AEHOSP2", "AEHOSP2", "AEHOSP2"]
            }
        )
        result = DataframeType({"value": valid_df_1}).present_on_multiple_rows_within(
            {"target": "RELID", "within": "USUBJID", "comparator": 2}
        )
        self.assertTrue(result.equals(pandas.Series([True, True, True, True, True, True])))

        invalid_df = pandas.DataFrame.from_dict(
            {
                "USUBJID": [1, 1, 1, 2, 2, 2, 3],
                "SEQ": [1, 2, 3, 4, 5, 6, 7],
                "RELID": ["AEHOSP1", "AEHOSP1", "AEHOSP1", "AEHOSP2", "AEHOSP2", "AEHOSP2", "AEHOSP3"]
            }
        )
        result = DataframeType({"value": invalid_df}).present_on_multiple_rows_within(
            {"target": "RELID", "within": "USUBJID", "comparator": 1}
        )
        self.assertTrue(result.equals(pandas.Series([True, True, True, True, True, True, False])))

    def test_present_on_multiple_rows_within_mixed_group(self):
        df = pandas.DataFrame.from_dict(
            {
                "USUBJID": [1, 1, 1, 2, 2, 2, 3, 3, 3],
                "DSDECOD": ["ICO", "ICO", "COMPLETE", "RANDOM", "RANDOM", "COMPLETE", "A", "B", "C"]
            }
        )
        result = DataframeType({"value": df}).present_on_multiple_rows_within(
            {"target": "DSDECOD", "within": "USUBJID"}
        )
        self.assertTrue(result.equals(pandas.Series([True, True, False, True, True, False, False, False, False])))

        # Comparator determines the max number of rows with the same value before an error is flagged.
        # In this case, comparator: 5 means that if a value is present on more than 5 rows within the grouping target an error should be raised. Since no values appear more than 5 times within a USUBJID no error should be raised.
        result = DataframeType({"value": df}).present_on_multiple_rows_within(
                {"target": "DSDECOD", "within": "USUBJID", "comparator": 5}
        )
        self.assertTrue(result.equals(pandas.Series([False, False, False, False, False, False, False, False, False])))

    def test_not_present_on_multiple_rows_within(self):
        """
        Unit test for not_present_on_multiple_rows_within operator.
        """
        valid_df = pandas.DataFrame.from_dict(
            {
                "USUBJID": [1, 1, 1, 2, 2, 2, ],
                "SEQ": [1, 2, 3, 4, 5, 6],
                "RELID": ["AEHOSP1", "AEHOSP1", "AEHOSP1", "AEHOSP2", "AEHOSP2", "AEHOSP2"]
            }
        )
        result = DataframeType({"value": valid_df}).not_present_on_multiple_rows_within(
            {"target": "RELID", "within": "USUBJID", "comparator": 1}
        )
        self.assertTrue(result.equals(pandas.Series([False, False, False, False, False, False])))

        invalid_df = pandas.DataFrame.from_dict(
            {
                "USUBJID": [1, 1, 1, 2, 2, 2, 3],
                "SEQ": [1, 2, 3, 4, 5, 6, 7],
                "RELID": ["AEHOSP1", "AEHOSP1", "AEHOSP1", "AEHOSP2", "AEHOSP2", "AEHOSP2", "AEHOSP3"]
            }
        )
        result = DataframeType({"value": invalid_df}).not_present_on_multiple_rows_within(
            {"target": "RELID", "within": "USUBJID", "comparator": 1}
        )
        self.assertTrue(result.equals(pandas.Series([False, False, False, False, False, False, True])))


