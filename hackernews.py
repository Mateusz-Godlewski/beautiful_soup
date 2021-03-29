import requests
from bs4 import BeautifulSoup


site = "https://news.ycombinator.com/news"
data = requests.get(url=site)
data = data.text
id_list = []
id_clean = []
inject = "score_"
maximum = 0
minimum = 99999999
id_of_highest_raw = ""
id_of_lowest_raw = ""

soup = BeautifulSoup(data, "html.parser")
for item in soup.find_all(class_="athing"):
    id_list.append(item.get("id"))
for id_num in id_list:
    ready_data = inject + id_num
    id_clean.append(ready_data)
for item in id_clean:
    split_data = int(soup.find(id=item).getText().split()[0])
    if split_data > maximum:
        maximum = split_data
        id_of_highest_raw = item
    if split_data < minimum:
        minimum = split_data
        id_of_lowest_raw = item
id_of_highest = id_of_highest_raw.split("_")[1]
id_of_lowest = id_of_lowest_raw.split("_")[1]
link_to_article_max = soup.find(id=id_of_highest).find(name="a", class_="storylink").get("href")
link_to_article_min = soup.find(id=id_of_lowest).find(name="a", class_="storylink").get("href")

print(f"{link_to_article_max} is the most upvoted article with {maximum} upvotes")
print(f"{link_to_article_min} is the least upvoted article with {minimum} upvotes")
