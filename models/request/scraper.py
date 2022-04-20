import os
from pathlib import Path
import pandas as pd
import requests


from bs4 import BeautifulSoup
from check_list import CheckList


def get_csv_links() -> list:
    path = Path(os.path.dirname(os.path.abspath(__file__)))
    ibb_func_path = str(path.parent.parent.absolute())
    
    links_file_path = ibb_func_path + '\\Links\\datasets_links.txt'
    link_file_open = open(links_file_path, 'r')
    links_file = link_file_open.read().splitlines()
    link_file_open.close()
    
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Fedora;Linux x86; rv:60.0) Gecko/20100101 Firefox/60.0'}
    request = requests.get('https://data.ibb.gov.tr/dataset/hourly-public-transport-data-set',headers=headers)
    datasets_links = []
    
    soup = BeautifulSoup(request.text, 'html.parser')
    
    data = soup.findAll('div', {"class": "data-btn"})
    for div in data:
        for childdiv in div.findAll('a')[1:]:
            datasets_links.append(childdiv["href"])

    equal = CheckList.check_equal(datasets_links,links_file)
    diff = CheckList.check_diff(datasets_links,links_file)
    
    if equal: print(equal)
    print("test")
    # pandasop.PandasOperations(datasets_links)

        
get_csv_links()





