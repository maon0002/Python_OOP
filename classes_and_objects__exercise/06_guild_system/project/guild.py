from typing import List
from project.player import Player


class Guild:

    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player) -> str:
        if player.guild == "Unaffiliated":
            player.guild = self.name
            self.players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"
        elif player in self.players:
            return f"Player {player.name} is already in the guild."
        else:
            return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str) -> str:
        try:
            current_player = next(filter(lambda p: p.name == player_name, self.players))
            player.guild = "Unaffiliated"
            self.players.remove(current_player)
            return f"Player {player_name} has been removed from the guild."
        except StopIteration:
            return f"Player {player_name} is not in the guild."

    def guild_info(self) -> str:
        info_list = [
            f"Guild: {self.name}",
        ]
        info_list.extend([p.player_info() for p in self.players])

        return "\n".join(info_list)


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())

# print(guild.kick_player("George"))
# print(guild.guild_info())
# print(guild.assign_player(player))
# print(guild.guild_info())
# print(player.add_skill("Shield Break", 20))