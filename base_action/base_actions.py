import logging
import time
from selenium import webdriver
from selenium.common.exceptions import *

from reali_web.base_action import base_actions_data
from reali_web.consumer_pages.sign.sign_in import sign_in_page
from reali_web.consumer_pages.buy.homes import homes_page

ba = base_actions_data
si = sign_in_page.SignInPage
hp = homes_page.HomesPage


class BaseFunctions:

    @staticmethod
    def base_navigation(driver: webdriver, url: str):
        try:
            driver.get(url)
            logging.info('navigation accrued')
            print(f'navigation accrued to {url}')
        except WebDriverException as err:
            logging.error('navigation did not accrued')
            print(f'navigation did not accrued to {url}')
            raise err

    @staticmethod
    def base_login(driver: webdriver, url: str, email: str, password: str):
        try:
            BaseFunctions.base_navigation(driver, url)
            hp.validate_navigation_to_homes_primary_page(driver)
            hp.click_on_sign_in(driver)
            assert si.validate_in_sign_in_page(driver)
            si.send_keys_to_email(driver, email)
            si.send_keys_to_password(driver, password)
            si.click_on_sign_in_button_in_sign_in_page(driver)
            assert hp.validate_navigation_to_homes_primary_page(driver)
            logging.info('login was successful')
            print('login was successful')
            return True
        except (AssertionError, NoSuchFrameException, ElementClickInterceptedException, NoSuchElementException) as err:
            logging.error('login was not init successfully')
            print('login was not init successfully')
            raise err

    @staticmethod
    def tear_down(driver: webdriver):
        try:
            driver.quit()
            time.sleep(5)
            logging.info('closed the chrome instance')
            print('closed the chrome instance')
        except WebDriverException as err:
            logging.error('did not managed to close the chrome session')
            print('did not managed to close the chrome session')
            raise err

    @staticmethod
    def handle_to_current_window(driver: webdriver):
        try:
            window_handle = driver.current_window_handle
            logging.info('got handle_to_current_window')
            print('got handle_to_current_window')
            return window_handle
        except NoSuchFrameException as err:
            logging.error('did not get handle_to_current_window')
            print('did not get handle_to_current_window')
            raise err

    @staticmethod
    def get_windows_handles(driver: webdriver):
        try:
            time.sleep(3)
            windows_list = driver.window_handles
            logging.info('got all different windows handles')
            print('got all different windows handles')
            return windows_list
        except NoSuchFrameException as err:
            logging.error('did not get all different windows handles')
            print('did not get all different windows handles')
            raise err

    @staticmethod
    def switch_to_window(driver, handle):
        try:
            time.sleep(5)
            driver.switch_to.window(handle)
            logging.info('switch_to new window')
            print('switch_to new window')
        except InvalidSwitchToTargetException as err:
            logging.error('did not managed to switch_to new window')
            print('did not managed to switch_to new window')
            raise err
