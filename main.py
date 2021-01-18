from bs4 import BeautifulSoup
import requests

search = input("Enter a search term: ")
params={"q":search}
r = requests.get("https://www.bing.com/search",params=params)

soup = BeautifulSoup(r.text,"html.parser")
print(soup.prettify)
# results = soup.find("ol",{"id":"atvcap"})
# links = results.__getattribute__

# for item in links:
#     item_text = item.find("a").text
#     item_href = item.find("a").attrs["href"]

#     if item_text and item_href:
#         print(item_text)
#         print(item_href)
