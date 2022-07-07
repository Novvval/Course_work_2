from flask import jsonify, Blueprint
import logging
from api_test.api_utils import get_posts, get_post


api_blueprint = Blueprint("api_blueprint", __name__)
logging.basicConfig(filename='api.log', level=logging.DEBUG, encoding="utf-8", format="%(asctime)s [%(levelname)s] %(message)s")


@api_blueprint.route("/api/posts/")
def get_posts_all():
    posts = get_posts()
    logging.info("запрошены все посты")
    return jsonify(posts)


@api_blueprint.route("/api/posts/<int:pid>")
def get_one_post(pid):
    post = get_post(pid)
    logging.info(f"запрошен пост {pid}")
    return jsonify(post)


