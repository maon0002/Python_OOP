from typing import List

from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food
from project.supply.supply import Supply


class Controller:
    VALID_SUPPLY_TYPES = ["Food", "Drink"]

    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *player):
        added_players = []

        for p in player:
            if p.name in [p.name for p in self.players]:
                continue
            else:
                self.players.append(p)
                added_players.append(p)
        return f'Successfully added: {", ".join([p.name for p in added_players])}'

    def add_supply(self, *supply):
        for s in supply:
            self.supplies.append(s)

    def sustain(self, player_name: str, sustenance_type: str):
        if player_name not in [p.name for p in self.players] or sustenance_type not in Controller.VALID_SUPPLY_TYPES:
            pass
        else:
            player = next(filter(lambda p: p.name == player_name, self.players))
            if not player.need_sustenance:
                return f"{player_name} have enough stamina."
            if sustenance_type not in [s.__class__.__name__ for s in self.supplies]:
                raise Exception(f"There are no {sustenance_type.lower()} supplies left!")
            last_supply = [s for s in self.supplies if s.__class__.__name__ == sustenance_type][-1]
            last_supply_energy = last_supply.energy
            last_supply_name = last_supply.name
            player.stamina = min(player.stamina + last_supply_energy, Player.MAX_STAMINA)
            self.supplies.remove(last_supply)
            return f"{player_name} sustained successfully with {last_supply_name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player_one = next(filter(lambda p: p.name == first_player_name, self.players))
        player_two = next(filter(lambda p: p.name == second_player_name, self.players))
        player_one_stamina = player_one.stamina
        player_two_stamina = player_two.stamina

        if player_one_stamina == 0 and player_two_stamina == 0:
            return f"Player {first_player_name} does not have enough stamina.\nPlayer {second_player_name} does not have enough stamina."

        elif player_one_stamina == 0 or player_two_stamina == 0:
            return f"Player {[p.name for p in [player_one, player_two] if p.stamina == 0][0]} does not have enough stamina."

        else:
            winner = None
            loser = None
            first_attacks = None
            second_attacks = None
            if player_one_stamina < player_two_stamina:
                first_attacks = player_one
                second_attacks = player_two
            else:
                first_attacks = player_two
                second_attacks = player_one

            second_attacks.stamina -= first_attacks.stamina / 2
            if second_attacks.stamina <= 0:
                second_attacks.stamina = 0
                winner = first_attacks
                return f"Winner: {winner.name}"
            first_attacks, second_attacks = second_attacks, first_attacks
            second_attacks.stamina -= first_attacks.stamina / 2
            if second_attacks.stamina <= 0:
                second_attacks.stamina = 0
                winner = first_attacks
                return f"Winner: {winner.name}"

            return f"Winner: {first_attacks.name if first_attacks.stamina > second_attacks.stamina else second_attacks.name}"

    def next_day(self):
        for p in self.players:
            p.stamina = max(p.stamina - (p.age * 2), 0)

        for p in self.players:
            self.sustain(p.name, "Food")
            self.sustain(p.name, "Drink")

    def __str__(self):
        result = []
        for p in self.players:
            # if p not in result:
            result.append(p)
        for s in self.supplies:
            # if s.details() not in result:
            result.append(s.details())

        return "\n".join([str(line) for line in result])


controller = Controller()
apple = Food("apple", 22)
cheese = Food("cheese")
juice = Drink("orange juice")
water = Drink("water")
first_player = Player('Peter', 15)
second_player = Player('Lilly', 12, 94)
print(controller.add_supply(cheese, apple, cheese, apple, juice, water, water))
print(controller.add_player(first_player, second_player))
print(controller.duel("Peter", "Lilly"))
print(controller.add_player(first_player))
print(controller.sustain("Lilly", "Drink"))
first_player.stamina = 0
print(controller.duel("Peter", "Lilly"))
print(first_player)
print(second_player)
controller.next_day()
print(controller)

# controller = Controller()
# apple = Food("apple", 22)
# cheese = Food("cheese")
# juice = Drink("orange juice")
# water = Drink("water")
# first_player = Player('Peter', 15)
# second_player = Player('Lilly', 12, 94)
# # third_player = Player('Lilly', 12, 94)
# # fourth_player = Player('Maon', 13, 95)
# # print(controller.add_supply(cheese, apple, cheese, apple, juice, water, water))
# print(controller.add_player(first_player, second_player))
# print(controller.add_player(second_player, fourth_player))
# print(controller.duel("Peter", "Lilly"))
# print(controller.add_player(first_player))
# print(controller.sustain("Lilly", "Drink"))
# print(controller.sustain("Lilly", "Drink"))
#
# print(controller.sustain("Lilly", "Food"))
# print(controller.sustain("Lilly", "Food"))
# print(controller.sustain("Lilly", "Food"))
#
# first_player.stamina = 0
# print(controller.duel("Peter", "Lilly"))
# print(first_player)
# print(second_player)
# controller.next_day()
# print(controller)
