class NewsWebsite:
    """
    DOC...
    """
    # first level data contains list of filtered title-url pairs
    first_level_data = []

    # define keywords for narrow search
    first_level_keywords = ['жена', 'съпруга', 'дъщеря', 'внучка', 'девойка', 'момиче', 'студентка', 'ученичка', 'баба',
                            'годеница', 'приятелка', 'гимназистка', 'майка']
    second_level_keywords = ['домашно насилие', 'убита', 'застреляна', 'намушкана', 'обезобразена', 'пребита',
                             'изнасилена', 'тормозена',

                             ]

    def __init__(self, name: str, url: str, protocol: str):
        self.name = name
        self.url = url
        self.protocol = protocol
