from models.news import NewsDTO
from datetime import datetime
from helpers.helpers import get_news

def test_news_dto_class_initilization():
    title = "Soc"
    content = "Mare accident"
    create_date = datetime.now()
    author = "Jean"
    images = ["picture1", "picture2"]
    news = NewsDTO(title, content, create_date, author, images)
    assert news.author == author
    assert news.content == content
    assert news.date == create_date
    assert news.pictures == images

def test_reading_json_data():
    news = get_news()
    print(news)