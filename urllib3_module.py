"""
It is Python library that can be used for retrieving data from URLs similar
to the requests library.
"""
import urllib3
from bs4 import BeautifulSoup
http = urllib3.PoolManager()
res = http.request('GET', 'https://authoraditiagarwal.com')
soup = BeautifulSoup(res.data, 'lxml')
print(soup.title)
print(soup.title.text)