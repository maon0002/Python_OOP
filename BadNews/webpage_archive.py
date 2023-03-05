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
                 title_class: str, title_tag: str, article_class: str, article_tag: str,
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

    def make_first_level_soup(self, source: requests) -> List[BeautifulSoup]:
        source_text = source.text
        soup = BeautifulSoup(source_text, 'lxml')
        soup_scope = soup.find_all(self.title_tag, {'class': self.title_class})  # ('a', {'class': 'title'})
        return soup_scope

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

    def get_first_level_data(self, tags: List[BeautifulSoup]) -> List[List[str]]:
        title_url_pairs = []
        title_url_pairs.extend([[tags[i].string, tags[i]['href']] for i in range(len(tags))
                                if tags[i]['href'].startswith(f"https://{self.name}")])

        return title_url_pairs

    #TODO --continue from here
    def add_location(self, articles: Series, df: DataFrame):
        article_list = articles.to_list()
        locations = []
        # concat_location = "|".join(postal_codes_df['location'])
        # filtered_location_series = articles.str.contains(concat_location, regex=True)


        # df.loc[df['Article'].str.upper().contains(postal_codes_df['location']), 'Location'] = postal_codes_df['location']

        locations = postal_codes_df['location']
        article_series = df['Article'].str.upper()

        test = locations.isin(article_series)

        # df = df[locations.isin(article_series), 'Location'] = postal_codes_df['location']
        if test:
            print(test.bool())


        # df.loc[~df['nickname'].str.len() < 1, 'concat_emp_company'] = df['nickname'].str[:] + "|" + df['company'].str[:]

        # for article in article_list:
        #     print(article)
        #     article = article.upper()
        #     print(article)

            # articles.append(soup_scope.getText().replace("\n", ""))
        # concat_first_lvl_keywords = "|".join(NewsWebsite.first_level_keywords)
        # filtered_df = df.loc[(df['Title']).str.contains(concat_first_lvl_keywords, regex=True)]

        return df

    def filtered_titles_df(self, df) -> DataFrame:
        concat_first_lvl_keywords = "|".join(NewsWebsite.first_level_keywords)
        filtered_df = df.loc[(df['Title']).str.contains(concat_first_lvl_keywords, regex=True)]
        return filtered_df

    def create_df(self, scrapped_data: List[str]) -> DataFrame:
        init_df = pd.DataFrame(scrapped_data, columns=['Title', 'URL'])
        init_df['Source'] = self.name
        init_df['Type'] = self.media_type

        # init_df['Article'] = ''

        data_after_filtering = self.filtered_titles_df(init_df)
        return data_after_filtering

    def crawling_through_pages(self):
        page = 1

        while True:
            print(page)
            source = requests.get(self.start_page_url + str(page))
            is_200 = self.check_response_status(source)

            if not is_200 or page > 5:
                # if not is_200:
                break

            tags = self.make_first_level_soup(source)
            initial_data = self.get_first_level_data(tags)

            NewsWebsite.first_level_data.extend(initial_data)
            page += 1

        df = self.create_df(NewsWebsite.first_level_data)

        # TODO add columns for date, location, article text
        df['Datetime'] = self.make_second_level_soup_time(df['URL'])
        df['Article'] = self.make_second_level_soup_article(df['URL'])
        df['Location'] = self.add_location(df['Article'], df)
        # df = self.add_location(df['Article'], df)
        return df

    def get_articles(self):

        pass

    def get_links(self):
        pass

    def __repr__(self):
        pass


news_bg = WebpageArchive("news.bg", "https://news.bg", "https://", "web news", "https://news.bg/bulgaria?page=",
                         "title", "a",
                         "article-text", "p",
                         "time", "p")

# <div class="article-text" itemprop="articleBody">

# <p class="time" itemprop="datePublished" content="2023-03-05T10:07:50+02:00">
#             05.03.2023 10:07:50
#         </p>

df_news_bg = news_bg.crawling_through_pages()
print(df_news_bg.head(10))

# Create a Pandas Excel writer using XlsxWriter as the engine.
with pd.ExcelWriter('DF_TEST.xlsx', engine='xlsxwriter') as ew:
    df_news_bg.to_excel(r'D:\GIT_REPOS\News-website-scraping\export_dataframe.xlsx', index=False)
