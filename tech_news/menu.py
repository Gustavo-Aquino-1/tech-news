import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_categories

# Requisitos 11 e 12

options = """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por categoria;
 4 - Listar top 5 categorias;
 5 - Sair."""


def analyzer_menu():
    guide = {
        "0": [get_tech_news, "Digite quantas notícias serão buscadas:"],
        "1": [search_by_title, "Digite o título:"],
        "2": [search_by_date, "Digite a data no formato aaaa-mm-dd:"],
        "3": [search_by_category, "Digite a categoria:"],
        "4": [top_5_categories],
        "5": [lambda: print('Encerrando script')]
    }
    try:
        print(options)
        option = input()

        if not guide.get(option):
            raise Exception

        param = None
        if len(ar := guide.get(option)) == 2:
            param = input(ar[1])

        print(ar[0]() if not param else ar[0](param))

    except Exception:
        sys.stderr.write("Opção inválida\n")
