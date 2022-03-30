import logging
from selenium import webdriver
from selenium.common.exceptions import *
from reali_web.wait import wait_options
from reali_web.base_action import base_actions
from reali_web.conftest import take_screenshot

wf = wait_options.wait_functions
ba = base_actions.BaseFunctions


class RefreshFunctions:

    @staticmethod
    def refresh_page(driver: webdriver, element_to_wait: str):
        try:
            driver.refresh()
            wf.wait_for_element(driver, element_to_wait)
            logging.info('page was refreshed')
            print('page was refreshed')
        except WebDriverException as err:
            logging.error('Error in refreshing the page')
            print('Error in refreshing the page')
            take_screenshot(driver, 'refresh_page')
            raise err
