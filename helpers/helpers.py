import os
import json
from models.news import NewsDTO


def get_news():
    cwd = os.getcwd()
    with open(os.path.join(cwd,"news_data.json"), "r") as f:
        data = f.read()
    parsed_data = json.loads(data)
    dto_list = []
    for dto in parsed_data:
        dto_list.append(NewsDTO(dto["title"], dto["content"], dto["date"], dto["author"], dto["pictures"]))
    return dto_list


def newsdto_list_to_dict_list(news_list: list[NewsDTO]) -> list[dict]:
    dict_list = []
    for news in news_list:
        dict_list.append(  
            {
            "title": news.title,
            "content": news.content,
            "date": news.date,
            "author": news.author,
            "pictures": news.pictures
            })
    return dict_list



def create_news(news: NewsDTO):
    all_news = get_news()
    all_news.append(news)
    cwd = os.getcwd()
    with open(os.path.join(cwd,"news_data.json"), "w") as f:
        f.write(json.dumps(newsdto_list_to_dict_list(all_news)))

