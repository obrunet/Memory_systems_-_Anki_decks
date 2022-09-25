""""
Scrape all the tips posted as images on the blog https://mathdatasimplified.com/
in order to create an anki deck
All the credits go to Khuyen Tran https://github.com/khuyentran1401
coded by O.Brunet on September 2022
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv
import random
import time
import string
from datetime import datetime
import shutil
import os


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


def retrieve_webpage(req_url):
    """Retrieve a webpage with the help of the request module and check the status code
    it tries 5 times, with a wait between 2 & 4 seconds between each attempts
    Args:
        - req_url: the url requested
    Return:
        - the response including its content
        - False if something went wrong
    """
    req_response, nb_tries = False, 5
    while nb_tries:
        time.sleep(random.randint(2, 5))
        req_response = requests.get(req_url, headers=random.choice(user_agents))
        if req_response.status_code == 200:
            break
        else:
            nb_tries -= 1
    return req_response
    

def get_soup_from_req(req_response):
    """Make a (beautiful) soup from a web page
    Args:
        - req_response: the response of the requests module for a specific url
    Returns:
        - a soup or False if something went wrong
    """
    try:
        soup = BeautifulSoup(req_response.content, 'html.parser')
    except:
        soup = False
    finally:
        return soup

        
def extract_blog_entry_content(soup):
    """Retrieve all the needed infos from a blog entry
    Args:
        - soup: a (beautifull) soup
    Return:
        - a tuple: date, front (title), back_img_path, back_text, img_url
    """
    
    back_text = soup.find_all("div", {"class": "entry-content"})[0].text.split('\n\n')[0].replace('\n', ' ')
    
    title_with_punctuation = soup.select('h1.entry-title')[0].text.strip()
    title_without_punctuation =  title_with_punctuation.translate(str.maketrans('', '', string.punctuation))

    date_time_str = soup.find_all("time", {"class": "entry-date published"})[0]['datetime']
    date_time = datetime.fromisoformat(date_time_str)

    image_url = soup.find_all("img")[0]['data-src']

    image_file_name = f'{date_time.year}-{date_time.month}-{date_time.day}_{title_without_punctuation}'
    image_file_name += '.' + image_url.split('.')[-1]
    
    nb_tries = 5
    while nb_tries:
        time.sleep(random.randint(2, 5))
        res = requests.get(image_url, stream=True, headers=random.choice(user_agents))
        if res.status_code == 200:
            try:
                with open(os.path.join('drive' ,'MyDrive', 'scraping', 'img', image_file_name), 'wb') as f:
                    shutil.copyfileobj(res.raw, f)
                    back_img_path = image_file_name
            except:
                pass
            else:
                break
        else:
            nb_tries -= 1
    if nb_tries == False:
        return None
    
    date_time = f'{date_time.year}-{date_time.month}-{date_time.day}'
    return [date_time, title_with_punctuation, image_file_name, back_text, image_url]


def save_to_csv(var_list, file_name):
    """Save a list to a csv file
    Args:
        - var_list: a list of elements to be saved
        - file_name: the name of the file saved
    Return nothing
    """   
    # opening the csv file in 'w+' mode
    file = open(os.path.join('drive', 'MyDrive', 'scraping', file_name), 'w+', newline ='')
    
    # writing the data into the file
    with file:   
        write = csv.writer(file)
        write.writerows(var_list)


# -------------------------------------------- main -------------------------------------------- 


BASE_URL = 'https://mathdatasimplified.com/'
df_columns = ['date', 'front', 'back_img_path', 'back_text', 'image_url']
df = pd.DataFrame(columns=df_columns)
current_directory = os.getcwd()

blog_pages_not_scraped, blog_entries_not_scraped = [], []


for i in range(1, 3): # 64

    # parse all the blog webpages (not entries)
    web_page_url = BASE_URL + 'page/' + str(i)

    print(web_page_url)
    req_response = retrieve_webpage(web_page_url)
    if not req_response:
        blog_pages_not_scraped.append(web_page_url)
        break

    soup = get_soup_from_req(req_response)
    if not soup:
        blog_pages_not_scraped.append(web_page_url)
        break

    
    # get all blog entries of a specific webpage 
    entries_urls = []
    for tag in soup.find_all("h2")[:-1]:
        entries_urls.append(str(tag.find_all(href=True)[0]).split('<a href="')[1].split('" rel')[0])
    
    # scrape all blog entries
    for entry_url in entries_urls:

        print(entry_url)

        req_response = retrieve_webpage(entry_url)
        if not req_response:
            blog_entries_not_scraped.append(entry_url)
            break

        soup = get_soup_from_req(req_response)
        if not soup:
            blog_entries_not_scraped.append(entry_url)
            break

        # skip entries with video tutorials
        if 'youtu' in str(soup) or 'video' in str(soup) or 'Video' in str(soup):
            continue

        # retrieve all infos
        entry_infos = extract_blog_entry_content(soup)
        if entry_infos is None:
            blog_entries_not_scraped.append(entry_url)
            continue
        
        # append dataframe
        new_row = pd.DataFrame(entry_infos).T
        new_row.columns = df_columns
        df = pd.concat([df, new_row], axis=0)


df.to_csv(os.path.join('drive', 'MyDrive', 'scraping', 'mathdatasimplified_data.csv'))

save_to_csv(blog_pages_not_scraped, 'blog_pages_not_scraped.csv')
save_to_csv(blog_entries_not_scraped, 'blog_entries_not_scraped.csv')

print('\n\nend')
print('blog_pages_not_scraped')
print(blog_pages_not_scraped)
print('blog_entries_not_scraped')
print(blog_entries_not_scraped)