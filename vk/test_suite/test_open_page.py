from framework.base_test import BaseTest
from vk.pages.main_page import MainPage
from framework import base_test


class _OpenPage(BaseTest):
    def __init__(self):
        super().__init__()
        self.vk_main_page = MainPage()

    def test(self):
        self.vk_main_page.open()


class Test:
    """ Класс - контейнер для запуска
        теста при помощи pytest.
        Он нужен потому, что pytest
        принимает только классы без
        конструктора.
    """
    _OpenPage().test()


if __name__ == '__main__':
    _OpenPage().test()

