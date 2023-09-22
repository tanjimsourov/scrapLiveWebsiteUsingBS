from bs4 import BeautifulSoup
import requests
response = requests.get("https://news.ycombinator.com/news")

yc_wbPage = response.text

soup = BeautifulSoup(yc_wbPage,"html.parser")
articles = soup.findAll(name="a",rel = "noreferrer")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.get_text()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)
article_upvotes =[ int(score.getText().split()[0]) for score in soup.findAll(name="span",class_="score") ]

print(article_texts)
print(article_links)
print(article_upvotes)
