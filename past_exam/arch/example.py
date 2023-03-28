from abc import ABC


class Musician(ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"class name is: {self.__class__.__name__}\n with name: {self.name}\nand age: {self.age}"


class Drummer(Musician):
    SKILLS_THAT_CAN_LEARN = ["play the drums with drumsticks", "play the drums with drum brushes", "read sheet music"]
    skills = []

    def __init__(self, name: str, age: int):
        super().__init__(name, age)


class Guitarist(Musician):
    SKILLS_THAT_CAN_LEARN = ["play metal", "play rock", "play jazz"]
    skills = []

    def __init__(self, name: str, age: int):
        super().__init__(name, age)


class Singer(Musician):
    SKILLS_THAT_CAN_LEARN = ["sing high pitch notes", "sing low pitch notes"]
    skills = []

    def __init__(self, name: str, age: int):
        super().__init__(name, age)


print([m.__name__ for m in Musician.__subclasses__()])

adamD = Drummer("AdamD", 17)
adamG = Guitarist("AdamG", 17)

musician_name = "AdamD"

# [print(n) for n in [Guitarist, Singer, Drummer]]

# print([str(m) for m in [Guitarist.__dict__, Singer.__dict__, Drummer.__dict__]])
print([m.__str__() for m in [Guitarist.__dict__.values(), Singer.__dict__.values(), Drummer.__dict__.values()]])
