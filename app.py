from flask import Flask, render_template, request, redirect, url_for
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
    crud_manager = NewsCrudManager()
    all_news = crud_manager.read()
    return render_template("all_news.html", news=all_news)

@app.route("/news/<int:news_id>", methods=["GET"])
def read_news_article(news_id: int):
    crud_manager = NewsCrudManager()
    news_article = crud_manager.read(news_id=news_id)
    return render_template("news_article.html", news=news_article)
    

@app.route("/news/<int:news_id>/update", methods=["GET"])
def get_news_update_form(news_id:int):
    crud_manager = NewsCrudManager()
    news = crud_manager.read(news_id=news_id)
    return render_template("news_edit_form.html", news=news)

@app.route("/news/<int:news_id>/update", methods=["POST"])
def news_update(news_id:int):
    news_id = request.form.get("news_id")
    title = request.form.get("title")
    content = request.form.get("content")
    date = request.form.get("date")
    author = request.form.get("author")
    pictures = None
    if request.form.get("pictures") is not None:
        pictures = request.form.get("pictures").split(",")
    news = NewsDTO(title, content, date, author, pictures, news_id)
    crud_manager = NewsCrudManager()
    crud_manager.update(news)
    return redirect(url_for("read_news_article", news_id=news_id))

@app.route("/news/<int:news_id>/delete")
def delete_news(news_id: int):
    crud_manager = NewsCrudManager()
    crud_manager.delete(news_id)
    return redirect(url_for("read_news"))