import pandas
from . import TestCase
from business_rules.operators import DataframeType

class ValidDateTests(TestCase):
    def test_invalid_date(self):
        df = pandas.DataFrame.from_dict(
            {
                "var1": ['2021', '2021', '2021', '2021', '2099', "2022", "2023"],
                "var2": ["2099", "2022", "2034", "90999", "20999", "2022", "2023"],
                "var2.1": ["20220311", "2022", "20121123", "2022-03-11T09", "2099", "2022", "2023"],
                "var3": ["1997-07", "1997-07-16", "1997-07-16T19:20:30.45+01:00", "1997-07-16T19:20:30+01:00", "1997-07-16T19:20+01:00", "2022-05-08T13:44:a", "2022-05-08T13:44:66"], 
            }
        )
        self.assertTrue(DataframeType({"value": df, "column_prefix_map": {"--": "va"}}).invalid_date({"target": "--r1"})
            .equals(pandas.Series([False, False, False, False, False, False, False])))
        self.assertTrue(DataframeType({"value": df}).invalid_date({"target": "var3"})
            .equals(pandas.Series([False, False, False, False, False, True, True])))
        self.assertTrue(DataframeType({"value": df}).invalid_date({"target": "var2"})
            .equals(pandas.Series([False, False, False, True, True, False, False])))

        # Test date string can be parsed into a date
        # Ex: 20121123 cannot be parsed into a date so it is invalid
        self.assertTrue(DataframeType({"value": df}).invalid_date({"target": "var2.1"})
                        .equals(pandas.Series([False, False, False, False, False, False, False])))
    def test_invalid_date_incorrect_month_day_values(self):
        df = pandas.DataFrame.from_dict(
            {
                "var3": ["1997-23", "1997-07-44", "1997-00-16T19:20:30+01:00", "1997-07-32T19:20:30+01:00", "1997-02-30"], 
            }
        )
        self.assertTrue(DataframeType({"value": df}).invalid_date({"target": "var3"})
                    .equals(pandas.Series([True, True, True, True, True])))
