from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
movies_page = response.text

soup = BeautifulSoup(movies_page, "html.parser")
article_texts = []
articles = soup.find_all(name = "h3", class_ = "title")
for article in articles:
    article_texts.append(article.get_text())

movie_rankings = article_texts[::-1]
print(movie_rankings)

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movie_rankings:
        file.write(f"{movie}\n")