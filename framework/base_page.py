from framework.driver import Driver


class BasePage:
    """ Родительский класс для всех страниц тестируемого проекта. """

    def __init__(self):
        self.browser = Driver().chrome
        self.url = ''

    def open(self) -> None:
        """ Открыть страницу. """
        self.browser.get(url=self.url)

    def close(self) -> None:
        # TODO: Доделать или удалить позже
        pass
