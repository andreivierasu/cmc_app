from models.news import NewsDTO
from helpers.helpers import create_news, get_news, update_news

class NewsCrudManager:

    def create(self, news: NewsDTO) -> NewsDTO:
        create_news(news)
        return news

    def read(self, news_id=None) -> list[NewsDTO]|None|NewsDTO:
        all_news = get_news()
        if news_id is None:
            return all_news
        for news in all_news:
            if news.news_id == news_id:
                return news
        return None

    def update(self,news) -> NewsDTO|KeyError:
        if news.news_id is None:
            raise KeyError("You forgot to specify a news ID!")
        updated_news = update_news(news)
        if updated_news is None:
            raise ValueError(f"There is no news with ID {news.news_id}!")
        return updated_news
        

    def delete(self) -> None:
        pass