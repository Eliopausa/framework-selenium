from framework.driver import Driver


class BaseTest:
    """ Базовый класс для тест-кейсов. """
    def __init__(self):
        self.browser = Driver().chrome

    def setup(self) -> None:
        """ Подготавливает тестовое окружение для теста. """
        self.browser.get(url="https://vk.com")

    def teardown(self) -> None:
        """ Очищает тестовые данные и удаляет
            окружение после выполнения теста. """
        pass

z