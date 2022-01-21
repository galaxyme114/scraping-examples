"""
It is a simple python web scraping library. It is an efficient HTTP
library used for accessing web pages. With the help of Requests, we
can get the raw HTML of web pages which can then be parsed for retrieving
the data.
"""
import requests
res = requests.get('https://medcombo.com/')
print(res.text)  # print(res.text[:200])
