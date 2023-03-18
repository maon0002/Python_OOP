from pandas import DataFrame, Series

from news_website import NewsWebsite
from typing import List
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# pip freeze > requirements.txt
# pip install -r requirements.txt

# import postal data
postal_codes_df = pd.read_csv('imports/postal_codes_bg_2016.csv')


class WebpageArchive(NewsWebsite):
    """
        DOC...
    """

    def __init__(self, name: str, url: str, protocol: str, media_type: str, start_page_url: str,
                 title_class: str, title_tag: str,
                 article_class: str, article_tag: str,
                 datetime_class: str, datetime_tag: str, ):
        super().__init__(name, url, protocol)
        self.media_type = media_type
        self.start_page_url = start_page_url
        self.title_class = title_class
        self.title_tag = title_tag
        self.article_class = article_class
        self.article_tag = article_tag
        self.datetime_class = datetime_class
        self.datetime_tag = datetime_tag

    def check_response_status(self, source: requests) -> bool:
        return source.status_code == 200

    def make_first_level_soup(self, source: requests) -> [List[str], List[str]]:
        source_text = source.text
        soup = BeautifulSoup(source_text, 'lxml')
        section = soup.find_all(class_=self.title_class)  # ('div', class_='news-article-inline')  //"div" or "a",
        initial_data = self.get_first_level_data(section)

        return initial_data

    def get_first_level_data(self, section) -> List[List[str]]:
        title_link_pairs = []

        for i in range(len(section)):
            element = section[i]
            title = element.find(class_=self.title_tag).text
            link = element.a['href']
            # date = element.find(class_='date').text

            if not link.startswith(self.url):
                valid_link = self.url + link
            else:
                valid_link = link

            pair_to_add = [title, valid_link]
            title_link_pairs.append(pair_to_add)
            print(pair_to_add)

        return title_link_pairs

    def make_second_level_soup_time(self, column: [Series]) -> [Series]:  # `series.loc[i:j]`.
        link_list = column.to_list()
        datetimes = []
        for link in link_list:
            print(link)
            source = requests.get(link)
            source_text = source.text
            soup = BeautifulSoup(source_text, 'lxml')
            soup_scope = soup.find(self.datetime_tag, {'class': self.datetime_class})  # ('p', {'class': 'time'})
            datetimes.append(soup_scope.getText().lstrip().replace("\n", ""))

        return datetimes

    def make_second_level_soup_article(self, column: [Series]) -> [Series]:
        link_list = column.to_list()
        articles = []
        for link in link_list:
            print(link)
            source = requests.get(link)
            source_text = source.text
            soup = BeautifulSoup(source_text, 'lxml')
            soup_scope = soup.find(class_=self.article_class)  # ('p', {'class': 'article-text'})
            articles.append(soup_scope.getText().replace("\n", ""))

        return articles

    # TODO --continue from here
    def add_location(self, articles: Series, df: DataFrame):
        pass

    def filtered_titles_df(self, df) -> DataFrame:
        concat_first_lvl_keywords = "|".join(NewsWebsite.first_level_keywords)
        filtered_df = df.loc[(df['Title']).str.contains(concat_first_lvl_keywords, regex=True)]
        return filtered_df

    def create_df(self, scrapped_data: List[str]) -> DataFrame:
        init_df = pd.DataFrame(scrapped_data, columns=['Title', 'URL'])
        init_df['Source'] = self.name
        init_df['Type'] = self.media_type
        # TODO add here function call for crawling through articles
        # init_df['Article'] = ''

        data_after_filtering = self.filtered_titles_df(init_df)
        return data_after_filtering

    def crawling_through_pages(self):
        page = 1

        while True:
            print(page)
            source = requests.get(self.start_page_url + str(page))
            is_200 = self.check_response_status(source)

            if not is_200 or page > 1:
                # if not is_200:
                break

            initial_data = self.make_first_level_soup(source)

            self.first_level_data.extend(initial_data)
            page += 1

        df = self.create_df(NewsWebsite.first_level_data)

        # TODO add columns for date, location, article text
        df['Datetime'] = self.make_second_level_soup_time(df['URL'])
        df['Article'] = self.make_second_level_soup_article(df['URL'])
        # df['Location'] = self.add_location(df['Article'], df)
        # df = self.add_location(df['Article'], df)
        return df

    def get_articles(self):

        pass

    def get_links(self):
        pass

    def __repr__(self):
        return f"name is :{self.name} with url: {self.start_page_url}---------------------" \
               f"titles with links are: {NewsWebsite.first_level_data}"


news_bg = WebpageArchive("news.bg", "https://news.bg", "https://", "Web news", "https://news.bg/bulgaria?page=",
                         "topic", "title",  # "title", "a",    ## title_class: str, title_tag: str,
                         "article-text", "p",             ## article_class: str, article_tag: str,
                         "time", "p")                     ## datetime_class: str, datetime_tag: str,



btvnovinite_bg = WebpageArchive("btvnovinite.bg", "https://btvnovinite.bg", "https://", "TV news",
                                "https://btvnovinite.bg/bulgaria/?page=",
                                "news-article-inline", "title",  ## title_class: str, title_tag: str,
                                "article-body", "p",         ## article_class: str, article_tag: str,
                                "date-time",                 ## datetime_class: str, datetime_tag: str,
                                "p")  # TODO to add url prefix empty string by default in case of missing prefix links

# df_news_bg = news_bg.crawling_through_pages()
# print(df_news_bg.head(10))

df_btvnovinite_bg = btvnovinite_bg.crawling_through_pages()
print(df_btvnovinite_bg.head(10))

# Create a Pandas Excel writer using XlsxWriter as the engine.
with pd.ExcelWriter('DF_TEST.xlsx', engine='xlsxwriter') as ew:
    # df_news_bg.to_excel(r'D:\GIT_REPOS\Python_OOP\BadNews\export_dataframe.xlsx', index=False)
    df_btvnovinite_bg.to_excel(r'D:\GIT_REPOS\Python_OOP\BadNews\export_dataframe.xlsx', index=False)
