from pathlib import Path
import pandas as pd

from constants import constants
from model.person import Person

from werkzeug.datastructures import FileStorage
from io import StringIO

pd.set_option("future.no_silent_downcasting", True)


class DataHandler:
    def __init__(self, file_obj: FileStorage) -> None:
        self.file_obj = file_obj
        self._df = pd.DataFrame()

    def get(self) -> pd.DataFrame:
        string_io = StringIO(self.file_obj.read().decode("utf-8"))
        _df = self._read_csv(string_io)
        _df = self._clean_data(_df)
        self._df = _df

        return _df

    def get_people_array(self) -> list[Person]:
        people = []
        _df = self.get()

        for _, row in _df.iterrows():
            email = row["email"]
            year = row["year"]

            _preferences = [row["p1"], row["p2"], row["p3"]]
            _preferences = [pref for pref in _preferences if pd.notna(pref)]

            # Replace Kilmainham with City Centre - Southside
            _preferences = [
                "City Centre - Southside" if pref == "Kilmainham" else pref
                for pref in _preferences
            ]

            if len(_preferences) != 3:
                continue

            signup = row["signup"]
            leader = row["leader"]

            people.append(Person(email, year, list(set(_preferences)), signup, leader))

        return people

    def output(self, output_dir: Path) -> None:
        self._df.to_csv(output_dir, index=False)

    def _read_csv(self, string_io: StringIO) -> pd.DataFrame:
        return pd.read_csv(string_io)

    def _clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        _df = self._clean_columns(df)
        _df = self._clean_dtypes(_df)
        _df = self._remove_bad_rows(_df)
        _df = self._insert_leader_col(_df)

        return _df

    def _clean_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        _df = df.drop(columns=constants.COLUMNS_TO_DROP)
        _df.columns = pd.Index(constants.DF_COLUMNS)
        _df["signup"] = _df["signup"].replace(constants.SIGNUP_MAP)
        _df = _df[_df["signup"]]
        return _df

    def _clean_dtypes(self, df: pd.DataFrame) -> pd.DataFrame:
        return df.astype(constants.DTYPE_DICT)

    def _remove_bad_rows(self, df: pd.DataFrame) -> pd.DataFrame:
        _df = df.dropna(subset=["email"])
        _df = _df[_df["email"].str.contains("@ucd")]

        return _df

    def _insert_leader_col(self, df: pd.DataFrame) -> pd.DataFrame:
        df["leader"] = df["year"].isin(["UEM4"])
        return df
