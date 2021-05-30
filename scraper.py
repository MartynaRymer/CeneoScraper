from bs4 import BeautifulSoup
import requests
import json

def get_feature(dom_tree,selector,attribute=None):
    try:
        if isinstance(attribute,str):
            return dom_tree.select_one(selector)[attribute].strip()
        if isinstance(attribute,list):
            return [element.text.strip() for element in dom_tree.select(selector)]
        else:
            return dom_tree.select_one(selector).text.strip()
    except (AttributeError,TypeError):
        return None

next_page = 'https://www.ceneo.pl/63419968#tab=reviews'
all_opinions = []

while next_page:
    respons = requests.get(next_page)

    page_dom = BeautifulSoup(respons.text, "html.parser")
    opinions = page_dom.select("div.js_product-review")



    for opinion in opinions:
        single_opinion = {
        "opinion_id": opinion["data-entry-id"],
        "author": get_feature(opinion,"span.user-post__author-name"),
        "recomm": get_feature(opinion,"span.user-post__author-recomendation"),
        "stars": get_feature(opinion,"span.user-post__score-count"),
        "content": get_feature(opinion,"div.user-post__text"),
        "pros": get_feature(opinion,"div.review-feature__title--positives ~ div.review-feature__item",[]),
        "cons": get_feature(opinion,"div.review-feature__title--negatives ~ div.review-feature__item",[]),
        "useful": get_feature(opinion,"button.vote-yes > span"),
        "useless": get_feature(opinion,"button.vote-no > span"),
        "purchased": get_feature(opinion,"div.review-pz"),
        "publish_date": get_feature(opinion,"span.user-post__published > time:nth-child(1)","datetime"),
        "purchase_date": get_feature(opinion,"span.user-post__published > time:nth-child(2)","datetime")
        }
        all_opinions.append(single_opinion)

    try:
        next_page = 'https://www.ceneo.pl' + get_feature(page_dom, "pagination__next", "href")
    except TypeError:
        next_page = None

with open("opinions/63419968.json","w",encoding="UTF-8") as jf:
    json.dump(all_opinions, jf, indent=4,ensure_ascii=False)

#print(json.dumps(all_opinions, indent=4,ensure_ascii=False))