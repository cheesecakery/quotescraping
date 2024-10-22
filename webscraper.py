from bs4 import BeautifulSoup 
import requests
import json

quoteArr = []

html_text = requests.get()


# root = "https://quotes.toscrape.com/"
# pageNo = 1

# while True:
#     url = f'{root}/page/{pageNo}'
#     response = requests.get(url, timeout=5)
#     content = BeautifulSoup(response.content, "html.parser")

#     for quoteObject in content.find_all('div', attrs={"class": "quote"}):
#         quote = quoteObject.find('span', attrs={"class": "text"}).text 
#         author = quoteObject.find('small', attrs={"class": "author"}).text 
#         tags = list(map(lambda a : a.text, quoteObject.find_all('a', attrs={"class": "tag"})))
#         quoteArr.append({"quote": quote, "author": author, "tags": tags})

#     if content.find('li', attrs={"class": "next"}):
#         pageNo += 1
#     else:
#         break

# with open("quotesData.json", "w") as outfile: 
#     json.dump(quoteArr, outfile)
