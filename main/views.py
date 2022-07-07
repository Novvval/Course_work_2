from flask import Blueprint, render_template, request, redirect
from utils import search_for_posts, get_posts_by_user, get_posts_all, get_post_by_pk, get_comments_by_post_id, return_data, get_by_tag, add_bookmark, delete_bookmark

main_blueprint = Blueprint('main_blueprint', __name__, url_prefix="/", static_folder="/static")


@main_blueprint.route('/')
def get_all_posts():
    data = get_posts_all()
    bookmarks = len(return_data("data\\bookmarks.json"))
    return render_template("index.html", data=data, bookmarks=bookmarks)


@main_blueprint.route("/posts/<int:pid>")
def get_post(pid):
    post = get_post_by_pk(pid)
    comments = get_comments_by_post_id(pid)
    return render_template("post.html", post=post, comments=comments)


@main_blueprint.route("/search/")
def show_results():
    s = request.args["s"]
    valid_posts = search_for_posts(s)
    return render_template("search.html", posts=valid_posts)


@main_blueprint.route("/users/<username>")
def get_user(username):
    user_posts = get_posts_by_user(username)
    return render_template("users.html", user_posts=user_posts)


@main_blueprint.route("/tag/<tag>")
def get_tags(tag):
    posts = get_by_tag(tag)
    return render_template("tag.html", posts=posts, tag=tag)


@main_blueprint.route("/bookmarks/")
def get_bookmarks():
    bookmarks = return_data("data\\bookmarks.json")
    return render_template("bookmarks.html", bookmarks=bookmarks)


@main_blueprint.route("/bookmarks/add/<int:pid>")
def add_bookmark_by_pid(pid):
    add_bookmark(pid)
    return redirect("/", code=302)


@main_blueprint.route("/bookmarks/remove/<int:pid>")
def delete_bookmark_by_pid(pid):
    delete_bookmark(pid)
    return redirect("/bookmarks/", code=302)

