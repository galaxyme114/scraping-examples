import requests
import string
PAGE_SIZE = 15
url = 'http://example.webscraping.com/ajax/' + 'search.json?page={}&page_size={}&search_term=a'
countries = set()
for letter in string.ascii_lowercase:
   print('Searching with %s' % letter)
   page = 0
   while True:
       response=requests.get(url.format(page, PAGE_SIZE, letter))
       data = response.json()
       print('adding %d records from the page %d' %(len(data.get('records')),page))
   for record in data.get('records'):countries.add(record['country'])
   page += 1
   if page >= data['num_pages']:
      break
   with open('countries.txt', 'w') as countries_file:
   countries_file.write('n'.join(sorted(countries)))