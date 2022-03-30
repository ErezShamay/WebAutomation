import logging
from selenium import webdriver
from selenium.common.exceptions import *

from reali_web.conftest import take_screenshot
from reali_web.wait import wait_options
from reali_web.consumer_pages.sign.sign_up import verification_page
from reali_web.consumer_pages.sign.sign_up import time_line_page_locators

v = verification_page.VerificationPage
w = wait_options.wait_functions
tlpl = time_line_page_locators.TimeLinePageLocators


class TimeLinePage:
    @staticmethod
    def validate_in_time_line_page(driver: webdriver):
        try:
            w.wait_for_element(driver, tlpl.OPTION_1)
            driver.find_element(*tlpl.OPTION_1)
            logging.info('in time_line_page')
            print('in time_line_page')
            return True
        except NoSuchElementException as err:
            logging.error('not in time_line_page')
            print('not in time_line_page')
            take_screenshot(driver, 'validate_in_time_line_page')
            raise err

    @staticmethod
    def select_time_line_option(driver: webdriver, option: str):
        if option == '0-3':
            TimeLinePage.click_on_0_3_option(driver)
        elif option == '3-6':
            TimeLinePage.click_on_3_6_option(driver)
        elif option == '6+':
            TimeLinePage.click_on_6_plus_option(driver)
        else:
            TimeLinePage.click_on_0_3_option(driver)

    @staticmethod
    def click_on_0_3_option(driver: webdriver):
        try:
            element = driver.find_element(*tlpl.OPTION_1)
            element.click()
            assert v.validate_in_verification_page(driver)
            logging.info('click_on_0_3_option')
            print('click_on_0_3_option')
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_0_3_option')
            print('did not click_on_0_3_option')
            take_screenshot(driver, 'click_on_0_3_option')
            raise err

    @staticmethod
    def click_on_3_6_option(driver: webdriver):
        try:
            element = driver.find_element(*tlpl.OPTION_2)
            element.click()
            assert v.validate_in_verification_page(driver)
            logging.info('click_on_3_6_option')
            print('click_on_3_6_option')
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_3_6_option')
            print('did not click_on_3_6_option')
            take_screenshot(driver, 'click_on_3_6_option')
            raise err

    @staticmethod
    def click_on_6_plus_option(driver: webdriver):
        try:
            element = driver.find_element(*tlpl.OPTION_3)
            element.click()
            assert v.validate_in_verification_page(driver)
            logging.info('click_on_6_plus_option')
            print('click_on_6_plus_option')
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_6_plus_option')
            print('did not click_on_6_plus_option')
            take_screenshot(driver, 'click_on_6_plus_option')
            raise err
