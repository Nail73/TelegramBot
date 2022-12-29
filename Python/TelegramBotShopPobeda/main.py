import requests
import json
from bs4 import BeautifulSoup


def get_first_comp():
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    }

    url = "https://xn---63-5cdesg4ei.xn--p1ai/catalog/kompyuternaya-tehnika/sistemnye-bloki/"
    r = requests.get(url=url, headers=headers)
    r.encoding = 'utf-8'
    page = r.text

    soup = BeautifulSoup(page, "lxml")
    articles_cards = soup.find_all("a", class_="card-title")

    comp_dict = {}
    for article in articles_cards:
        article_url = article.get("href")
        article_id = article_url.split("-")[-1][:-1]
        article_title = article.get("title")

        comp_dict[article_id] = {
            'article_title': article_title,
            'article_url': article_url
        }

    with open('comp_dict.json', 'w') as file:
        json.dump(comp_dict, file, indent=4, ensure_ascii=False)


def check_comp_update():
    with open('comp_dict.json') as file:
        comp_dict = json.load(file)

    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    }

    url = "https://xn---63-5cdesg4ei.xn--p1ai/catalog/kompyuternaya-tehnika/sistemnye-bloki/"
    r = requests.get(url=url, headers=headers)
    r.encoding = 'utf-8'
    page = r.text

    soup = BeautifulSoup(page, "lxml")
    articles_cards = soup.find_all("a", class_="card-title")

    fresh_comp = {}

    for article in articles_cards:
        article_url = article.get("href")
        article_id = article_url.split("-")[-1][:-1]

        if article_id in comp_dict:
            continue
        else:
            article_title = article.get("title")

        comp_dict[article_id] = {
            'article_title': article_title,
            'article_url': article_url
        }
        fresh_comp[article_id] = {
            'article_title': article_title,
            'article_url': article_url
        }

    with open('comp_dict.json', 'w') as file:
        json.dump(comp_dict, file, indent=4, ensure_ascii=False)

    return fresh_comp


def main():
    # get_first_comp()
    print(check_comp_update())


if __name__ == '__main__':
    main()
