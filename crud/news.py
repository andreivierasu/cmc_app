from models.news import NewsDTO
from helpers.helpers import create_news, get_news

class NewsCrudManager:

    def create(self, news: NewsDTO) -> NewsDTO:
        create_news(news)
        return news

    def read(self) -> list[NewsDTO]:
        return get_news()

    def update(self) -> None:
        pass

    def delete(self) -> None:
        pass