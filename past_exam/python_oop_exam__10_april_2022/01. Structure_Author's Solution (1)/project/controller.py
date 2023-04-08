class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        successfully_added = []
        for p in players:
            if p not in self.players:
                self.players.append(p)
                successfully_added.append(p.name)
        return f"Successfully added: {', '.join(successfully_added)}"

    def add_supply(self, *supplies):
        self.supplies.extend(supplies)

    def __take_last_supply(self, supply_type: str):
        for i in range(len(self.supplies) - 1, 0, -1):
            if type(self.supplies[i]).__name__ == supply_type:
                return self.supplies.pop(i)
        if supply_type == "Food":
            raise Exception("There are no food supplies left!")
        if supply_type == "Drink":
            raise Exception("There are no drink supplies left!")

    def __find_player_by_name(self, name: str):
        for p in self.players:
            if p.name == name:
                return p

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__find_player_by_name(player_name)
        if player.stamina == 100:
            return f"{player.name} have enough stamina."
        supply = self.__take_last_supply(sustenance_type)
        if supply:
            player._sustain_player(supply)
            return f"{player_name} sustained successfully with {supply.name}."

    @staticmethod
    def __attack(p1, p2):
        p2.stamina -= (p1.stamina / 2)
        if p1.stamina - (p2.stamina / 2) < 0:
            p1.stamina = 0
        else:
            p1.stamina -= (p2.stamina / 2)
        if p1 < p2:
            return f"Winner: {p2.name}"
        else:
            return f"Winner: {p1.name}"

    @staticmethod
    def __check_if_the_players_cannot_duel(*players):
        result = []
        for player in players:
            if player.stamina == 0:
                result.append(f"Player {player.name} does not have enough stamina.")
        if result:
            return '\n'.join(result)

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.__find_player_by_name(first_player_name)
        second_player = self.__find_player_by_name(second_player_name)

        result = self.__check_if_the_players_cannot_duel(first_player, second_player)
        if result:
            return result

        if first_player < second_player:
            return self.__attack(first_player, second_player)
        else:
            return self.__attack(second_player, first_player)

    def next_day(self):
        for p in self.players:
            if p.stamina - (p.age * 2) < 0:
                p.stamina = 0
            else:
                p.stamina -= (p.age * 2)
        for p in self.players:
            self.sustain(p.name, "Food")
            self.sustain(p.name, "Drink")

    def __str__(self):
        info = []
        for p in self.players:
            info.append(p.__str__())
        for s in self.supplies:
            info.append(s.details())
        result = "\n".join(info)
        return result
