import allure
from allure_commons.types import Severity

from ozon_demo_project.application import app


@allure.title('Куки попап отображается на странице')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_cookie_popup_should_appear_on_the_page():
    app.open()

    app.cookie_popup.should_render()


@allure.title('Куки попап пропадает после нажатия на кнопку Accept All Cookies')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_cookie_popup_should_disappear_after_accept_button_is_pressed():
    app.open()

    app.cookie_popup.click_on_accept_button()

    app.cookie_popup.should_disappear()
