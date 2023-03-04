import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# pip freeze > requirements.txt
# pip install -r requirements.txt

# define keywords for narrow search
first_level_keywords = ['жена', 'съпруга', 'дъщеря', 'внучка', 'девойка', 'момиче', 'студентка', 'ученичка', 'баба',
                        'годеница', 'приятелка', 'гимназистка']
second_level_keywords = ['домашно насилие', 'убита', 'застреляна', 'намушкана', 'обезобразена', 'пребита', 'изнасилена',
                         'тормозена']

# import postal data
postal_codes_df = pd.read_csv('imports/postal_codes_bg_2016.csv')


class ArchiveWebMedia:

    def __init__(self, name: str, start_page_url: str, section: str, class_names: list, tags: list):
        self.name = name
        self.start_page_url = start_page_url
        self.section = section
        self.class_names = class_names
        self.tags = tags
        self.df = ''

    def preparation(self):
        source = requests.get(news_bg.start_page_url).text

        soup = BeautifulSoup(source, 'lxml')
        # print(soup.prettify())

        # box = soup.find_all('div', class_='topic-information')
        # needed_section = soup.find("secondary-articles")
        needed_section = soup.find("main-news")
        print(needed_section.prettify())

        # # headline_match = needed_section.find_all('div', class_='topic-information').p.text
        # headline_match = needed_section.find('div', class_='title').text
        # # headline_match = needed_section.find('topic-information')
        # headline = headline_match.h2.a.text
        # print(headline)

        # for piece in box:
        #     headline = piece.h2.a.text
        #     print(headline)
        #     link = piece.h2.a.href
        #     print(link)

    def create_df(self):
        pass

    def get_articles(self):
        # for
        pass

    def get_links(self):
        pass


news_bg = ArchiveWebMedia("news.bg", "https://news.bg/bulgaria?page=1", "bulgaria",
                          ["topic", "topic-information"], ["a", "h2"])  # div

news_bg.preparation()
