import logging
import time

from selenium import webdriver
from selenium.common.exceptions import *

from reali_web.conftest import take_screenshot
from reali_web.consumer_pages.sign.sign_up import sign_up_page
from reali_web.wait import wait_options
from reali_web.consumer_pages.sign.sign_in import sign_in_page_locators

su = sign_up_page.SignUpPage
w = wait_options.wait_functions
sipl = sign_in_page_locators.SignInPageLocators


class SignInPage:
    @staticmethod
    def validate_in_sign_in_page(driver: webdriver):
        try:
            w.wait_for_element(driver, sipl.FORGOT_PASSWORD)
            driver.find_element(*sipl.FORGOT_PASSWORD)
            logging.info('in sign in page')
            print('in sign in page')
            return True
        except NoSuchElementException as err:
            logging.error('not in sign in page')
            print('not in sign in page')
            take_screenshot(driver, 'validate_in_sign_in_page')
            raise err

    @staticmethod
    def validate_in_general_sign_in_page(driver: webdriver):
        try:
            w.wait_for_element(driver, sipl.EMAIL_LOCATOR)
            driver.find_element(*sipl.EMAIL_LOCATOR)
            logging.info('in sign in page')
            print('in sign in page')
            return True
        except NoSuchElementException as err:
            logging.error('not in sign in page')
            print('not in sign in page')
            take_screenshot(driver, 'validate_in_sign_in_page')
            raise err

    @staticmethod
    def click_on_sign_up(driver: webdriver):
        try:
            time.sleep(3)
            w.wait_for_element(driver, sipl.SIGN_UP)
            element = driver.find_element(*sipl.SIGN_UP)
            element.click()
            assert su.validate_in_sign_up_page(driver)
            logging.info('clicked on sign up')
            print('clicked on sign up')
            return True
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not clicked on sign up')
            print('did not clicked on sign up')
            take_screenshot(driver, 'click_on_sign_up')
            raise err

    @staticmethod
    def send_keys_to_email(driver: webdriver, email: str):
        try:
            element = driver.find_element(*sipl.EMAIL_LOCATOR)
            element.send_keys(email)
            logging.info('send_keys_to_email')
            print('send_keys_to_email')
        except (NoSuchElementException, WebDriverException) as err:
            logging.error('did not send_keys_to_email')
            print('did not send_keys_to_email')
            take_screenshot(driver, 'send_keys_to_email')
            raise err

    @staticmethod
    def send_keys_to_password(driver: webdriver, password: str):
        try:
            element = driver.find_element(*sipl.PASSWORD_LOCATOR)
            element.send_keys(password)
            logging.info('send_keys_to_password')
            print('send_keys_to_password')
        except (NoSuchElementException, WebDriverException) as err:
            logging.error('did not send_keys_to_password')
            print('did not send_keys_to_password')
            take_screenshot(driver, 'send_keys_to_password')
            raise err

    @staticmethod
    def send_keys_to_general_email(driver: webdriver, email: str):
        try:
            element = driver.find_element(*sipl.GENERAL_EMAIL_LOCATOR)
            element.send_keys(email)
            logging.info('send_keys_to_general_email')
            print('send_keys_to_general_email')
        except (NoSuchElementException, WebDriverException) as err:
            logging.error('did not send_keys_to_general_email')
            print('did not send_keys_to_general_email')
            take_screenshot(driver, 'send_keys_to_general_email')
            raise err

    @staticmethod
    def send_keys_to_general_password(driver: webdriver, password: str):
        try:
            element = driver.find_element(*sipl.GENERAL_PASSWORD_LOCATOR)
            element.send_keys(password)
            logging.info('send_keys_to_general_password')
            print('send_keys_to_general_password')
        except (NoSuchElementException, WebDriverException) as err:
            logging.error('did not send_keys_to_general_password')
            print('did not send_keys_to_general_password')
            take_screenshot(driver, 'send_keys_to_general_password')
            raise err

    @staticmethod
    def click_on_sign_in_button_in_sign_in_page(driver: webdriver):
        try:
            w.wait_for_element(driver, sipl.SIGN_IN_BUTTON)
            element = driver.find_element(*sipl.SIGN_IN_BUTTON)
            element.click()
            logging.info('click_on_sign_button')
            print('click_on_sign_button')
        except (NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_sign_button')
            print('did not click_on_sign_button')
            take_screenshot(driver, 'click_on_sign_in_button_in_sign_in_page')
            raise err

    @staticmethod
    def click_on_sign_in_button_in_header(driver: webdriver):
        try:
            driver.find_element(*sipl.HEADER_SIGN_IN_BUTTON).click()
            SignInPage.validate_in_sign_in_page(driver)
            logging.info('click_on_sign_button')
            print('click_on_sign_button')
        except (NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_sign_button')
            print('did not click_on_sign_button')
            take_screenshot(driver, 'click_on_sign_in_button_in_header')
            raise err

    @staticmethod
    def do_login(driver: webdriver, email: str, password: str):
        try:
            SignInPage.click_on_sign_in_button_in_header(driver)
            SignInPage.send_keys_to_general_email(driver, email)
            SignInPage.send_keys_to_general_password(driver, password)
            SignInPage.click_on_sign_in_button_in_sign_in_page(driver)
            SignInPage.validate_login_was_made(driver)
            logging.info('login was made')
            print('login was made')
            return True
        except (NoSuchElementException, ElementClickInterceptedException, WebDriverException) as err:
            logging.error('error in login')
            print('error in login')
            take_screenshot(driver, 'do_login')
            raise err

    @staticmethod
    def validate_login_was_made(driver: webdriver):
        try:
            time.sleep(5)
            w.wait_for_element(driver, sipl.USER_ICON)
            driver.find_element(*sipl.USER_ICON)
            logging.info('validate_login_was_made')
            print('validate_login_was_made')
            return True
        except (TimeoutException, NoSuchElementException) as err:
            logging.error('did not validate_login_was_made')
            print('did not validate_login_was_made')
            take_screenshot(driver, 'validate_login_was_made')
            raise err
