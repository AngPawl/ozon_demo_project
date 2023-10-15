import allure
from selene import browser

from ozon_demo_project.components.cookie_popup import CookiePopup
from ozon_demo_project.components.header import Header
from ozon_demo_project.pages.search_result_page import SearchResultPage


class ApplicationManager:
    def __init__(self):
        self.header = Header()
        self.cookie_popup = CookiePopup()
        self.search_result_page = SearchResultPage()

    @staticmethod
    @allure.step('Открыть веб-приложение')
    def open():
        browser.open('/')


app = ApplicationManager()
