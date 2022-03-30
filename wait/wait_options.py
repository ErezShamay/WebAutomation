import logging
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from reali_web.conftest import take_screenshot


class wait_functions:
    @staticmethod
    def wait_for_element(driver: webdriver, element):
        try:
            WebDriverWait(driver, 20).until(EC.presence_of_element_located(element))
        except (NoSuchElementException, TimeoutException, ElementNotVisibleException, NoSuchAttributeException) as err:
            logging.error('waiting take too long')
            take_screenshot(driver, 'validate_listings_as_designed')

    @staticmethod
    def wait_for_element_to_be_click(driver: webdriver, element):
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(element))
        except TimeoutException as err:
            logging.error('waiting take too long')
            print('waiting take too long')
