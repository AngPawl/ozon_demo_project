import allure
from selene import browser, be


class CookiePopup:
    def __init__(self):
        self.popup = browser.element('[data-widget="cookiePopup"]')
        self.accept_button = self.popup.all('button').first

    @allure.step('Куки попап должен отображаться на странице')
    def should_render(self):
        self.popup.should(be.visible)
        self.popup.should(be.clickable)

    @allure.step('Нажать на кнопку Accept All Cookies')
    def click_on_accept_button(self):
        self.accept_button.click()

    @allure.step('Куки попап пропадает')
    def should_disappear(self):
        self.popup.should(be.not_.visible)
