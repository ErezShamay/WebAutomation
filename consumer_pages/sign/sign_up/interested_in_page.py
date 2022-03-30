import logging
from selenium import webdriver
from selenium.common.exceptions import *

from reali_web.conftest import take_screenshot
from reali_web.wait import wait_options
from reali_web.consumer_pages.sign.sign_up import sign_up_page
from reali_web.consumer_pages.sign.sign_up import interested_in_page_locators

su = sign_up_page.SignUpPage
w = wait_options.wait_functions
iipl = interested_in_page_locators.InterestedInPageLocators


class InterestedInPage:
    @staticmethod
    def validate_in_interested_in(driver: webdriver):
        try:
            w.wait_for_element(driver, iipl.BUYING)
            driver.find_element(*iipl.BUYING)
            logging.info('in_interested_in')
            print('in_interested_in')
            return True
        except NoSuchElementException as err:
            logging.error('is not in_interested_in')
            print('is not in_interested_in')
            take_screenshot(driver, 'validate_in_interested_in')
            raise err 

    @staticmethod
    def select_interested_in_option(driver: webdriver, option: str):
        if option == 'buying':
            InterestedInPage.click_on_buying(driver)
        elif option == 'selling':
            InterestedInPage.click_on_selling(driver)
        elif option == 'buying and selling':
            InterestedInPage.click_on_buying_and_selling(driver)
        else:
            InterestedInPage.click_on_buying(driver)

    @staticmethod
    def click_on_buying(driver: webdriver):
        try:
            element = driver.find_element(*iipl.BUYING)
            element.click()
            assert su.validate_in_where(driver)
            logging.info('click_on_buying')
            print('click_on_buying')
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_buying')
            print('did not click_on_buying')
            take_screenshot(driver, 'click_on_buying')
            raise err

    @staticmethod
    def click_on_selling(driver: webdriver):
        try:
            element = driver.find_element(*iipl.SELLING)
            element.click()
            assert su.validate_in_where(driver)
            logging.info('click_on_selling')
            print('click_on_selling')
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_selling')
            print('did not click_on_selling')
            take_screenshot(driver, 'click_on_selling')
            raise err

    @staticmethod
    def click_on_buying_and_selling(driver: webdriver):
        try:
            element = driver.find_element(*iipl.BUYING_AND_SELLING)
            element.click()
            assert su.validate_in_where(driver)
            logging.info('click_on_buying_and_selling')
            print('click_on_buying_and_selling')
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_buying_and_selling')
            print('did not click_on_buying_and_selling')
            take_screenshot(driver, 'click_on_buying_and_selling')
            raise err
