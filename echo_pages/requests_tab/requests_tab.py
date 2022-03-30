import logging
from selenium import webdriver
from selenium.common.exceptions import *

from reali_web.conftest import take_screenshot
from reali_web.wait import wait_options
from reali_web.echo_pages.requests_tab import requests_tab_locators
from reali_web.base_action import base_actions

wf = wait_options.wait_functions
rtl = requests_tab_locators.RequestsTabLocators
ba = base_actions.BaseFunctions


class RequestsTab:
    @staticmethod
    def click_on_requests_tab(driver: webdriver):
        try:
            wf.wait_for_element(driver, rtl.REQUESTS_TAB)
            element = driver.find_element(*rtl.REQUESTS_TAB)
            element.click()
            logging.info('click_on_requests_tab')
            print('click_on_requests_tab')
            assert RequestsTab.validate_requests_menu_open(driver)
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_requests_tab')
            print('did not click_on_requests_tab')
            take_screenshot(driver, 'click_on_requests_tab')
            raise err

    @staticmethod
    def validate_requests_menu_open(driver: webdriver):
        try:
            wf.wait_for_element(driver, rtl.VERIFICATIONS_TAB)
            driver.find_element(*rtl.VERIFICATIONS_TAB)
            logging.info('validate_requests_menu_open')
            print('validate_requests_menu_open')
            return True
        except NoSuchElementException as err:
            logging.error('did not validate_requests_menu_open')
            print('did not validate_requests_menu_open')
            take_screenshot(driver, 'validate_requests_menu_open')
            raise err
