from tech_news.database import db
import re
import datetime


# Requisito 7
def search_by_title(title):
    regex = re.compile(title, re.IGNORECASE)
    news = db.news.find({"title": {"$regex": regex}})
    return [(x["title"], x["url"]) for x in news]


# Requisito 8
def format(str):
    return int(str[1]) if str[0] == "0" else int(str)


def search_by_date(date: str):
    try:
        year, month, day = [format(x) for x in date.split("-")]
        datetime.date(year, month, day)
        date = "/".join(list(reversed(date.split("-"))))
        news = db.news.find({"timestamp": date})
        return [(x["title"], x["url"]) for x in news]
    except Exception:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
