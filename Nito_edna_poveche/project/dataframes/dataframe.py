from abc import ABC, abstractmethod
import pandas as pd


class BaseDataframe(ABC):

    def __init__(self, name: str, path: str):
        self.name = name
        self.path = path

    def show_first_ten_rows(self):
        df = pd.read_csv(self.path)
        return df.head(10)

    def import_to_df(self):
        df = pd.read_csv(self.path)
        return df

    def df_to_dictionary(self):
        df = self.import_to_df()
        dictionary = {}
        for i in range(len(df)):
            key = i
            value = [str(_) for _ in df.iloc[i]]
            dictionary[i] = value
        print(len(dictionary))
        return dictionary

    def __repr__(self):
        return f"Size of the {self.name} file is: {len(self.import_to_df())} rows and {len(self.import_to_df().columns)} columns"
