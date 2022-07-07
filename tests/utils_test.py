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
        try:
            user = utils.get_posts_by_user("johnny")
            wrong_user = utils.get_posts_by_user("fgfgfgfg")
            assert user is not None, "Ошибка при чтении пользователя"
        except ValueError as e:
            pytest.fail(e, pytrace=True)

    def test_get_comments_by_post_id(self):
        value = utils.get_comments_by_post_id(1)
        assert value is not None, "Ошибка при чтении комментов"

    def test_search_for_posts(self):
        value = utils.search_for_posts("елки")
        assert value[0]["poster_name"] == "hank", "Ошибка при поиске"

    def test_get_post_by_pk(self):
        value = utils.get_post_by_pk(1)
        assert value is not None, "Ошибка при получении постов"


if __name__ == '__main__':
    os.system("pytest")
