import logging
from selenium import webdriver
from selenium.common.exceptions import *

from reali_web.conftest import take_screenshot
from reali_web.consumer_pages.sell import sell_page_locators
from reali_web.wait import wait_options
from reali_web.consumer_pages.sign.sign_up import sign_up_page
from reali_web.consumer_pages.sign.sign_in import sign_in_page

spl = sell_page_locators.SellPageLocators
wf = wait_options.wait_functions
sup = sign_up_page.SignUpPage
sip = sign_in_page.SignInPage


class SellPage:

    @staticmethod
    def validate_navigation_to_sell_page(driver: webdriver):
        try:
            wf.wait_for_element(driver, spl.VALIDATE_NAVIGATION)
            driver.find_element(*spl.VALIDATE_NAVIGATION)
            logging.info('validate_navigation_to_sell_page')
            print('validate_navigation_to_sell_page')
            return True
        except NoSuchElementException as err:
            logging.error('did not validate_navigation_to_sell_page')
            print('did not validate_navigation_to_sell_page')
            take_screenshot(driver, 'validate_navigation_to_sell_page')
            raise err 

    @staticmethod
    def click_on_sell_option(driver: webdriver):
        try:
            element = driver.find_element(*spl.SELL_OPTION)
            element.click()
            logging.info('click_on_sell_option')
            print('click_on_sell_option')
        except (NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_sell_option')
            print('did not click_on_sell_option')
            take_screenshot(driver, 'click_on_sell_option')
            raise err

    @staticmethod
    def click_on_get_started_button(driver: webdriver):
        try:
            wf.wait_for_element(driver, spl.GET_STARTED)
            element = driver.find_element(*spl.GET_STARTED)
            element.click()
            logging.info('click_on_get_started_button')
            print('click_on_get_started_button')
            assert SellPage.validate_navigation_to_home_valuation_page(driver)
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_get_started_button')
            print('did not click_on_get_started_button')
            take_screenshot(driver, 'click_on_get_started_button')
            raise err

    @staticmethod
    def validate_navigation_to_home_valuation_page(driver: webdriver):
        try:
            wf.wait_for_element(driver, spl.HOME_VALUATION)
            driver.find_element(*spl.HOME_VALUATION)
            logging.info('validate_navigation_to_home_valuation_page')
            print('validate_navigation_to_home_valuation_page')
            return True
        except NoSuchElementException as err:
            logging.error('did not validate_navigation_to_home_valuation_page')
            print('did not validate_navigation_to_home_valuation_page')
            take_screenshot(driver, 'validate_navigation_to_home_valuation_page')
            raise err

    @staticmethod
    def send_keys_to_search_address(driver: webdriver, sell_address: str):
        try:
            wf.wait_for_element(driver, spl.SEARCH_ADDRESS)
            element = driver.find_element(*spl.SEARCH_ADDRESS)
            element.send_keys(sell_address)
            logging.info('send_keys_to_search_address')
            print('send_keys_to_search_address')
        except (NoSuchElementException, WebDriverException) as err:
            logging.error('did not send_keys_to_search_address')
            print('did not send_keys_to_search_address')
            take_screenshot(driver, 'send_keys_to_search_address')
            raise err

    @staticmethod
    def select_address_from_search_result(driver: webdriver):
        try:
            wf.wait_for_element(driver, spl.SELECT_SEARCH_VALUE)
            element = driver.find_element(*spl.SELECT_SEARCH_VALUE)
            element.click()
            logging.info('select_address_from_search_result')
            print('select_address_from_search_result')
        except (NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not select_address_from_search_result')
            print('did not select_address_from_search_result')
            raise err

    @staticmethod
    def click_on_request_home_valuation(driver: webdriver):
        try:
            wf.wait_for_element(driver, spl.REQUEST_HOME_VALUATION_BUTTON)
            element = driver.find_element(*spl.REQUEST_HOME_VALUATION_BUTTON)
            element.click()
            logging.info('click_on_request_home_valuation')
            print('click_on_request_home_valuation')
            assert sup.validate_in_sign_up_page(driver)
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_request_home_valuation')
            print('did not click_on_request_home_valuation')
            take_screenshot(driver, 'click_on_request_home_valuation')
            raise err

    @staticmethod
    def validate_congrats_message(driver: webdriver):
        try:
            wf.wait_for_element(driver, spl.CONGRATS_MESSAGE)
            driver.find_element(*spl.CONGRATS_MESSAGE)
            logging.info('validate_congrats_message')
            print('validate_congrats_message')
            return True
        except NoSuchElementException as err:
            logging.error('did not validate_congrats_message')
            print('did not validate_congrats_message')
            take_screenshot(driver, 'validate_congrats_message')
            raise err

    @staticmethod
    def validate_request_sent(driver: webdriver):
        try:
            SellPage.validate_navigation_to_sell_page(driver)
            SellPage.click_on_sell_option(driver)
            SellPage.click_on_get_started_button(driver)
            SellPage.validate_congrats_message(driver)
            logging.info('validate_request_sent')
            print('validate_request_sent')
            return True
        except(NoSuchElementException, WebDriverException, ElementClickInterceptedException) as err:
            logging.error('did not validate_request_sent')
            print('did not validate_request_sent')
            take_screenshot(driver, 'validate_request_sent')
            raise err
