from typing import List

from band_members.musician import Musician


class Band:
    def __init__(self, name: str):
        self.name = name
        self.members: List[Musician] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Band name should contain at least one character!")
        self.__name = value
    #
    # def add_member(self, musician):
    #     self.members.append(musician)
    #
    # def remove_member(self, musician):
    #     self.members.remove(musician)

    def __str__(self):
        return f"{self.name} with {len(self.members)} members."




#
# coldplay = Band("Coldplay")
# print(coldplay.name)
# print(coldplay.members)