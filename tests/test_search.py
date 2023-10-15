import allure
from allure_commons.types import Severity

from ozon_demo_project.application import app


@allure.title('Поисковый запрос возвращает результаты поиска')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_send_valid_search_query():
    app.open()

    app.header.type_search_query('компьютер')

    app.search_result_page.search_query_returned_results()


@allure.title('Поисковый запрос не возвращает результаты поиска')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_send_invalid_search_query():
    app.open()

    app.header.type_search_query('123babracadabra')

    app.search_result_page.search_query_returned_no_results()
