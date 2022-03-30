import logging
from selenium import webdriver
from selenium.common.exceptions import *

from reali_web.conftest import take_screenshot
from reali_web.wait import wait_options
from reali_web.echo_pages.main_page import main_page_locators
from reali_web.echo_pages.requests_tab import requests_tab
from reali_web.echo_pages.requests_tab.verification_tab import verification_tab_page

wf = wait_options.wait_functions
mpl = main_page_locators.MainPageLocators
rt = requests_tab.RequestsTab
vtp = verification_tab_page.VerificationTabPage


class MainPage:
    @staticmethod
    def validate_navigation_to_main_page(driver: webdriver):
        try:
            wf.wait_for_element(driver, mpl.CHAT_CARD)
            driver.find_element(*mpl.CHAT_CARD)
            logging.info('validate_navigation_to_main_page')
            print('validate_navigation_to_main_page')
            return True
        except NoSuchElementException as err:
            logging.error('did not validate_navigation_to_main_page')
            print('did not validate_navigation_to_main_page')
            take_screenshot(driver, 'validate_navigation_to_main_page')
            raise err

    @staticmethod
    def validate_change_request_status(driver: webdriver, status_option: str):
        try:
            rt.click_on_requests_tab(driver)
            assert vtp.click_on_verifications_tab(driver)
            assert vtp.click_on_status_field(driver)
            assert vtp.select_status_option(driver, status_option)
            logging.info('validate_change_request_status')
            print('validate_change_request_status')
            return True
        except (AssertionError, WebDriverException) as err:
            logging.error('did not validate_change_request_status')
            print('did not validate_change_request_status')
            take_screenshot(driver, 'validate_change_request_status')
            raise err
