class Profile:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) not in range(5, 15):
            raise ValueError("The username must be between 5 and 15 characters.")

        self.__username = value

    @property
    def password(self):
        return self.__password


    @password.setter
    def password(self, value):
        error_message = "The password must be 8 or more characters with at least 1 digit and 1 uppercase letter."

        if len(value) < 8:
            raise ValueError(error_message)
        elif value.lower() == value:
            raise ValueError(error_message)
        elif not [l for l in value if l.isdigit()]:
            raise ValueError(error_message)

        self.__password = value

    # @password.setter
    # def password(self, value):
    #     three_are_valid = all([
    #         len(value) > 7,
    #         value != value.lower(),
    #         [x for x in value if x.isdigit()]
    #     ])
    #
    #     if not three_are_valid:
    #         raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
    #
    #     self.__password = value

    def __str__(self):
        return f"You have a profile with username: '{self.username}' and password: {'*' * len(self.password)}"


# profile_with_invalid_password = Profile('My_username', 'My-password')
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)

a = 16
print(a in range(5, 16))