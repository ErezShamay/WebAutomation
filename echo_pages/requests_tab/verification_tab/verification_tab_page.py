import logging
from selenium import webdriver
from selenium.common.exceptions import *

from reali_web.conftest import take_screenshot
from reali_web.wait import wait_options
from reali_web.echo_pages.requests_tab.verification_tab import verification_tab_page_locatoros
from reali_web.base_action import base_actions

wf = wait_options.wait_functions
vtpl = verification_tab_page_locatoros.VerificationTabPageLocators
ba = base_actions.BaseFunctions


class VerificationTabPage:
    @staticmethod
    def click_on_verifications_tab(driver: webdriver):
        try:
            wf.wait_for_element(driver, vtpl.VERIFICATIONS_TAB)
            element = driver.find_element(*vtpl.VERIFICATIONS_TAB)
            element.click()
            logging.info('click_on_verifications_tab')
            print('click_on_verifications_tab')
            assert VerificationTabPage.validate_navigated_to_verifications_table(driver)
            return True
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_verifications_tab')
            print('did not click_on_verifications_tab')
            take_screenshot(driver, 'click_on_verifications_tab')
            raise err

    @staticmethod
    def validate_navigated_to_verifications_table(driver: webdriver):
        try:
            wf.wait_for_element(driver, vtpl.VERIFICATIONS_TABLE)
            driver.find_element(*vtpl.VERIFICATIONS_TABLE)
            logging.info('validate_navigated_to_verifications_table')
            print('validate_navigated_to_verifications_table')
            return True
        except (NoSuchElementException, TimeoutException):
            logging.error('did not validate_navigated_to_verifications_table')
            print('did not validate_navigated_to_verifications_table')
            take_screenshot(driver, 'validate_navigated_to_verifications_table')
            return False

    @staticmethod
    def click_on_status_field(driver: webdriver):
        try:
            element = driver.find_element(*vtpl.STATUS_FIELD)
            element.click()
            logging.info('click_on_status_field')
            print('click_on_status_field')
            assert VerificationTabPage.validate_status_drop_down_is_open(driver)
            return True
        except (NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_status_field')
            print('did not click_on_status_field')
            take_screenshot(driver, 'click_on_status_field')
            raise err

    @staticmethod
    def validate_status_drop_down_is_open(driver: webdriver):
        try:
            wf.wait_for_element(driver, vtpl.STATUS_DROP_DOWN_MENU)
            driver.find_element(*vtpl.STATUS_DROP_DOWN_MENU)
            logging.info('validate_status_drop_down_is_open')
            print('validate_status_drop_down_is_open')
            return True
        except (NoSuchElementException, TimeoutException) as err:
            logging.error('did not validate_status_drop_down_is_open')
            print('did not validate_status_drop_down_is_open')
            take_screenshot(driver, 'validate_status_drop_down_is_open')
            raise err

    @staticmethod
    def select_status_option(driver: webdriver, status_option: str):
        try:
            if status_option == 'Pending':
                element = driver.find_element(*vtpl.PENDING)
                element.click()
            else:
                element = driver.find_element(*vtpl.WORKING)
                element.click()
            logging.info('select_status_option -> ' + status_option)
            print('select_status_option -> ' + status_option)
            assert VerificationTabPage.validate_toaster_message(driver)
            return True
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not select_status_option -> ' + status_option)
            print('did not select_status_option -> ' + status_option)
            take_screenshot(driver, 'select_status_option')
            raise err

    @staticmethod
    def validate_toaster_message(driver: webdriver):
        try:
            driver.find_element(*vtpl.TOASTER_MESSAGE)
            logging.info('validate_toaster_message')
            print('validate_toaster_message')
            return True
        except NoSuchElementException as err:
            logging.error('did not validate_toaster_message')
            print('did not validate_toaster_message')
            take_screenshot(driver, 'validate_toaster_message')
            raise err
