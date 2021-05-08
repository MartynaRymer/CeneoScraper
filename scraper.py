import requests
from bs4 import BeautifulSoup

respons = requests.get('https://www.ceneo.pl/63419968#tab=reviews')

page_dom = BeautifulSoup(respons.text, "html.parser")
#print(page_dom.prettify())

opinions = page_dom.select("div.js_product-review")
opinion = opinions.pop(0)

opinion_id = opinion["data-entry-id"]
author = opinion.select_one("span.user-post__author-name").get_text().strip()
recomm = opinion.select_one("span.user-post__author-recomendation").get_text().strip()
stars = opinion.select_one("span.user-post__score-count").get_text().strip()
content = opinion.select_one("div.user-post__text").get_text().strip()
pros = opinion.select("div.review-feature__title--positives ~ review-feature__item")
cons = opinion.select("div.review-feature__title--negatives ~ review-feature__item")
useful = opinion.select_one("button.vote-yes[data-total-vote]").get_text().strip()
useless = opinion.select_one("button.vote-no[data-total-vote]").get_text().strip()
purchased = opinion.select_one("div.review-pz").get_text().strip()
publish_date = opinion.select_one("span.user-post__published > time:nth-child(1)")["datetime"]
purchase_date = opinion.select_one("span.user-post__published > time:nth-child(2)")["datetime"]

print(opinion_id, author, recomm, stars, content, pros, cons, useful, useless, purchased, publish_date, purchase_date)
