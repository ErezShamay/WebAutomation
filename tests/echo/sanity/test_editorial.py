import logging
import allure
import pytest

from reali_web.base_action import base_actions
from reali_web.echo_pages.login_page import login_page
from reali_web.tests.echo.sanity import config_echo
from reali_web.echo_pages.main_page import main_page
from reali_web.consumer_pages.buy.homes import homes_page
from reali_web.tests.consumer.anonymous_user import config_anon_search
from reali_web.consumer_pages.sell import sell_page
from reali_web.consumer_pages.sign.sign_up import sign_up_page
from reali_web.consumer_pages.sign.sign_in import sign_in_page
from reali_web.echo_pages.listings_tab import listings_tab_page
from reali_web.conftest import Product
from reali_web.tests.config_users import config_users
from reali_web.tests.config_experts import config_experts

lp = login_page.LoginPage
ba = base_actions.BaseFunctions
std_echo = config_echo.ConfigEcho
mp = main_page.MainPage
hp = homes_page.HomesPage
std_consumer = config_anon_search.ConfigAnonSearch
sp = sell_page.SellPage
sup = sign_up_page.SignUpPage
sip = sign_in_page.SignInPage
ltp = listings_tab_page.ListingsTabPage
cu = config_users.ConfigUsers
ce = config_experts.ConfigExperts


@pytest.mark.usefixtures('browser')
@allure.feature('echo')
@allure.description('test suite for echo sanity')
class TestEchoEditorialSanity:
    @allure.title('test editorial')
    @pytest.mark.sanity
    def test_editorial(self, browser, environment, echo_user_email, echo_password):
        allure.description(f'Running tests in: {environment} environment')
        logging.info(f'Running tests in: {environment} environment')
        print(f'running test test_editorial in {environment} environment')
        ba.base_navigation(browser, Product.consumer(environment))
        hp.validate_navigation_to_homes_primary_page(browser)
        hp.click_on_sell_tab(browser)
        sp.click_on_sell_option(browser)
        sp.click_on_get_started_button(browser)
        sp.send_keys_to_search_address(browser, std_echo.SELL_SEARCH_VALUE)
        sp.select_address_from_search_result(browser)
        sp.click_on_request_home_valuation(browser)
        sup.click_on_sign_in_button(browser)
        sip.validate_in_sign_in_page(browser)
        sip.send_keys_to_email(browser, ce.EMAIL)
        sip.send_keys_to_password(browser, ce.PASSWORD)
        sip.click_on_sign_in_button_in_sign_in_page(browser)
        assert sp.validate_congrats_message(browser)
        url, token = Product.echo(environment)
        ba.base_navigation(browser, url)
        lp.do_quick_login(browser, token)
        url, token = Product.echo(environment)
        ba.base_navigation(browser, url)
        assert mp.validate_navigation_to_main_page(browser)
