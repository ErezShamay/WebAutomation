import logging
import time
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains

from reali_web.conftest import take_screenshot
from reali_web.wait import wait_options
from reali_web.consumer_pages.morgtage.purchase import purchase_main_page_locators
from reali_web.consumer_pages.real_estate import real_estat_drop_down

wf = wait_options.wait_functions
pp = purchase_main_page_locators.PurchaseMainPageLocators
re = real_estat_drop_down.RealEstateDropDown


class PurchaseMainPage:
    @staticmethod
    def click_on_purchase_in_mortgage_drop_down(driver: webdriver):
        try:
            wf.wait_for_element(driver, pp.PURCHASE_OPTION)
            element = driver.find_element(*pp.PURCHASE_OPTION)
            element.click()
            logging.info('click_on_purchase_in_mortgage_drop_down')
            print('click_on_purchase_in_mortgage_drop_down')
            assert PurchaseMainPage.validate_navigated_to_purchase_main_page(driver)
            return True
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_purchase_in_mortgage_drop_down')
            print('did not click_on_purchase_in_mortgage_drop_down')
            take_screenshot(driver, 'click_on_purchase_in_mortgage_drop_down')
            raise err

    @staticmethod
    def validate_navigated_to_purchase_main_page(driver: webdriver):
        try:
            time.sleep(10)
            driver.find_element(*pp.ZIP_CODE)
            logging.info('validate_navigated_to_purchase_main_page')
            print('validate_navigated_to_purchase_main_page')
            return True
        except NoSuchElementException as err:
            logging.error('did not validate_navigated_to_purchase_main_page')
            print('did not validate_navigated_to_purchase_main_page')
            take_screenshot(driver, 'validate_navigated_to_purchase_main_page')
            raise err

    @staticmethod
    def move_to_on_real_estate_tab(driver: webdriver):
        try:
            time.sleep(5)
            element = driver.find_element(*pp.REAL_ESTATE)
            action = ActionChains(driver)
            action.move_to_element(element).perform()
            logging.info('move_to_on_mortgage_tab')
            print('move_to_on_mortgage_tab')
            assert re.validate_real_estate_drop_down_open(driver)
            return True
        except (AssertionError, WebDriverException) as err:
            logging.error('did not move_to_on_mortgage_tab')
            print('did not move_to_on_mortgage_tab')
            take_screenshot(driver, 'move_to_on_real_estate_tab')
            raise err
