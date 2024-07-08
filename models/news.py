# Data Transfer Object for News
class NewsDTO:
    def __init__(self, title, content, date, author, pictures) -> None:
        self.title = title
        self.content = content
        self.date = date
        self.author = author
        self.pictures = pictures