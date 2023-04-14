from typing import List
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import Series, DataFrame
import os

from project.files.region_info import Village
from project.imports import Import, PostalCode
from project.websites.website import BaseWebsite


class WebsiteArchive(BaseWebsite):
    first_level_data = []

    def __init__(self, name, base_url, media_type, start_url, title_class, title_tag, article_class, article_tag,
                 datetime_tag, website_type):
        super().__init__(name, base_url, media_type)
        self.protocol = "https://" if base_url.__contains__("https://") else "http://"
        self.start_url = start_url
        self.title_class = title_class
        self.title_tag = title_tag
        self.article_class = article_class
        self.article_tag = article_tag
        self.datetime_tag = datetime_tag
        self.website_type = website_type

    def check_response_status(self, source: requests) -> bool:
        """
        The function returns either the url request is 200 or not
        :param source:
        :return: True / False
        """
        return source.status_code == 200

    def get_second_level_data(self, article_link):
        """
        This function follows the link to the article and returns the article text + date of publishing
        :param article_link:
        :return: List[str, str]
        """
        source = requests.get(article_link)
        is_200 = self.check_response_status(source)

        if is_200:
            article = None
            article_datetime = None

            source = requests.get(article_link)
            source_text = source.text
            soup = BeautifulSoup(source_text, 'lxml')

            text_scope = soup.find(class_=self.article_class)  # ('p', {'class': 'article-text'}) -- # ('p', class_='article-body')  //"div" or "a",
            article = " ".join(a.getText().replace('\xa0', " ").strip() for a in text_scope.findAll(self.article_tag)) # TODO attribute or function
            datetime_scope = soup.find(class_=self.datetime_tag)
            article_datetime = datetime_scope.getText().replace(" ч.", "").replace(" г.",
                                                                                   "")  # TODO transform datetime text into datetime

            return [article, article_datetime]

    def find_if_location_in_text(self, article_text: str, search_dict: dict):
        # print(search_dict)
        # location = [substring in article_text for substring in search_dict.values()]
        # location = [substring for substring in [v for v in search_dict.values()] if substring in article_text]
        location = []
        for value in search_dict.values():
            set([location.append(v) for v in value if v in article_text.upper() and v not in location])
            # if [location.append(v) for v in value if v in article_text.upper()]:
            #
            #     location.append(value)

        if location:
            return location

    def get_first_level_data(self, section) -> dict:
        """
        The function collects data for the '_data_dict' columns when the news content are related to women and violence against them
        :param section:
        :return:
        """

        for i in range(len(section)):
            element = section[i]
            title = element.find(class_=self.title_tag).text

            if any(substring in title for substring in BaseWebsite._first_level_keywords):
                link = element.a['href']
                if not link.startswith(self.base_url):
                    valid_link = self.base_url + link
                else:
                    valid_link = link

                BaseWebsite._data_dict["Title"].append(title)
                BaseWebsite._data_dict["URL"].append(valid_link)
                BaseWebsite._data_dict["Source"].append(self.name)
                BaseWebsite._data_dict["Type"].append(self.media_type)

                article_datetime_str = self.get_second_level_data(valid_link)[1]
                article_text = self.get_second_level_data(valid_link)[0]

                # search_dict = Import("Postal codes", "postal_codes_bg_2016.csv").file_to_dictionary_with_auto_index()
                # search_dict = Import("villages", "project/files/villages_list.csv").file_to_dictionary()
                search_dict = Import("cities", "project/files/cities_list.csv").file_to_dictionary()
                # search_dict = Village("villages").get_list()
                location = self.find_if_location_in_text(article_text, search_dict)
                # print(location)

                BaseWebsite._data_dict["DateTime"].append(article_datetime_str)
                BaseWebsite._data_dict["Article"].append(article_text)
                BaseWebsite._data_dict["Location"] += location
                print(BaseWebsite._data_dict)

        return BaseWebsite._data_dict

    def make_first_level_soup(self, source: requests) -> dict:
        source_text = source.text
        soup = BeautifulSoup(source_text, 'lxml')
        main_section = soup.find(class_="section-listing news-articles-inline")  # TODO make self.main_section
        section = main_section.find_all(
            class_=self.title_class)  # ('div', class_='news-article-inline')  //"div" or "a",
        initial_data = self.get_first_level_data(section)

        return initial_data

    def crawling_through_pages(self) -> dict:
        page = 1
        initial_data = None

        while True:
            print(page)
            source = requests.get(self.start_url + str(page))
            is_200 = self.check_response_status(source)

            if not is_200 or page > 1:
                break

            initial_data = self.make_first_level_soup(source)
            page += 1

        return initial_data

    def main(self):
        pass

    def __repr__(self):
        return f"""
Media name is: {self.name} >>>
Media main link is: {self.base_url} >>>
Media type is: {self.media_type} >>>
The archive page base url w/o the page number is: {self.start_url} >>>
The title class after webpage inspection is: '{self.title_class}' with tag for the title: '{self.title_tag}' >>>
with Article class: '{self.article_class}' and tag: '{self.article_tag}' >>>
With datetime tag from the articles pages: '{self.datetime_tag}'
"""


# postal_codes_2016 = Import("Postal codes", "postal_codes_bg_2016.csv")
# search_dict = postal_codes_2016.file_to_dictionary()


# print(postal_codes_2016.file_to_dictionary())
# print(postal_codes_2016.show_first_ten_rows())
# print(postal_codes_2016)
# print(postal_codes_2016.file_to_dictionary())
print(os.getcwd())

btv = WebsiteArchive("btvnovinite.bg",
                     "https://btvnovinite.bg",
                     "TV news",
                     "https://btvnovinite.bg/bulgaria/?page=",
                     "news-article-inline", "title",  # "news-article-inline"
                     "article-body", "p",
                     "date-time",
                     "WebsiteArchive")

df_btvnovinite_bg = btv.crawling_through_pages()
