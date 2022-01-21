import re
import urllib.request
res = urllib.request.urlopen('http://example.webscraping.com/places/default/view/India-102')
html = res.read()
text = html.decode()
print(re.findall('<td class="w2p_fw">(.*?)</td>', text))