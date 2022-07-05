import json


def return_data(path):
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_posts_all():
    return return_data("data/data.json")


def get_posts_by_user(name):
    data = return_data("data/data.json")
    posts = []
    for item in data:
        if item["poster_name"] == name:
            posts.append(item)
    return posts


def get_comments_by_post_id(post_id):
    data = return_data("data/comments.json")
    comments = []
    for item in data:
        if item["post_id"] == post_id:
            comments.append(item)
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
    for item in data:
        if item["pk"] == pk:
            return item


def get_by_tag(tag):
    data = return_data("data/data.json")
    posts = []
    for item in data:
        if f"#{tag}" in item["content"]:
            posts.append(item)
    return posts


def add_bookmark(post_id):
    post = get_post_by_pk(post_id)
    with open("data/bookmarks.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        if post not in data:
            data.append(post)
    with open("data/bookmarks.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def delete_bookmark(post_id):
    with open("data/bookmarks.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        for item in data:
            if item["pk"] == post_id:
                data.remove(item)
    with open("data/ookmarks.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
