import os
from flask import json


def get_posts():
    with open("data/data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_post(pid):
    data = get_posts()
    for post in data:
        if post["pk"] == pid:
            return post
