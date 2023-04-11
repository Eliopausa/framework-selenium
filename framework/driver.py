from selenium import webdriver
from framework.singleton import Singleton
from selenium.webdriver.firefox.options import Options


class Driver(metaclass=Singleton):
    def __init__(self):
        options = Options()
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        # self.firefox = webdriver.Firefox(
        #     executable_path=r"C:\Projects\selenium-framework\drivers\firefox\geckodriver.exe")
        self.chrome = webdriver.Chrome(
            executable_path=r"C:\Projects\selenium-framework\drivers\chrome\chromedriver.exe")
