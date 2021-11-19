from flask import Blueprint, render_template, request, redirect, url_for
from .models import Post
from . import db
views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html")

@views.route("/about-me")
def about_me():
    return render_template("about-me.html")

@views.route("/posts/<page>")


def posts(page):
    posts = Post.query.all()
    posts.reverse()
    grouped = []
    for x in range(0, len(posts), 3):
        chunk = [posts[x:x+3]]
        grouped.insert(1, chunk)
    page = 1
    posts_by_page = grouped[page-1]
    return render_template("posts.html", posts_by_page = posts_by_page)



@views.route("/new-post", methods=["GET", "POST"])
def new_post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        
        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('auth.dashboard'))

    return render_template("new-post.html")

@views.route("/documentation")
def documentation():
    return render_template("documentation.html")

@views.route("/contact")
def contact():
    return render_template("contact.html")

