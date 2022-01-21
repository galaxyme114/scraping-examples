import requests
from bs4 import BeautifulSoup
import csv
res = requests.get('https://authoraditiagarwal.com/')
soup = BeautifulSoup(res.text, 'lxml')
f = csv.writer(open('dataprocessing.csv', 'w'))
f.writerow(['Title'])
f.writerow([soup.title.text])