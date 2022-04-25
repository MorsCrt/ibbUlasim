import requests
import sys
from pathlib import Path
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))
from bs4 import BeautifulSoup


def get_csv_links() -> list:
    datasets_links = []

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Fedora;Linux x86; rv:60.0) Gecko/20100101 Firefox/60.0'}
    request = requests.get('https://data.ibb.gov.tr/dataset/hourly-public-transport-data-set',headers=headers)
    
    soup = BeautifulSoup(request.text, 'html.parser')
    
    data = soup.findAll('div', {"class": "data-btn"})
    for div in data:
        for childdiv in div.findAll('a')[1:]:
            datasets_links.append(childdiv["href"])
    
    datasets_links.append("https://data.ibb.gov.tr/dataset/015e8185-d59c-47c1-a4cf-8d7fc709ef44/resource/12f5bc23-224a-43cb-b60d-3f36f83ffd33/download/ibb_wifi_subscriber.csv")     
    return datasets_links
