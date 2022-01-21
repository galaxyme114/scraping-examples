import requests
url = "https://authoraditiagarwal.com/wpcontent/uploads/2018/05/MetaSlider_ThinkBig-1080x180.jpg"
res = requests.get(url)
with open("ThinkBig.png", 'wb') as f:
    f.write(res.content)