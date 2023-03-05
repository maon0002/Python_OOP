from typing import List

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# pip freeze > requirements.txt
# pip install -r requirements.txt

# import postal data
postal_codes_df = pd.read_csv('imports/postal_codes_bg_2016.csv')


class ArchiveWebMedia:
    # first level data contains list of filtered title-url pairs
    first_level_data = []

    # define keywords for narrow search
    first_level_keywords = ['жена', 'съпруга', 'дъщеря', 'внучка', 'девойка', 'момиче', 'студентка', 'ученичка', 'баба',
                            'годеница', 'приятелка', 'гимназистка', 'майка']
    second_level_keywords = ['домашно насилие', 'убита', 'застреляна', 'намушкана', 'обезобразена', 'пребита',
                             'изнасилена',
                             'тормозена']

    def __init__(self, name: str, start_page_url: str, section: str, class_names: list, tags: list):
        self.name = name
        self.start_page_url = start_page_url
        self.section = section
        self.class_names = class_names
        self.tags = tags
        self.df = ''

    def check_response_status(self, source: requests) -> bool:
        return source.status_code == 200

    # <div class="article-text" itemprop="articleBody">

    # <p class="time" itemprop="datePublished" content="2023-03-05T10:07:50+02:00">
    #             05.03.2023 10:07:50
    #         </p>

    def make_soup(self, source: requests) -> BeautifulSoup: # article
        source_text = source.text
        soup = BeautifulSoup(source_text, 'html.parser')
        selection_class = 'article-text'
        # selection_tag = 'articleBody'
        selection_tag = ["p", "strong"]
        # soup_scope = soup.find_all({'class_': 'article-text'})  # ('a', {'class': 'title'})
        soup_scope = soup.find(class_='article-text').getText() # ('a', {'class': 'title'})
        # soup_scope = soup.find_all(class_='article-text') # ('a', {'class': 'title'})
        print(soup_scope)
        print(len(soup_scope))
        # soup_scope = soup.find_all(itemprop="articleBody")  # ('a', {'class': 'title'})

        return soup_scope

    # def make_soup(self, source: requests) -> BeautifulSoup: # article
    #     # source_text = source.text
    #     soup = BeautifulSoup(source.content)
    #
    #     soup_scope = soup.find_all(class_='article-text') # ('a', {'class': 'title'})
    #     text = soup.select('p.card-text a')
    #
    #     print(soup.prettify())
    #     print(text)
    #     # print(soup_scope)
    #     # print(len(soup_scope))
    #
    #
    #     return soup_scope

    # def make_soup(self, source: requests) -> BeautifulSoup: # time
    #     source_text = source.text
    #     soup = BeautifulSoup(source_text, 'lxml')
    #     selection_class = 'time'
    #     selection_tag = 'p'
    #     soup_scope = soup.find(selection_tag, {'class': selection_class})  # ('a', {'class': 'title'})
    #
    #     return soup_scope.string

    def get_first_level_data(self, tags: List[BeautifulSoup]) -> List[List[str]]:
        title_url_pairs = []
        title_url_pairs.extend([[tags[i].string, tags[i]['href']] for i in range(len(tags)) \
                                if tags[i]['href'].startswith(f"https://{self.name}")])
        return title_url_pairs

    def filter_first_level_data(self, data: List[List[str]]) -> List[List[str]]:
        filtered_data = []
        for pair in data:
            title = pair[0]
            for word in ArchiveWebMedia.first_level_keywords:
                if word in title:
                    filtered_data.append(pair)
                    break
        return filtered_data

    def crawling_through_pages(self):


        source = requests.get(self.start_page_url)
        is_200 = self.check_response_status(source)

        if not is_200:
            print("Page response is not OK")

        tags = self.make_soup(source)
        print(tags)

        #     initial_data = self.get_first_level_data(tags)
        #     new_data = self.filter_first_level_data(initial_data)
        #
        #     if new_data:
        #         ArchiveWebMedia.first_level_data.extend(new_data)
        #
        #
        # [print(f"{item[0]} -> {item[1]}") for item in ArchiveWebMedia.first_level_data]

    def create_df(self):
        pass

    def get_articles(self):

        pass

    def get_links(self):
        pass

    def __repr__(self):
        return self.start_page_url


news_bg = ArchiveWebMedia("news.bg", "https://news.bg/society/tencho-tenev-patnite-politsai-i-kamerite-ne-sa-dostatachno.html", "bulgaria",
                          ["topic", "topic-information"], ["a", "h2"])  # div

news_bg.crawling_through_pages()
