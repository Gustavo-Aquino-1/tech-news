from tech_news.database import db
import re


# Requisito 7
def search_by_title(title):
    regex = re.compile(title, re.IGNORECASE)
    news = db.news.find({"title": {"$regex": regex}})
    return [(x["title"], x["url"]) for x in news]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
