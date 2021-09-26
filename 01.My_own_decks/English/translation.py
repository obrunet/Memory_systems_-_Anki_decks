import pandas as pd
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
from random import randint
import time
import os.path


TRANSLATED_WORDS_FILENAME = "translated_words.csv"
SCRAPED_WORDS_FILENAME = "scraped_words.csv"
BASE_URL = "https://www.larousse.fr/dictionnaires/anglais-francais/"
user_agents = [
        {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"},
        {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"},
        {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"},
        {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"},
        {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"},
        {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"},
        {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"},
        {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15"},
        {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"},
        {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"},
        {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36"},
        {'User-Agent': "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36"},
        {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"},
        {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
    ]


def request_webpage(req_url):
    """Get a webpage with the requests module & return the scrape translation of a word"""
    try:
        req_response = requests.get(req_url, headers=user_agents[randint(0, len(user_agents))])
        req_response.raise_for_status()
        s = BeautifulSoup(req_response.content, 'html.parser')
        return list(set([elt.text for elt in s.find_all("a", class_="lienarticle2")]))
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err} for URL {req_url}')
        return False
    except Exception as err:
        print(f'Other error occurred: {err} for URL {req_url}')
        return False
        

def main():
    # at 1st no words translated : scrape it baby
    if not os.path.isfile(TRANSLATED_WORDS_FILENAME):
        df = pd.read_csv(SCRAPED_WORDS_FILENAME)
        for w in df['words'].values:
            time.sleep(5)
            translation = ""
            try:
                translation = request_webpage(BASE_URL + w + "/")
            except:
                pass
            if translation is not False:
                if len(translation) > 4: translation = translation[:4]
                if len(translation) > 1:
                    translation = '<b>' + translation[0] + '</b> <i>(' + ", ".join([t for t in translation[1:]]) + ')</i>'
                df.loc[df[df['words'] == w].index, "translations"] = translation
        df.to_csv(TRANSLATED_WORDS_FILENAME, index=False)
    # otherwise not all words were translated, let's grab the missing translations
    else:
        df = pd.read_csv(TRANSLATED_WORDS_FILENAME)
        for w in df[df['translations'].isnull()]['words'].values:
            time.sleep(5)
            translation = ""
            try:
                translation = request_webpage(BASE_URL + w + "/")
            except:
                pass
            if translation is not False:
                if len(translation) > 4: translation = translation[:4]
                if len(translation) > 1:
                    translation = '<b>' + translation[0] + '</b> <i>(' + ", ".join([t for t in translation[1:]]) + ')</i>'
                df.loc[df[df['words'] == w].index, "translations"] = translation
        df.to_csv(TRANSLATED_WORDS_FILENAME, index=False)        


if __name__ == "__main__":
    main()