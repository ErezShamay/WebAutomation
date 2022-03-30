import logging
import time

from selenium import webdriver
from selenium.common.exceptions import *

from reali_web.conftest import take_screenshot
from reali_web.echo_pages.login_page import login_page_locators
from reali_web.echo_pages.main_page import main_page
from reali_web.wait import wait_options
from reali_web.base_action import base_actions
from selenium.webdriver.common.action_chains import ActionChains

lpl = login_page_locators.LoginPageLocators
ba = base_actions.BaseFunctions
mp = main_page.MainPage
wf = wait_options.wait_functions


class LoginPage:
    @staticmethod
    def validate_navigation_to_login_page(driver: webdriver):
        try:
            driver.find_element(*lpl.GOOGLE_SIGN_IN_BUTTON)
            logging.info('validate_navigation_to_home_page')
            print('validate_navigation_to_home_page')
            return True
        except NoSuchElementException as err:
            logging.error('did not validate_navigation_to_home_page')
            print('did not validate_navigation_to_home_page')
            take_screenshot(driver, 'validate_navigation_to_login_page')
            raise err

    @staticmethod
    def click_on_sign_in_with_google_button(driver: webdriver):
        try:
            element = driver.find_element(*lpl.GOOGLE_SIGN_IN_BUTTON)
            element.click()
            logging.info('click_on_sign_in_with_google_button')
            print('click_on_sign_in_with_google_button')
        except(NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_sign_in_with_google_button')
            print('did not click_on_sign_in_with_google_button')
            take_screenshot(driver, 'click_on_sign_in_with_google_button')
            raise err

    @staticmethod
    def click_on_google_user(driver: webdriver):
        try:
            element = driver.find_element(*lpl.GOOGLE_USER)
            element.click()
            logging.info('click_on_google_user')
            print('click_on_google_user')
        except (NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_google_user')
            print('did not click_on_google_user')
            take_screenshot(driver, 'click_on_google_user')
            raise err

    @staticmethod
    def do_login(driver: webdriver, email: str, password: str):
        try:
            current_window = ba.handle_to_current_window(driver)
            LoginPage.click_on_sign_in_with_google_button(driver)
            list_of_windows_handles = ba.get_windows_handles(driver)
            ba.switch_to_window(driver, list_of_windows_handles[1])
            LoginPage.send_keys_to_email(driver, email)
            LoginPage.click_on_email_next_button(driver)
            LoginPage.send_keys_to_password(driver, password)
            LoginPage.click_on_password_next_button(driver)
            ba.switch_to_window(driver, current_window)
            assert mp.validate_navigation_to_main_page(driver)
            logging.info('login is done')
            print('login is done')
            return True
        except (WebDriverException, AssertionError) as err:
            logging.error('error in login')
            print('error in login')
            take_screenshot(driver, 'do_login')
            raise err

    @staticmethod
    def send_keys_to_email(driver: webdriver, email: str):
        try:
            action = ActionChains(driver)
            wf.wait_for_element(driver, lpl.EMAIL_FIELD)
            driver.find_element(*lpl.EMAIL_FIELD)
            action.send_keys(email)
            action.perform()
            logging.info('send_keys_to_email')
            print('send_keys_to_email')
        except (NoSuchElementException, WebDriverException) as err:
            logging.error('did not send_keys_to_email')
            print('did not send_keys_to_email')
            take_screenshot(driver, 'send_keys_to_email')
            raise err

    @staticmethod
    def click_on_email_next_button(driver: webdriver):
        try:
            element = driver.find_element(*lpl.EMAIL_NEXT_BUTTON)
            element.click()
            logging.info('click_on_next_button')
            print('click_on_next_button')
        except (NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_next_button')
            print('did not click_on_next_button')
            take_screenshot(driver, 'click_on_email_next_button')
            raise err

    @staticmethod
    def send_keys_to_password(driver: webdriver, password: str):
        try:
            action = ActionChains(driver)
            time.sleep(5)
            driver.find_element(*lpl.PASSWORD_FIELD)
            action.send_keys(password)
            action.perform()
            logging.info('send_keys_to_password')
            print('send_keys_to_password')
        except(NoSuchElementException, WebDriverException) as err:
            logging.error('did not send_keys_to_password')
            print('did not send_keys_to_password')
            take_screenshot(driver, 'send_keys_to_password')
            raise err

    @staticmethod
    def click_on_password_next_button(driver: webdriver):
        try:
            wf.wait_for_element(driver, lpl.PASSWORD_NEXT_BUTTON)
            element = driver.find_element(*lpl.PASSWORD_NEXT_BUTTON)
            element.click()
            logging.info('click_on_next_button')
            print('click_on_next_button')
        except (NoSuchElementException, ElementClickInterceptedException, TimeoutException) as err:
            logging.error('did not click_on_next_button')
            print('did not click_on_next_button')
            take_screenshot(driver, 'click_on_password_next_button')
            raise err

    @staticmethod
    def do_quick_login(driver: webdriver, token: str):
        try:
            driver.execute_script(f"window.localStorage.setItem('auth_token', '{token}')")
        except (WebDriverException, AssertionError) as err:
            logging.error('error in login')
            print('error in login')
            take_screenshot(driver, 'do_login')
            raise err
