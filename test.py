import requests
from bs4 import BeautifulSoup

url = "https://www.kozakdev.com/contact"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html5lib')
print(soup.prettyfy())