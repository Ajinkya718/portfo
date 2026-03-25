from bs4 import BeautifulSoup
import requests
URL = "https://news.ycombinator.com/news"
response = requests.get(URL)

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name = "span", class_ = "titleline")
article_texts = []
article_links = []
scores = []
for article in articles:
    a_tag = article.find("a")
    article_texts.append(a_tag.get_text())
    article_links.append(a_tag.get("href"))
# print(article_texts)
# print(article_links)

upvotes = soup.find_all(name = "span", class_ = "score")
for upvote in upvotes:
    scores.append(int(upvote.get_text().split()[0]))
print(scores)

print(max(scores))
max_index = scores.index(max(scores))
print(max_index)

print(article_texts[max_index])
print(article_links[max_index])

