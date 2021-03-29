import requests
from bs4 import BeautifulSoup


site = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url=site)
data = response.text
soup = BeautifulSoup(data, "html.parser")
titles = []
for item in soup.find_all(name="h3"):
    titles.append(str(item.getText()).replace(")", ":")+"\n")
titles.reverse()
with open("movies.txt" , 'w') as file:
    for item in titles:
        file.write(item)

# DATA FROM WEBSITE HAS BEEN REWORKED? USED WAYBACK MACHINE TO ACCESS PREVIOUS VERSION OF THE WEBSITE

# for item in soup.find_all(class_="jsx-3821216435"):
#     try:
#         line = str(item.find(class_="jsx-4245974604").img)
#     except AttributeError:
#         pass
#     try:
#         title = line.split("=")[1].split("class")[0].strip('"').split('"')[0]
#     except IndexError:
#         pass
#     try:
#         if title not in titles:
#             if title != "100 Greatest Movies":
#                 titles.append(title.title())
#     except NameError:
#         pass
# print(titles)
