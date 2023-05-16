from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
import pytest

mock_news = [
    {
        "_id": {"$oid": "6463ec83c9ad31fa49a9ab52"},
        "url": "https://blog.betrybe.com/tecnologia/site-responsivo/",
        "title": "Site responsivo: o que é e 10 dicas para aplicar",
        "timestamp": "10/05/2023",
        "writer": "Lucas Marchiori",
        "reading_time": 11,
        "summary": "Com o avanço da tecnologia, grande parte das pessoas",
        "category": "Tecnologia",
    },
    {
        "_id": {"$oid": "6463ec83c9ad31fa49a9ab53"},
        "url": "https://blog.betrybe.com/tecnologia/modelo-as-a-service/",
        "title": "SaaS, GaaS, IaaS, DaaS, PaaS: entenda o modelo as a service",
        "timestamp": "27/04/2023",
        "writer": "Cairo Noleto",
        "reading_time": 14,
        "summary": "Você sabe o que é computação em nuvem?",
        "category": "Tecnologia",
    },
    {
        "_id": {"$oid": "6463ec83c9ad31fa49a9ab55"},
        "url": "https://blog.betrybe.com/tecnologia/componentizacao-tudo-s",
        "title": "Componentização: o que é, por que usar e exemplo na prát",
        "timestamp": "17/04/2023",
        "writer": "Cairo Noleto",
        "reading_time": 10,
        "summary": "Se você é uma pessoa programadora",
        "category": "Tecnologia",
    },
    {
        "_id": {"$oid": "6463ec83c9ad31fa49a9ab56"},
        "url": "https://blog.betrybe.com/tecnologia/10-navegadores-leves/",
        "title": "10 navegadores leves, rápidos e seguros para PC fraco!",
        "timestamp": "13/04/2023",
        "writer": "Cairo Noleto",
        "reading_time": 9,
        "summary": "Dá pra se imaginar sem internet? É por meio",
        "category": "Tecnologia",
    },
]


def test_reading_plan_group_news(monkeypatch):
    monkeypatch.setattr(
        ReadingPlanService,
        '_db_news_proxy',
        lambda: mock_news
    )
    news = ReadingPlanService.group_news_for_available_time(10)
    assert news == {
        "readable": [
            {
                "chosen_news": [
                    (
                        "Componentização: o que é, por que usar e "
                        "exemplo na prát",
                        10,
                    )
                ],
                "unfilled_time": 0,
            },
            {
                "chosen_news": [
                    (
                        "10 navegadores leves, rápidos e seguros para "
                        "PC fraco!",
                        9,
                    )
                ],
                "unfilled_time": 1,
            },
        ],
        "unreadable": [
            ("Site responsivo: o que é e 10 dicas para aplicar", 11),
            (
                "SaaS, GaaS, IaaS, DaaS, PaaS: entenda o modelo as a service",
                14,
            ),
        ],
    }

    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(-10)
