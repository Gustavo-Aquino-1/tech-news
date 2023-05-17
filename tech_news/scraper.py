import requests
from requests import ReadTimeout
from parsel import Selector
from time import sleep
from tech_news.database import create_news

# import scrapy


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
    news = selector.css("h2.entry-title > a::attr(href)").getall()  # pai > fil
    return news or []


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    return selector.css("a.next::attr(href)").get()


# Requisito 4
def get_time(str):
    num = ""
    for x in str:
        try:
            int(x)
            num += x
        except Exception:
            break
    return int(num)


def scrape_news(html_content):
    selector = Selector(html_content)
    news = {}
    # news['url'] = selector.css('h2.entry-title > a::attr(href)').get()
    news["url"] = selector.xpath('//link[@rel="canonical"]/@href').get()
    news["title"] = (
        selector.xpath('//h1[@class="entry-title"]/text()').get().strip()
    )
    news["timestamp"] = selector.xpath(
        '//ul[@class="post-meta"]/li[@class="meta-date"]/text()'
    ).get()
    news["writer"] = selector.xpath('//span[@class="author"]/a/text()').get()
    news["reading_time"] = (
        selector.xpath('//li[@class="meta-reading-time"]/text()').get().strip()
    )
    # strip para retirar espeços em branco e limpar o texto
    news["summary"] = "".join(
        selector.xpath('string(//div[@class="entry-content"]/p[1])')
        .get()
        .strip()
    )
    # p[1] para pegar apenas o primeiro paragrafo que satisfaça a condição
    news["category"] = selector.xpath('//span[@class="label"]/text()').get()
    news["reading_time"] = get_time(news["reading_time"])
    return news


# Requisito 5
def get_tech_news(amount):
    amount = int(amount)
    news, count = [], 0
    url = "https://blog.betrybe.com"
    while count < amount:
        content = fetch(url)
        news_url = scrape_updates(fetch(url))
        for u in news_url:
            news_details = fetch(u)
            news.append(scrape_news(news_details))
            count += 1
            if count == amount:
                break
        url = scrape_next_page_link(content)

    create_news(news)
    return news
