import requests
import sys
from pathlib import Path
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))
from bs4 import BeautifulSoup

# from models.request.check_list import CheckList

def get_csv_links() -> list:
    datasets_links = []

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Fedora;Linux x86; rv:60.0) Gecko/20100101 Firefox/60.0'}
    request = requests.get('https://data.ibb.gov.tr/dataset/hourly-public-transport-data-set',headers=headers)
    
    soup = BeautifulSoup(request.text, 'html.parser')
    
    data = soup.findAll('div', {"class": "data-btn"})
    for div in data:
        for childdiv in div.findAll('a')[1:]:
            datasets_links.append(childdiv["href"])
            
    return datasets_links
            
    # pandasop.PandasOperations(datasets_links)
        
# CheckList.check_empty()
# equal = CheckList.check_equal(datasets_links,file_paths.link_formatted)
# diff = CheckList.check_diff(datasets_links,file_paths.link_formatted)
# print(diff)

