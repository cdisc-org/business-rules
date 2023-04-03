from business_rules.operators import DataframeType
import pandas
from . import TestCase


class IsUniqueSetTests(TestCase):
    def test_is_unique_set(self):
        df = pandas.DataFrame.from_dict(
            {
                "ARM": ["PLACEBO", "PLACEBO", "A", "A"],
                "TAE": [1, 1, 1, 2],
                "LAE": [1, 2, 1, 2],
                "ARF": [1, 2, 3, 4],
            }
        )
        df_type = DataframeType({"value": df})
        self.assertTrue(
            df_type.is_unique_set({"target": "ARM", "comparator": "LAE"}).equals(
                pandas.Series([True, True, True, True])
            )
        )
        self.assertTrue(
            df_type.is_unique_set({"target": "ARM", "comparator": ["LAE"]}).equals(
                pandas.Series([True, True, True, True])
            )
        )
        self.assertTrue(
            df_type.is_unique_set({"target": "ARM", "comparator": ["TAE"]}).equals(
                pandas.Series([False, False, True, True])
            )
        )
        self.assertTrue(
            df_type.is_unique_set(
                {"target": "ARM", "comparator": ["TAE", "NOT_IN_DS"]}
            ).equals(pandas.Series([False, False, True, True]))
        )
        self.assertTrue(
            df_type.is_unique_set({"target": "ARM", "comparator": "TAE"}).equals(
                pandas.Series([False, False, True, True])
            )
        )

        df_type = DataframeType({"value": df, "column_prefix_map": {"--": "AR"}})
        self.assertTrue(
            df_type.is_unique_set({"target": "--M", "comparator": "--F"}).equals(
                pandas.Series([True, True, True, True])
            )
        )
        self.assertTrue(
            df_type.is_unique_set({"target": "--M", "comparator": ["--F"]}).equals(
                pandas.Series([True, True, True, True])
            )
        )

    def test_is_not_unique_set(self):
        df = pandas.DataFrame.from_dict(
            {
                "ARM": ["PLACEBO", "PLACEBO", "A", "A"],
                "TAE": [1, 1, 1, 2],
                "LAE": [1, 2, 1, 2],
                "ARF": [1, 2, 3, 4],
            }
        )
        df_type = DataframeType({"value": df})
        self.assertTrue(
            df_type.is_not_unique_set({"target": "ARM", "comparator": "LAE"}).equals(
                pandas.Series([False, False, False, False])
            )
        )
        self.assertTrue(
            df_type.is_not_unique_set({"target": "ARM", "comparator": ["LAE"]}).equals(
                pandas.Series([False, False, False, False])
            )
        )
        self.assertTrue(
            df_type.is_not_unique_set({"target": "ARM", "comparator": ["TAE"]}).equals(
                pandas.Series([True, True, False, False])
            )
        )
        self.assertTrue(
            df_type.is_not_unique_set(
                {"target": "ARM", "comparator": ["TAE", "NOT_IN_DS"]}
            ).equals(pandas.Series([True, True, False, False]))
        )
        self.assertTrue(
            df_type.is_not_unique_set({"target": "ARM", "comparator": "TAE"}).equals(
                pandas.Series([True, True, False, False])
            )
        )

        df_type = DataframeType({"value": df, "column_prefix_map": {"--": "AR"}})
        self.assertTrue(
            df_type.is_not_unique_set({"target": "--M", "comparator": "--F"}).equals(
                pandas.Series([False, False, False, False])
            )
        )
        self.assertTrue(
            df_type.is_not_unique_set({"target": "--M", "comparator": ["--F"]}).equals(
                pandas.Series([False, False, False, False])
            )
        )
