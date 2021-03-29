from bs4 import BeautifulSoup
import lxml


with open("website.html", encoding="utf-8") as data:
    content = data.read()

soup = BeautifulSoup(content, "lxml")
print(soup.find_all(name="a"))
for item in soup.find_all(name="a"):
    print(item.get("href"))