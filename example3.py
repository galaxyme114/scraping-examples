import requests
from bs4 import BeautifulSoup
import json
res = requests.get('https://authoraditiagarwal.com/')
soup = BeautifulSoup(res.text, 'lxml')
y = json.dumps(soup.title.text)
with open('JSONFile.txt', 'wt') as outfile:
    json.dump(y, outfile)