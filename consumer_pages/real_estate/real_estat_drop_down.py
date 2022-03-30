import logging
from selenium import webdriver
from selenium.common.exceptions import *

from reali_web.conftest import take_screenshot
from reali_web.wait import wait_options
from reali_web.consumer_pages.real_estate import real_estat_drop_down_locators

wf = wait_options.wait_functions
re = real_estat_drop_down_locators.RealEstateDropDownLocators


class RealEstateDropDown:
    @staticmethod
    def validate_real_estate_drop_down_open(driver: webdriver):
        try:
            wf.wait_for_element(driver, re.BUY)
            driver.find_element(*re.BUY)
            logging.info('validate_mortgage_drop_down_open')
            print('validate_mortgage_drop_down_open')
            return True
        except NoSuchElementException as err:
            logging.error('did not validate_mortgage_drop_down_open')
            print('did not validate_mortgage_drop_down_open')
            take_screenshot(driver, 'validate_real_estate_drop_down_open')
            raise err

    @staticmethod
    def click_on_buy_option(driver: webdriver):
        try:
            element = driver.find_element(*re.BUY)
            element.click()
            logging.info('click_on_buy_option')
            print('click_on_buy_option')
            assert RealEstateDropDown.validate_real_estate_drop_down_open(driver)
            return True
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_buy_option')
            print('did not click_on_buy_option')
            take_screenshot(driver, 'click_on_buy_option')
            raise err

    @staticmethod
    def click_on_sell_option(driver: webdriver):
        try:
            element = driver.find_element(*re.SELL)
            element.click()
            logging.info('click_on_sell_option')
            print('click_on_sell_option')
            assert RealEstateDropDown.validate_real_estate_drop_down_open(driver)
            return True
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_sell_option')
            print('did not click_on_sell_option')
            take_screenshot(driver, 'click_on_sell_option')
            raise err
