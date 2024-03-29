class Player:
    UNIQUE_NAMES = []
    MIN_STAMINA = 0
    MAX_STAMINA = 100

    def __init__(self, name: str, age: int, stamina: int = 100):
        self.name = name
        self.age = age
        self.stamina = stamina
        # self.need_sustenance = self.stamina < 100

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name not valid!")
        if value in Player.UNIQUE_NAMES:
            raise Exception(f"Name {value} is already used!")
        self.__name = value
        Player.UNIQUE_NAMES.append(value)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if not Player.MIN_STAMINA <= value <= Player.MAX_STAMINA:
            raise ValueError("Stamina not valid!")
        self.__stamina = value

    @property
    def need_sustenance(self):
        return self.__stamina < 100
    #
    # @need_sustenance.setter
    # def need_sustenance(self, value):
    #     self._need_sustenance = self.__need_sustenance

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"


# maon = Player("Maon", 12, 99)
# print(maon.name)
# print(maon.age)
# print(maon.stamina)
# maon.need_sustenance = None
# print(maon.need_sustenance)
# print(maon)
