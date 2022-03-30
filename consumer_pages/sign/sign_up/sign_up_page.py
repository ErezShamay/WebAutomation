import logging
from selenium import webdriver
from selenium.common.exceptions import *

from reali_web.conftest import take_screenshot
from reali_web.wait import wait_options
from reali_web.consumer_pages.sign.sign_up import time_line_page
from reali_web.consumer_pages.sign.sign_up import sign_up_page_locators

tl = time_line_page.TimeLinePage
w = wait_options.wait_functions
supl = sign_up_page_locators.SignUpPageLocators


class SignUpPage:
    @staticmethod
    def validate_in_sign_up_page(driver: webdriver):
        try:
            w.wait_for_element(driver, supl.ZERO_EMAIL_LOCATOR)
            driver.find_element(*supl.ZERO_EMAIL_LOCATOR)
            logging.info('in sign up page')
            print('in sign up page')
            return True
        except NoSuchElementException as err:
            try:
                driver.find_element(*supl.EMAIL_LOCATOR)
            except (NoSuchElementException, WebDriverException, ElementNotInteractableException):
                logging.error('not in sign up page')
                print('not in sign up page')
                take_screenshot(driver, 'validate_in_sign_up_page')
                raise err
            return True

    @staticmethod
    def send_keys_to_email(driver: webdriver, email: str):
        try:
            w.wait_for_element(driver, supl.ZERO_EMAIL_LOCATOR)
            element = driver.find_element(*supl.ZERO_EMAIL_LOCATOR)
            element.send_keys(email)
            logging.info('send_keys_to_email')
            print('send_keys_to_email')
        except (NoSuchElementException, WebDriverException, ElementNotInteractableException) as err:
            try:
                element = driver.find_element(*supl.EMAIL_LOCATOR)
                element.send_keys(email)
            except (NoSuchElementException, WebDriverException, ElementNotInteractableException):
                logging.error('did not send_keys_to_email')
                print('send_keys_to_email')
                take_screenshot(driver, 'send_keys_to_email')
                raise err
            return True

    @staticmethod
    def send_keys_to_password(driver: webdriver, password: str):
        try:
            element = driver.find_element(*supl.ZERO_PASSWORD_LOCATOR)
            element.send_keys(password)
            logging.info('send_keys_to_email')
            print('send_keys_to_email')
        except(NoSuchElementException, WebDriverException) as err:
            try:
                element = driver.find_element(*supl.PASSWORD_LOCATOR)
                element.send_keys(password)
            except(NoSuchElementException, WebDriverException):
                logging.error('did not send_keys_to_email')
                print('did not send_keys_to_email')
                take_screenshot(driver, 'send_keys_to_password')
                raise err
            return True

    @staticmethod
    def click_on_sign_up_button(driver: webdriver):
        try:
            element = driver.find_element(*supl.SIGN_UP_BUTTON)
            element.click()
            assert SignUpPage.validate_in_account_profile(driver)
            logging.info('click_on_sign_up_button')
            print('click_on_sign_up_button')
        except(AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_sign_up_button')
            print('did not click_on_sign_up_button')
            take_screenshot(driver, 'click_on_sign_up_button')
            raise err

    @staticmethod
    def validate_in_account_profile(driver: webdriver):
        try:
            w.wait_for_element(driver, supl.FIRST_NAME)
            driver.find_element(*supl.FIRST_NAME)
            logging.info('in_account_profile')
            print('in_account_profile')
            return True
        except NoSuchElementException as err:
            logging.error('is not in_account_profile')
            print('is not in_account_profile')
            take_screenshot(driver, 'validate_in_account_profile')
            raise err

    @staticmethod
    def send_keys_to_first_name(driver: webdriver, first_name: str):
        try:
            element = driver.find_element(*supl.FIRST_NAME)
            element.send_keys(first_name)
            logging.info('send_keys_to_first_name')
            print('send_keys_to_first_name')
        except(NoSuchElementException, WebDriverException) as err:
            logging.error('did not send_keys_to_first_name')
            print('did not send_keys_to_first_name')
            take_screenshot(driver, 'send_keys_to_first_name')
            raise err

    @staticmethod
    def send_keys_to_last_name(driver: webdriver, last_name: str):
        try:
            element = driver.find_element(*supl.LAST_NAME)
            element.send_keys(last_name)
            logging.info('send_keys_to_last_name')
            print('send_keys_to_last_name')
        except (NoSuchElementException, WebDriverException) as err:
            logging.error('did not send_keys_to_last_name')
            print('did not send_keys_to_last_name')
            take_screenshot(driver, 'send_keys_to_last_name')
            raise err

    @staticmethod
    def send_keys_to_phone_number(driver: webdriver, phone_number: str):
        try:
            element = driver.find_element(*supl.PHONE_NUMBER)
            element.send_keys(phone_number)
            logging.info('send_keys_to_phone_number')
            print('send_keys_to_phone_number')
        except (NoSuchElementException, WebDriverException) as err:
            logging.error('did not send_keys_to_phone_number')
            print('did not send_keys_to_phone_number')
            take_screenshot(driver, 'send_keys_to_last_name')
            raise err

    @staticmethod
    def click_on_continue_button(driver: webdriver):
        try:
            element = driver.find_element(*supl.CONTINUE_BUTTON)
            element.click()
            logging.info('click_on_continue_button')
            print('click_on_continue_button')
        except (NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_continue_button')
            print('did not click_on_continue_button')
            take_screenshot(driver, 'send_keys_to_last_name')
            raise err

    @staticmethod
    def validate_in_where(driver: webdriver):
        try:
            w.wait_for_element(driver, supl.CALIFORNIA)
            driver.find_element(*supl.CALIFORNIA)
            logging.info('in_where')
            print('in_where')
            return True
        except NoSuchElementException as err:
            logging.error('not in_where')
            print('not in_where')
            take_screenshot(driver, 'send_keys_to_last_name')
            raise err

    @staticmethod
    def select_where_option(driver: webdriver, option: str):
        if option == 'california':
            SignUpPage.click_on_california_option(driver)
        elif option == 'out side california':
            SignUpPage.click_on_out_side_california_option(driver)
        else:
            SignUpPage.click_on_california_option(driver)

    @staticmethod
    def click_on_california_option(driver: webdriver):
        try:
            element = driver.find_element(*supl.CALIFORNIA)
            element.click()
            assert tl.validate_in_time_line_page(driver)
            logging.info('click_on_california_option')
            print('click_on_california_option')
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_california_option')
            print('did not click_on_california_option')
            take_screenshot(driver, 'click_on_california_option')
            raise err

    @staticmethod
    def click_on_out_side_california_option(driver: webdriver):
        try:
            element = driver.find_element(*supl.OUTSIDE_CALIFORNIA)
            element.click()
            assert tl.validate_in_time_line_page(driver)
            logging.info('click_on_california_option')
            print('click_on_california_option')
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_california_option')
            print('did not click_on_california_option')
            take_screenshot(driver, 'click_on_out_side_california_option')
            raise err

    @staticmethod
    def click_on_sign_in_button(driver: webdriver):
        try:
            element = driver.find_element(*supl.SIGN_IN_LINK)
            element.click()
            logging.info('click_on_sign_in_button')
            print('click_on_sign_in_button')
        except (NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_sign_in_button')
            print('did not click_on_sign_in_button')
            take_screenshot(driver, 'click_on_sign_in_button')
            raise err
