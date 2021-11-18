from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html")

@views.route("/about-me")
def about_me():
    return render_template("about-me.html")

@views.route("/posts")
def posts():
    return render_template("posts.html")

@views.route("/documentation")
def documentation():
    return render_template("documentation.html")

@views.route("/contact")
def contact():
    return render_template("contact.html")

