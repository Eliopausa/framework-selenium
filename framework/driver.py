# coding: utf-8

from selenium import webdriver
from framework.singleton import Singleton
from selenium.webdriver.chrome.service import Service


class Driver(metaclass=Singleton):
    """ Класс-синглтон веб-драйвера. """
    def __init__(self):
        # TODO: Сделать экземпляр для других браузеров: FireFox и т.д.
        self.chrome = webdriver.Chrome(
            service=Service(executable_path="drivers/chrome/chromedriver.exe"),
            options=webdriver.ChromeOptions())
