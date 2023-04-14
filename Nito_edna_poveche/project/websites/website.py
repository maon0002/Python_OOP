from abc import ABC, abstractmethod

import requests


class BaseWebsite(ABC):
    _first_level_keywords = ['жена', 'съпруга', 'дъщеря', 'внучка', 'девойка', 'момиче', 'студентка', 'ученичка', 'баба',
                            'годеница', 'приятелка', 'гимназистка', 'майка']
    _second_level_keywords = ['домашно насилие', 'убита', 'застреляна', 'намушкана', 'обезобразена', 'пребита',
                             'изнасилена', 'тормозена']

    _data_dict = {
            "Title": [],
            "URL": [],
            "Source": [],
            "Type": [],
            "DateTime": [],
            "Article": [],
            "Location": [],
        }

    def __init__(self, name, base_url, media_type):
        self.name = name
        self.base_url = base_url
        self.media_type = media_type

    @abstractmethod
    def check_response_status(self, source: requests) -> bool:
        ...












# btvnovinite_bg = WebpageArchive("btvnovinite.bg", "https://btvnovinite.bg", "https://", "TV news",
#                                 "https://btvnovinite.bg/bulgaria/?page=",
#                                 "news-article-inline", "title",  ## title_class: str, title_tag: str,
#                                 "article-body", "p",         ## article_class: str, article_tag: str,
#                                 "date-time",                 ## datetime_class: str, datetime_tag: str,
#                                 "p")

#   name : >>>  "btvnovinite.bg",
#   base_url : >>>  "https://btvnovinite.bg",
#   protocol : >>>  "https://",
#   media_type : >>>  "TV news",
#   start_url : >>>  "https://btvnovinite.bg/bulgaria/?page=",
#   title_class : >>> "news-article-inline"
#   title_tag : >>> "title"
#   article_class : >>> "article-body"
#   article_tag : >>> "p"
#   datetime_tag : >>> "date-time"