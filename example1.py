import requests
from bs4 import BeautifulSoup
res = requests.get('https://authoraditiagarwal.com/')
soup = BeautifulSoup(res.text, 'lxml')
print(soup.title)
print(soup.title.text)