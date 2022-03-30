import logging
import allure
import pytest

from reali_web.base_action import base_actions
from reali_web.echo_pages.login_page import login_page
from reali_web.echo_pages.main_page import main_page
from reali_web.conftest import Product
from reali_web.tests.config_experts import config_experts
from reali_web.tests.echo.sanity import config_echo

lp = login_page.LoginPage
ba = base_actions.BaseFunctions
mp = main_page.MainPage
ce = config_experts.ConfigExperts
co = config_echo.ConfigEcho


@pytest.mark.usefixtures('browser')
@allure.feature('echo')
@allure.description('test suite for echo sanity')
class TestRequestModification:
    @allure.title('test request modification')
    @pytest.mark.sanity
    def test_request_modification(self, browser, environment, echo_user_email, echo_password):
        allure.description(f'Running tests in: {environment} environment')
        logging.info(f'test_request_modification is running in: {environment} environment')
        print(f'test_request_modification is running in: {environment} environment')
        url, token = Product.echo(environment)
        ba.base_navigation(browser, url)
        lp.do_quick_login(browser, token)
        url, token = Product.echo(environment)
        ba.base_navigation(browser, url)
        assert mp.validate_navigation_to_main_page(browser)
        assert mp.validate_change_request_status(browser, co.STATUS_OPTION)
