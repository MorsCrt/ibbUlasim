import requests
from bs4 import BeautifulSoup
import time


headers = {'User-Agent': 'Mozilla/5.0 (X11; Fedora;Linux x86; rv:60.0) Gecko/20100101 Firefox/60.0'}
request = requests.get('https://data.ibb.gov.tr/dataset/hourly-public-transport-data-set',headers=headers)

soup = BeautifulSoup(request.text, 'html.parser')


datasets_links = []
def get_csv(datasets_links):
    data = soup.findAll('div', {"class": "data-btn"})
    for div in data:
        for childdiv in div.findAll('a')[1:]:
            datasets_links.append(childdiv["href"])
            
start_time = time.time()
get_csv(datasets_links)
print("--- %s seconds ---" % (time.time() - start_time))


# childdiv.text.split("Popüler")[0]




# import requests
# from bs4 import BeautifulSoup

# headers = {'User-Agent': 'Mozilla/5.0 (X11; Fedora;Linux x86; rv:60.0) Gecko/20100101 Firefox/60.0'}
# request = requests.get('https://data.ibb.gov.tr/dataset/hourly-public-transport-data-set',headers=headers)

# soup = BeautifulSoup(request.text, 'html.parser')
# data = soup.findAll('div', {"class": "data-name"})

# datasets = []
# for div in data:
#     for childdiv in div.findAll('div'):
#         print(childdiv["href"]+"/download/hourly_transportation_202001.csv")
        

# # childdiv.text.split("Popüler")[0]



