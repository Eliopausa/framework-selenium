from driver import Driver


class BasePage:
    def __init__(self):
        browser = Driver()
        self.browser = browser.chrome
        self.url = ''

    def open(self):
        self.browser.get(url=self.url)

    def close(self):
        pass


