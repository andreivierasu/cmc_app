import os
import json
from logging import getLogger
from models.news import NewsDTO


def get_news():
    cwd = os.getcwd()
    f = open(os.path.join(cwd,"news_data.json"), "r")
    data = f.read()
    f.close()
    parsed_data = json.loads(data)
    dto_list = []
    for dto in parsed_data:
        dto_list.append(NewsDTO(dto["title"], dto["content"], dto["date"], dto["author"], dto["pictures"]))
    return dto_list

