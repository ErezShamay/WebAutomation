import logging
from selenium import webdriver
from selenium.common.exceptions import *

from reali_web.conftest import take_screenshot
from reali_web.wait import wait_options
from reali_web.consumer_pages.morgtage import mortgage_drop_down_locators

wf = wait_options.wait_functions
mddl = mortgage_drop_down_locators.MortgageDropDownLocators


class MortgageDropDown:
    @staticmethod
    def validate_mortgage_drop_down_open(driver: webdriver):
        try:
            wf.wait_for_element(driver, mddl.MORTGAGE_DROP_DOWN_MENU)
            driver.find_element(*mddl.MORTGAGE_DROP_DOWN_MENU)
            logging.info('validate_mortgage_drop_down_open')
            print('validate_mortgage_drop_down_open')
            return True
        except NoSuchElementException as err:
            logging.error('did not validate_mortgage_drop_down_open')
            print('did not validate_mortgage_drop_down_open')
            take_screenshot(driver, 'validate_mortgage_drop_down_open')
            raise err
