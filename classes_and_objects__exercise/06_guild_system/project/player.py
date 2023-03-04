from typing import Dict


class Player:

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: Dict[str: int] = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int) -> str:
        try:
            skill = next(filter(lambda x: x == skill_name, self.skills.keys()))
            return "Skill already added"
        except StopIteration:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self) -> str:
        info_list = [f"Name: {self.name}",
                     f"Guild: {self.guild}",
                     f"HP: {self.hp}",
                     f"MP: {self.mp}"]
        info_list.extend([f"==={n} - {m}" for n, m in self.skills.items()])
        return '\n'.join(info_list)

