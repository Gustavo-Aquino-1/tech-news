from tech_news.database import db

# import pymongo


# Requisito 10

# No MongoDB, ao usar a etapa $group em uma pipeline,
#  é necessário usar o campo _id para especificar o
# campo que será usado como identificador exclusivo
# para agrupamento. O campo _id é especial e obriga-
# tório na etapa $group.


def top_5_categories():
    pipeline = [
        {
            "$group": {
                "_id": "$category",
                "count": {"$sum": 1},
            }
        },
        {"$sort": {"count": -1, "_id": 1}},
        {"$limit": 5},
    ]
    return [x["_id"] for x in list(db.news.aggregate(pipeline))]
