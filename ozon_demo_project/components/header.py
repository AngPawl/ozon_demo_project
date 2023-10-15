import allure
from selene import browser, have, be
from selene.support.conditions.have import exact_text


class Header:
    def __init__(self):
        self.titles = browser.all('[role="navigation"] a > span')
        self.logo = browser.element('#stickyHeader img')
        self.currency = browser.all('[role="navigation"] button span').first
        self.currency_dropdown = browser.element('input[name="filter"]')
        self.currency_options = browser.all('[role="option"] div')
        self.search_bar = browser.element('[action="/search"] input')

    @allure.step('Заголовки должны иметь следующие названия: {names}')
    def title_should_have_correct_names(self, names):
        self.titles.should(have.exact_texts(names))

    @allure.step('Логотип должен отображаться')
    def logo_should_render(self):
        self.logo.should(be.visible)

    @allure.step('Поменять валюту на {target_currency}')
    def change_currency(self, target_currency):
        self.currency.click()
        self.currency_dropdown.click()
        self.currency_options.element_by(exact_text(target_currency)).click()

    @allure.step('Валюта должна отображаться как {currency}')
    def currency_name_should_be_correct(self, currency):
        self.currency.should(have.exact_text(currency))

    @allure.step('Ввести запрос {query} в поисковое поле')
    def type_search_query(self, query):
        self.search_bar.send_keys(query).press_enter()
