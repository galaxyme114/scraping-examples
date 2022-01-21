import requests
from bs4 import BeautifulSoup
import re
import csv

session = requests.Session()
url = 'https://github.com/{}'
username = 'ibragim'
def github_scrap():
    file_name = csv_make()
    repos_array = []
    res = session.get(url.format(username), params={'page': 1, 'tab': 'repositories'})
    soup = BeautifulSoup(res.text, 'lxml')
    repos_element = soup.find(class_='repo-list')
    if not repos_element:
        repos_element = soup.find(id='user-repositories-list')

    repos = repos_element.find_all('li')
    for repo in repos:
        name = repo.find('h3').find('a').get_text(strip=True)
        description = repo.find(attrs={'itemprop': 'description'})
        description = description.get_text(strip=True) if description else 'unknown'
        language = repo.find(attrs={'itemprop': 'programmingLanguage'})
        language = language.get_text(strip=True) if language else 'unknown'
        stars = repo.find('a', attrs={'href': re.compile('\/stargazers')})
        stars = stars.get_text(strip=True) if stars else 0
        temp = [name, description, language, stars]
        repos_array.append(temp)
    try:
        # write csv file from array
        with open(file_name, 'a', newline='', encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=',')
            for line in repos_array:
                writer.writerow(line)
        f.close()
        array.clear()  # 1D array initialization

    except:
        pass
def csv_make():
    try:
        file_name = 'github' + username + '.csv'
        header = ['Name', 'Description', 'Language', 'Stars']

        with open(file_name, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(header)
        f.close()
    except:
        pass
    return file_name

github_scrap()






