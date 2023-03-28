from project.band import Band
from project.band_members.musician import Musician
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer
    }

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in ConcertTrackerApp.VALID_MUSICIAN_TYPES.keys():
            raise ValueError("Invalid musician type!")
        if name in [m.name for m in self.musicians]:
            raise Exception(f"{name} is already a musician!")
        self.musicians.append(ConcertTrackerApp.VALID_MUSICIAN_TYPES[musician_type](name, age))
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if name in [b.name for b in self.bands]:
            raise Exception(f"{name} band is already created!")
        self.bands.append(Band(name))
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        if place in [c.place for c in self.concerts]:
            concert_genre = [c.genre for c in self.concerts if c.place == place][0]
            raise Exception(f"{place} is already registered for {concert_genre} concert!")
        self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        try:
            musician = next(filter(lambda m: m.name == musician_name, self.musicians))
        except StopIteration:
            raise Exception(f"{musician_name} isn't a musician!")

        try:
            band = next(filter(lambda b: b.name == band_name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        try:
            band = next(filter(lambda b: b.name == band_name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        try:
            musician = next(filter(lambda m: m.name == musician_name, band.members))
        except StopIteration:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = next(filter(lambda b: b.name == band_name, self.bands))
        unique_musician_types = set(b.__class__.__name__ for b in band.members)
        if len(unique_musician_types) != len(ConcertTrackerApp.VALID_MUSICIAN_TYPES):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        concert = next(filter(lambda c: c.place == concert_place, self.concerts))

        if concert.genre == "Rock":
            for musician in band.members:
                if musician.__class__.__name__ == "Drummer" and "play the drums with drumsticks" not in musician.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if musician.__class__.__name__ == "Singer" and "sing high pitch notes" not in musician.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if musician.__class__.__name__ == "Guitarist" and "play rock" not in musician.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == "Metal":
            for musician in band.members:
                if musician.__class__.__name__ == "Drummer" and "play the drums with drumsticks" not in musician.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if musician.__class__.__name__ == "Singer" and "sing low pitch notes" not in musician.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if musician.__class__.__name__ == "Guitarist" and "play metal" not in musician.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == "Jazz":
            for musician in band.members:
                if musician.__class__.__name__ == "Drummer" and "play the drums with drum brushes" not in musician.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if musician.__class__.__name__ == "Singer" and (
                        "sing high pitch notes" not in musician.skills or "sing low pitch notes" not in musician.skills):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if musician.__class__.__name__ == "Guitarist" and "play jazz" not in musician.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."


musician_types = ["Singer", "Drummer", "Guitarist"]
names = ["George", "Alex", "Lilly"]

app = ConcertTrackerApp()

for i in range(3):
    print(app.create_musician(musician_types[i], names[i], 20))

print(app.musicians[0].learn_new_skill("sing high pitch notes"))
print(app.musicians[1].learn_new_skill("play the drums with drumsticks"))
print(app.musicians[2].learn_new_skill("play rock"))

print(app.create_band("RockName"))
for i in range(3):
    print(app.add_musician_to_band(names[i], "RockName"))

print(app.create_concert("Rock", 20, 5.20, 56.7, "Sofia"))

print(list(map(lambda a: a.__class__.__name__, app.bands[0].members)))
print(app.start_concert("Sofia", "RockName"))
