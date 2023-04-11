from framework.base_test import BaseTest
from vk.pages.main_page import MainPage


class TestOpenPage(BaseTest):
    def __init__(self):
        super().__init__()
        self.vk_main_page = MainPage()

    def test(self):
        self.vk_main_page.open()


if __name__ == '__main__':
    TestOpenPage().test()
