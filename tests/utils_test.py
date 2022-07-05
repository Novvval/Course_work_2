import pytest
import utils
import os


class TestUtils:
    def test_get_posts_all(self):
        data = utils.get_posts_all()
        assert isinstance(data, list), "Ошибка загрузки файла"

    def test_get_by_tag(self):
        data = utils.get_by_tag("кот")
        assert isinstance(data, list), "Ошибка загрузки тегов"

    def test_get_posts_by_user(self):
        user = utils.get_posts_by_user("johnny")
        assert user["views_count"] == 233, "Ошибка при чтении пользователя"

    def test_get_comments_by_post_id(self):
        value = utils.get_comments_by_post_id(1)
        assert value["comment"] == "Очень здорово!", "Ошибка при чтении комментов"

    def test_search_for_posts(self):
        value = utils.search_for_posts("елки")
        assert value[0]["poster_name"] == "hank", "Ошибка при поиске"


if __name__ == '__main__':
    os.system("pytest")
