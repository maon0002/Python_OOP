from typing import List

from band import Band
from band_members.musician import Musician
from band_members.drummer import Drummer
from band_members.singer import Singer
from band_members.guitarist import Guitarist
from concert import Concert


class ConcertTrackerApp:
    # VALID_MUSICIAN_TYPES = [m.__name__ for m in Musician.__subclasses__()]
    VALID_MUSICIAN_TYPES = ['Singer', 'Drummer', 'Guitarist']
    ALL_MUSICIANS_NAMES = []
    ALL_BANDS_NAMES = []

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in ConcertTrackerApp.VALID_MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")
        if name in self.ALL_MUSICIANS_NAMES:
            raise Exception(f"{name} is already a musician!")
        class_sel = next(filter(lambda m_class: m_class.__name__ == musician_type, Musician.__subclasses__()))
        musician = class_sel(name, age)
        self.musicians.append(musician)
        self.ALL_MUSICIANS_NAMES.append(name)
        return f"{musician.name} is now a {class_sel.__name__}."

    def create_band(self, name: str):
        if name in self.ALL_BANDS_NAMES:
            raise Exception(f"{name} band is already created!")
        band = Band(name)
        self.bands.append(band)
        self.ALL_BANDS_NAMES.append(name)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            if concert.place == place:
                raise Exception(f"{place} is already registered for {concert.genre} concert!")

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        if musician_name not in [m.name for m in self.musicians]:
            raise Exception(f"{musician_name} isn't a musician!")

        if band_name not in [b.name for b in self.bands]:
            raise Exception(f"{band_name} isn't a band!")

        band = [b for b in self.bands if b.name == band_name][0]
        musician = [m for m in self.musicians if m.name == musician_name][0]
        band.members.append(musician)

        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        if band_name not in [b.name for b in self.bands]:
            raise Exception(f"{band_name} isn't a band!")

        band = [b for b in self.bands if b.name == band_name][0]
        if musician_name not in [m.name for m in band.members]:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        musician = [m for m in self.musicians if m.name == musician_name][0]
        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = [b for b in self.bands if b.name == band_name][0]
        concert = [c for c in self.concerts if c.place == concert_place][0]
        unique_musician_types_in_band = set(band_member.__class__.__name__ for band_member in band.members)  # pos issue

        if len(unique_musician_types_in_band) != len(ConcertTrackerApp.VALID_MUSICIAN_TYPES):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if concert.genre == 'Rock':
            for musician in band.members:
                if musician.__class__.__name__ == "Drummer":
                    if "play the drums with drumsticks" not in musician.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if musician.__class__.__name__ == "Singer":
                    if "sing high pitch notes" not in musician.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if musician.__class__.__name__ == "Guitarist":
                    if "play rock" not in musician.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

        if concert.genre == 'Metal':
            for musician in band.members:
                if musician.__class__.__name__ == "Drummer":
                    if "play the drums with drumsticks" not in musician.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if musician.__class__.__name__ == "Singer":
                    if "sing low pitch notes" not in musician.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if musician.__class__.__name__ == "Guitarist":
                    if "play metal" not in musician.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

        if concert.genre == 'Jazz':
            for musician in band.members:
                if musician.__class__.__name__ == "Drummer":
                    if "play the drums with drum brushes" not in musician.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if musician.__class__.__name__ == "Singer":
                    if "sing low pitch notes" not in musician.skills or "sing high pitch notes" not in musician.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if musician.__class__.__name__ == "Guitarist":
                    if "play jazz" not in musician.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses

        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."
