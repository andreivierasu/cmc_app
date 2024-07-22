import os
import json
from models.news import NewsDTO

NEWS_FILE = "news_data_with_id.json"

def get_news():
    cwd = os.getcwd()
    with open(os.path.join(cwd,NEWS_FILE), "r") as f:
        data = f.read()
    parsed_data = json.loads(data)
    dto_list = []
    for news_dict in parsed_data:
        dto_list.append(NewsDTO(news_dict["title"], 
                                news_dict["content"], 
                                news_dict["date"], 
                                news_dict["author"], 
                                news_dict["pictures"], 
                                news_id=news_dict["news_id"]))
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
            "pictures": news.pictures,
            "news_id": news.news_id
            })
    return dict_list



def create_news(news: NewsDTO):
    all_news = get_news()
    all_news.append(news)
    cwd = os.getcwd()
    with open(os.path.join(cwd,NEWS_FILE), "w") as f:
        news_dict_list = newsdto_list_to_dict_list(all_news)
        news.news_id = len(news_dict_list) + 1
        f.write(json.dumps(news_dict_list))


def find_by_news_id(news_id: int, news_dict_list: list[dict[str,str]]):
    for to_update_news in news_dict_list:
        if to_update_news["news_id"] == int(news_id):
            return to_update_news
    return None


def update_news(news: NewsDTO) -> NewsDTO|None:
    all_news = get_news()
    news_dict_list = newsdto_list_to_dict_list(all_news)
    to_update_news = find_by_news_id(news.news_id, news_dict_list)
    if to_update_news is None:
        return None
    to_update_news["title"] = news.title
    to_update_news["content"] = news.content
    to_update_news["date"] = news.date
    to_update_news["author"] = news.author
    to_update_news["pictures"] = news.pictures
    cwd = os.getcwd()
    with open(os.path.join(cwd,NEWS_FILE), "w") as f:
        f.write(json.dumps(news_dict_list))
    return to_update_news
                