import os
import requests
import file_paths

from bs4 import BeautifulSoup
from check_list import CheckList

datasets_links = []
def get_csv_links(datasets_links) -> list:

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Fedora;Linux x86; rv:60.0) Gecko/20100101 Firefox/60.0'}
    request = requests.get('https://data.ibb.gov.tr/dataset/hourly-public-transport-data-set',headers=headers)
    
    soup = BeautifulSoup(request.text, 'html.parser')
    
    data = soup.findAll('div', {"class": "data-btn"})
    for div in data:
        for childdiv in div.findAll('a')[1:]:
            datasets_links.append(childdiv["href"])

    CheckList.check_empty()
    # equal = CheckList.check_equal(datasets_links,file_paths.links_file)
    # diff = CheckList.check_diff(datasets_links,file_paths.links_file)
    
    print(datasets_links)
    # if equal: print(equal)
    # print(diff)
    # pandasop.PandasOperations(datasets_links)

        
get_csv_links(datasets_links)





