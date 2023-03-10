from typing import List


class User:

    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books: List[str] = []

    def info(self) -> str:
        info_list = sorted(self.books)
        return f"{', '.join(info_list)}"

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"

# user = User(12, 'Peter')
# print(user.info)
