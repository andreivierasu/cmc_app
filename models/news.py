from datetime import datetime


# Data Transfer Object for News
class NewsDTO:
    def __init__(self, title:str, content:str, date:datetime, author:str, pictures:list[str], news_id=None) -> None:
        self.title = title
        self.content = content
        self.date = date
        self.author = author
        self.pictures = pictures
        self.news_id = news_id

    def __repr__(self) -> str:
        return f"<NewsDTO(news_id={self.news_id}, title={self.title}, content={self.content}, date={self.date}, author={self.author})>"