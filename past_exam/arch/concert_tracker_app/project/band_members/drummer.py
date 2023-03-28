from band_members.musician import Musician


class Drummer(Musician):
    SKILLS_THAT_CAN_LEARN = ["play the drums with drumsticks", "play the drums with drum brushes", "read sheet music"]

    def learn_new_skill(self, new_skill: str):
        if new_skill not in Drummer.SKILLS_THAT_CAN_LEARN:
            raise ValueError(f"{new_skill} is not a needed skill!")
        if new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")
        self.skills.append(new_skill)
        return f"{self.name} learned to {new_skill}."

# adamD = Drummer("AdamD", 17)
# print(adamD.name)
# print(adamD.age)
# print(adamD.skills)
# print(adamD.learn_new_skill("read sheet music"))
# print(adamD.skills)

# print([m.__name__ for m in Musician.__subclasses__()])
