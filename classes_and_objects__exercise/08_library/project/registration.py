from project.library import Library
from project.user import User


class Registration:

    def add_user(self, user: User, library: Library) -> [None, str]:
        if user not in library.user_records:
            library.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User, library: Library) -> [None, str]:
        if user in library.user_records:
            library.user_records.remove(user)
        else:
            return f"We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library) -> str:
        try:
            current_user_id = next(filter(lambda u: u.user_id == user_id, library.user_records))
            old_username = current_user_id.username
            if current_user_id.username != new_username:
                current_user_id.username = new_username
                old_record = library.rented_books[current_user_id.username]
                del library.rented_books[current_user_id.username]
                library.rented_books[new_username] = old_record
                return f"Username successfully changed to: {new_username} for user id: {user_id}"
            else:
                return "Please check again the provided username - it should be different than the username used so far!"
        except StopIteration:
            return f"There is no user with id = {user_id}!"


