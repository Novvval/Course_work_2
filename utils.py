import json
import os
from exceptions import NoDataSource


def return_data(path):
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(absolute_path + "/" + path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        raise NoDataSource("Нет файла с данными, либо он поврежден")
    else:
        return data


def get_posts_all():
    return return_data("data/data.json")


def get_posts_by_user(name):
    data = return_data("data/data.json")
    posts = []
    for item in data:
        if item["poster_name"] == name:
            posts.append(item)
    if len(posts) == 0:
        raise ValueError("Нет такого пользователя")
    return posts


def get_comments_by_post_id(post_id):
    data = return_data("data/comments.json")
    comments = []
    for item in data:
        if item["post_id"] == post_id:
            comments.append(item)
    if len(comments) == 0:
        raise ValueError("нет такого поста")
    return comments


def search_for_posts(query):
    data = get_posts_all()
    valid_posts = []
    for item in data:
        if query.lower() in item["content"].lower():
            valid_posts.append(item)
    return valid_posts


def get_post_by_pk(pk):
    data = get_posts_all()
    post = {}
    for item in data:
        if item["pk"] == pk:
            post = item
        return post
    if not post:
        raise ValueError("Нет такого поста")


def get_by_tag(tag):
    data = return_data("data/data.json")
    posts = []
    for item in data:
        if f"#{tag}" in item["content"]:
            posts.append(item)
    if len(posts) == 0:
        raise ValueError("Нет такого тега")
    return posts


def add_bookmark(post_id):
    post = get_post_by_pk(post_id)
    try:
        with open("data/bookmarks.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            if post not in data:
                data.append(post)
        with open("data/bookmarks.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except (FileNotFoundError, json.JSONDecodeError):
        raise NoDataSource("Нет файла с данными, либо он поврежден")


def delete_bookmark(post_id):
    try:
        with open("data/bookmarks.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            for item in data:
                if item["pk"] == post_id:
                    data.remove(item)
        with open("data/ookmarks.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except (FileNotFoundError, json.JSONDecodeError):
        raise NoDataSource("Нет файла с данными, либо он поврежден")
