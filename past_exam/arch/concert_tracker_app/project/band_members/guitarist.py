from band_members.musician import Musician


class Guitarist(Musician):
    SKILLS_THAT_CAN_LEARN = ["play metal", "play rock", "play jazz"]

    def learn_new_skill(self, new_skill: str):
        if new_skill not in Guitarist.SKILLS_THAT_CAN_LEARN:
            raise ValueError(f"{new_skill} is not a needed skill!")
        if new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")
        self.skills.append(new_skill)
        return f"{self.name} learned to {new_skill}."


# adamG = Guitarist("AdamG", 18)
# print(adamG.name)
# print(adamG.age)
# print(adamG.skills)
# print(adamG.learn_new_skill("play jazz"))
# print(adamG.skills)
