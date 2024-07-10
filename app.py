from flask import Flask, render_template, request
from helpers.helpers import get_news
from models.news import NewsDTO
from crud.news import NewsCrudManager

app = Flask(__name__)

@app.route("/")
def home():
    news = get_news()
    return render_template("index.html", news=news)

@app.route("/news/create", methods=["POST"])
def create_news():
    title = request.form.get("title")
    content = request.form.get("content")
    date = request.form.get("date")
    author = request.form.get("author")
    pictures = request.form.get("pictures").split(",")
    news = NewsDTO(title, content, date, author, pictures)
    crud_manager = NewsCrudManager()
    created_news = crud_manager.create(news)
    return render_template("news_article.html", news=created_news)

@app.route("/news/create", methods=["GET"])
def get_news_form():
    return render_template("news_form.html")

@app.route("/news", methods=["GET"])
def read_news():
    news_manager = NewsCrudManager()
    all_news = news_manager.read()
    return render_template("all_news.html", news=all_news)