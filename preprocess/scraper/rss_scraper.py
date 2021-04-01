import os, json, requests
import pandas as pd
from bs4 import BeautifulSoup
from urls import url_links

'''
1. define scraper function to access RSS feed list
2. scrape the following for each article - link, desc, content
3. create df to insert into columns
'''

def article_content(urls):
    try:
        for url in urls:

            # Get page content
            article = requests.get(url)

            # 1. 
            soup = BeautifulSoup(article.content, features='xml')

            print(url)
            print('Scraping job success: ', article.status_code)
        return

    except Exception as e:
        print("Scraping job failed! Check exception: ")
        print(e)


if __name__ == '__main__':
    print('Started Scrape')
    article_content(url_links)
    print('Finished Scrape')