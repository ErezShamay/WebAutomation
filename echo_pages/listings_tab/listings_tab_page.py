import logging
from selenium import webdriver
from selenium.common.exceptions import *

from reali_web.conftest import take_screenshot
from reali_web.wait import wait_options
from reali_web.echo_pages.listings_tab import listings_tab_page_locators
from reali_web.base_action import base_actions

wf = wait_options.wait_functions
ltpl = listings_tab_page_locators.ListingsTabPageLocators
ba = base_actions.BaseFunctions


class ListingsTabPage:
    @staticmethod
    def click_on_listings_tab(driver: webdriver):
        try:
            element = driver.find_element(ltpl.LISTINGS_TAB)
            element.click()
            logging.info('click_on_listings_tab')
            print('click_on_listings_tab')
            assert ListingsTabPage.validate_navigation_to_listings_page(driver)
            return True
        except(NoSuchElementException, ElementClickInterceptedException, AssertionError) as err:
            logging.error('did not click_on_listings_tab')
            print('did not click_on_listings_tab')
            take_screenshot(driver, 'click_on_listings_tab')
            raise err

    @staticmethod
    def validate_navigation_to_listings_page(driver: webdriver):
        try:
            wf.wait_for_element(driver, ltpl.LISTINGS_TABLE)
            driver.find_element(ltpl.LISTINGS_TABLE)
            logging.info('validate_navigation_to_listings_page')
            print('validate_navigation_to_listings_page')
            return True
        except NoSuchElementException as err:
            logging.error('did not validate_navigation_to_listings_page')
            print('did not validate_navigation_to_listings_page')
            take_screenshot(driver, 'validate_navigation_to_listings_page')
            raise err
