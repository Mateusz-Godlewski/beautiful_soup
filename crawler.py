import requests
from bs4 import BeautifulSoup

for i in range(0, 10000):
    site = "https://mateusz-godlewski.github.io/cv/"
    data = requests.get(url=site)
    data = data.text
    print(i)