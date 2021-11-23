from flask import Blueprint, render_template, request, redirect, url_for
from .models import Post, Link
from . import db
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
    posts = Post.query.all()
    posts.reverse()
    grouped = []
    for x in range(0, len(posts), 3):
        chunk = [posts[x:x+3]]
        grouped.insert(1, chunk)

    page = request.args.get('page', default = 1, type = int)
    posts_by_page = grouped[page-1]

    previous = page-1
    if previous == 0:
        previous_page = 'posts?page='+str(page)
    else:
        previous_page = "posts?page="+str(previous)

    next = page+1
    if next > len(grouped):
        next_page = 'posts?page='+str(page)
    else:
        next_page = "posts?page="+str(next)

    return render_template("posts.html", posts_by_page = posts_by_page, page = page, previous_page = previous_page, next_page = next_page)

@views.route("/new-post", methods=["GET", "POST"])
def new_post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        image = request.form.get('image')
        
        new_post = Post(title=title, content=content, image=image)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('auth.dashboard'))

    return render_template("new-post.html")

@views.route("/edit-posts", methods=["GET", "POST"])
def edit_posts():
    if request.method == 'POST':
        title = request.form.get('title')
        url ='/edit-post?title='+title

        return redirect(url)

    return render_template("edit-posts.html")

@views.route("/edit-post", methods=["GET", "POST"])
def edit_post():
    title = request.args.get('title')
    post = Post.query.filter_by(title="test")
    if request.method == 'POST':
        post.title = request.form.get('title')
        post.content = request.form.get('content')
        post.image = request.form.get('image')
        db.session.commit()
        redirect='/dashboard'

        return redirect(url_for(redirect))
    
    return render_template("edit-post.html", former_title=post.title, former_content=post.content, former_image=post.image)

@views.route("/resources")
def documentation():
    links = Link.query.all()
    links.reverse()
    grouped_links = []
    for x in range(0, len(posts), 3):
        chunk_links = [posts[x:x+3]]
        grouped_links.insert(1, chunk_links)

    page_links = request.args.get('page', default = 1, type = int)
    links_by_page = grouped_links[page_links-1]

    previous_links = page_links-1
    if previous_links == 0:
        previous_page_links = 'links?page='+str(page_links)
    else:
        previous_page_links = "links?page="+str(previous_links)

    next_links = page_links+1
    if next_links > len(grouped_links):
        next_page_links = 'links?page='+str(page_links)
    else:
        next_page_links = "links?page="+str(next)

    return render_template("documentation.html", page_links = page_links, links_by_page = links_by_page, previous_page_links = previous_page_links, next_page_links = next_page_links)

@views.route("/new-link", methods=["GET", "POST"])
def new_link():
    if request.method == 'POST':
        title = request.form.get('title')
        text = request.form.get('text')
        link = request.form.get('link')
        
        new_link = Link(title=title, text=text, link=link)
        db.session.add(new_link)
        db.session.commit()
        return redirect(url_for('auth.dashboard'))

    return render_template("new-link.html")

@views.route("/contact")
def contact():
    return render_template("contact.html")

