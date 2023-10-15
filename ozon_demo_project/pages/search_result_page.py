import allure
from selene import browser, be


class SearchResultPage:
    def __init__(self):
        self.some_results_header = browser.element(
            '[data-widget="fulltextResultsHeader"]'
        )
        self.no_results_header = browser.element('[data-widget="searchResultsError"]')

    @allure.step('Поисковый запрос вернул результаты')
    def search_query_returned_results(self):
        self.some_results_header.should(be.visible)

    @allure.step('Поисковый запрос не вернул результаты')
    def search_query_returned_no_results(self):
        self.no_results_header.should(be.visible)
