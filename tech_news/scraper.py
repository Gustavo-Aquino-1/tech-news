import requests
from requests import ReadTimeout
from parsel import Selector
from time import sleep


# Requisito 1
def fetch(url):
    try:
        sleep(1)
        response = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )
        if response.status_code == 200:
            return response.content.decode()
        return None
    except ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    news = selector.css('h2.entry-title > a::attr(href)').getall()  # pai > fil
    return news or []


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    return selector.css('a.next::attr(href)').get()


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
