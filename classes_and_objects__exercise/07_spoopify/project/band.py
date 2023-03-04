from typing import List

from project.album import Album
from project.song import Song


class Band:

    def __init__(self, name: str):
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, album: Album) -> str:
        try:
            current_album = next(filter(lambda a: a == album, self.albums))
            return f"Band {self.name} already has {album.name} in their library."
        except StopIteration:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str) -> str:
        try:
            current_album = next(filter(lambda a: a == album_name, self.albums))
            if not current_album.published:
                self.albums.remove(current_album)
                return f"Album {current_album.name} has been removed."
            else:
                return "Album has been published. It cannot be removed."
        except StopIteration:
            return f"Album {album_name} is not found."

    def details(self) -> str:
        band_details_list = [
            f"Band {self.name}"
        ]
        band_details_list.extend([a.details() for a in self.albums])

        return "\n".join(band_details_list)


