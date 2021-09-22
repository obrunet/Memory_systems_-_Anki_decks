import pandas as pd
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
from random import randint
import time
import os.path


WORD_LIST_URL = "https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000"
WORD_LIST_FILENAME = "./word_list.csv"
SCRAPED_WORDS_FILENAME = "./scraped_words.csv"
BASE_URL = "https://www.oxfordlearnersdictionaries.com"


def retrieve_webpage(req_url):
    """Get a webpage with the requests module & return the response"""
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
    try:
        req_response = requests.get(req_url, headers=user_agents[randint(0, len(user_agents))])
        req_response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err} for URL {req_url}')
        return None
    except Exception as err:
        print(f'Other error occurred: {err} for URL {req_url}')
        return None
    else: # Request success
        return req_response


def retrieve_wordlist():
    """Retrieves the list of the 5000 words, scrape all the needed infos and returns a dataframe"""
    req_response = retrieve_webpage(WORD_LIST_URL)
    if not req_response:
        print("Fail to get the 1st page")
        return None
    elif str(req_response) == '<Response [200]>':
        print("Succeed to get the 1st page")
        s = BeautifulSoup(req_response.content, 'html.parser')
        all_elts = s.find_all("li")[34:-44]
        words, levels, def_urls, types, sound_urls = [], [], [], [], []
        for i in all_elts:
            i = str(i)
            if "data-hw" in i:
                words.append(i.split('data-hw="')[1].split('"')[0])
            else:
                words.append("No word")
            if "data-ox5000" in i:
                levels.append(i.split('data-ox5000="')[1].split('"')[0])
            else:
                levels.append("No level")
            if "href" in i:
                def_urls.append(i.split('href="')[1].split('"')[0])
            else:
                def_urls.append("No def_url")
            if 'class="pos' in i:
                types.append(i.split('class="pos">')[1].split('<')[0])
            else:
                types.append("No types")
            if "data-src-mp3" in i:
                sound_urls.append(i.split('pron-us" data-src-mp3="')[1].split('"')[0])
            else:
                sound_urls.append("No sound url")
        df = pd.DataFrame(list(zip(words, levels, def_urls, types, sound_urls)), columns=['words', 'levels', 'def_urls', 'types', 'sound_urls'])
        df.loc[df[df['levels'] == 'No level'].index, 'levels'] = 'a1'
        df['def_urls'] = df['def_urls'].apply(lambda x: BASE_URL + x)
        df['levels'] = df['levels'].apply(lambda x: x.upper())
        df['types'] = df['types'].apply(lambda x: "(" + x + ")")
        df['sound_urls'] = df['sound_urls'].apply(lambda x: BASE_URL + x)
        df['sound_files'] = df['sound_urls'].apply(lambda x: x.split("/")[-1])
        return df
    else:
        print("Something went wrong...")
        return None


def scrape_word_data(resp):
    """Parse HTTP response of a single webpage with BS4 and return relevant data"""
    soup = BeautifulSoup(resp.content, 'html.parser')
    try:
        phonetic = soup.find_all("div", class_="phons_n_am")[0].find_all("span", class_="phon")[0].contents[0]
    except (Exception,):
        phonetic = ""
    try:
        senses = soup.find_all("li", class_="sense")
    except (Exception,):
        senses = []
    try:
        definitions = [se.find_all(class_="def")[0].contents[0] for se in senses]
        definitions = [f"{i + 1}. {def_.replace(';', ',')}" for i, def_ in enumerate(definitions)]
    except (Exception,):
        definitions = []
    try:
        examples = []  # a list of (list of examples for one definition)
        for se in senses:
            all_examples = se.find_all("ul", class_="examples")[0].find_all(htag="li")
            try:
                all_examples = [e.contents[0].text for e in all_examples]
            except (Exception,):
                try:
                    all_examples = [ex.find_all(class_="x")[0].text for ex in all_examples]
                except (Exception,):
                    all_examples = []
            examples.append("".join(["<dd>- " + e.replace(';', ',') + "<br>" for e in all_examples]))
    except (Exception,):
        examples = []
    return phonetic, definitions, examples


def ingest_infos_into_df(urls_list, df):
    """Receive a list of urls (for next words to be scraped) & return a df with formatted infos"""
    for url in urls_list:
        time.sleep(4)
        req_response = retrieve_webpage(url.strip())
        if not req_response:
            continue
        elif str(req_response) == '<Response [200]>':
            phonetic, definitions, examples = scrape_word_data(req_response)
            df.loc[df[df['def_urls'] == url].index, 'phonetic'] = phonetic
            for i, def_ in enumerate(definitions):
                df.loc[df[df['def_urls'] == url].index, f'definition_{i + 1}'] = def_
            for i, ex in enumerate(examples):
                df.loc[df[df['def_urls'] == url].index, f'examples_{i + 1}'] = ex
        else:
            print("Something went wrong for URL {url} !")
    return df


def main():

    # at 1st no list of words exists : scrape it baby
    if not os.path.isfile(WORD_LIST_FILENAME) and not os.path.isfile(SCRAPED_WORDS_FILENAME):
        df = retrieve_wordlist()
        if df is None:
            print("Fail to get the 1st page")
            return None
        df.to_csv(WORD_LIST_FILENAME, index=False)

    # otherwise if the wordlist is present but no specific data scraped : read the list of word already retrieved
    elif os.path.isfile(WORD_LIST_FILENAME) and not os.path.isfile(SCRAPED_WORDS_FILENAME):
        df = pd.read_csv(WORD_LIST_FILENAME)
        df = ingest_infos_into_df(df.iloc[:20]["def_urls"].values, df)  # df.iloc[:20] //::::::::/// change here
        df.to_csv(SCRAPED_WORDS_FILENAME, index=False)

    # finally, in the case some words def & examples have already been scraped but are incomplete (Nans)
    else:
        df = pd.read_csv(SCRAPED_WORDS_FILENAME)
        df = ingest_infos_into_df(df[df["definition_1"].isnull()].iloc[:20]["def_urls"].values, df)  # df.iloc[:20//::::::::::/ change here
        df.to_csv(SCRAPED_WORDS_FILENAME, index=False)


if __name__ == "__main__":
    main()