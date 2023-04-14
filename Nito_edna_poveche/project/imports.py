import pandas as pd
import os

from project.files.region_info import Village

print(os.getcwd())


class Import:

    def __init__(self, name: str, path: str):
        self.name = name
        self.path = path

    def show_first_ten_rows(self):
        df = pd.read_csv(self.path)
        return df.head(10)

    def import_to_df(self):
        df = pd.read_csv(self.path)
        return df

    def file_to_dictionary(self):
        """
        Transform .csv file to df then to dictionary. It returns only the first two columns
        :return: dictionary with Code: Location Name
        """
        df = pd.read_csv(self.path, dtype={"CODE": "string"})
        dictionary = {}
        for i in range(len(df)):
            key = df.iloc[i][0]
            value = df.iloc[i][1]
            dictionary[key] = value
        return dictionary

    def file_to_dictionary_with_auto_index(self):
        df = self.import_to_df()
        dictionary = {}
        for i in range(len(df)):
            key = i
            value = [str(_) for _ in df.iloc[i]]
            dictionary[key] = value
        # print(len(dictionary))
        return dictionary

    def __repr__(self):
        return f"Size of the {self.name} file is: {len(self.import_to_df())} rows and {len(self.import_to_df().columns)} columns"


class PostalCode(Import):
    postal_codes = None
    # print(">>>>>>>>>>>PostalCode(Import):    postal_codes >>>>>>", postal_codes)


# postal_codes_2016 = PostalCode("Postal codes", "files/postal_codes_bg_2016.csv")
# postal_codes_2016 = Import("Postal codes", "files/postal_codes_bg_2016.csv")
# print(postal_codes_2016.file_to_dictionary())

# print(postal_codes_2016.show_first_ten_rows())
# print(postal_codes_2016)
# postal_codes_dict = postal_codes_2016.file_to_dictionary()

#
# villages = Import("list", "files/villages_list.csv")
# print(villages.file_to_dictionary())

# cities = Import("list", "files/cities_list.csv")
# print(cities.file_to_dictionary())
