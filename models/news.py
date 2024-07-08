from datetime import datetime


# Data Transfer Object for News
class NewsDTO:
    def __init__(self, title:str, content:str, date:datetime, author:str, pictures:list[str]) -> None:
        self.title = title
        self.content = content
        self.date = date
        self.author = author
        self.pictures = pictures