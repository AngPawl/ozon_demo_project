import allure
from allure_commons.types import Severity

from ozon_demo_project.application import app


@allure.title('Заголовки в хедере имеют корректные наименования')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_header_titles_have_correct_names(browser_setup):
    app.open()

    app.header.title_should_have_correct_names(
        [
            'Стать продавцом',
            'Покупать как компания',
            'Мобильное приложение',
            'Помощь',
            'Пункты выдачи',
        ]
    )


@allure.title('В хедере отображается логотип')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_logo_should_render_on_the_page():
    app.open()

    app.header.logo_should_render()


@allure.title('Валюта успешно изменяется')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_change_currency():
    app.open()

    app.header.change_currency('USD')

    app.header.currency_name_should_be_correct('USD')
