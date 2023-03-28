from band_members.musician import Musician


class Singer(Musician):
    SKILLS_THAT_CAN_LEARN = ["sing high pitch notes", "sing low pitch notes"]

    def learn_new_skill(self, new_skill: str):
        if new_skill not in Singer.SKILLS_THAT_CAN_LEARN:
            raise ValueError(f"{new_skill} is not a needed skill!")
        if new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")
        self.skills.append(new_skill)
        return f"{self.name} learned to {new_skill}."

#
# adam = Singer("Adam", 16)
# print(adam.name)
# print(adam.age)
# print(adam.skills)
# print(adam.learn_new_skill("sing high pitch notes"))
# print(adam.skills)
