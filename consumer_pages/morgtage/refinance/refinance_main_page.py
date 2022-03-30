import logging
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import *

from reali_web.conftest import take_screenshot
from reali_web.wait import wait_options
from reali_web.consumer_pages.morgtage.refinance import refinance_main_page_locators
from reali_web.consumer_pages.real_estate import real_estat_drop_down

wf = wait_options.wait_functions
rp = refinance_main_page_locators.RefinanceMainPageLocators
re = real_estat_drop_down.RealEstateDropDown


class RefinanceMainPage:
    @staticmethod
    def click_on_refinance_in_mortgage_drop_down(driver: webdriver):
        try:
            element = driver.find_element(*rp.REFINANCE_OPTION)
            element.click()
            logging.info('click_on_refinance_in_mortgage_drop_down')
            print('click_on_refinance_in_mortgage_drop_down')
            assert RefinanceMainPage.validate_navigated_to_refinance_main_page(driver)
            return True
        except(AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_refinance_in_mortgage_drop_down')
            print('did not click_on_refinance_in_mortgage_drop_down')
            take_screenshot(driver, 'click_on_refinance_in_mortgage_drop_down')
            raise err

    @staticmethod
    def validate_navigated_to_refinance_main_page(driver: webdriver):
        try:
            wf.wait_for_element(driver, rp.ZIP_CODE)
            driver.find_element(*rp.ZIP_CODE)
            logging.info('validate_navigated_to_refinance_main_page')
            print('validate_navigated_to_refinance_main_page')
            return True
        except NoSuchElementException as err:
            logging.error('did not validate_navigated_to_refinance_main_page')
            print('did not validate_navigated_to_refinance_main_page')
            take_screenshot(driver, 'validate_navigated_to_refinance_main_page')
            raise err

    @staticmethod
    def move_to_on_real_estate_tab(driver: webdriver):
        try:
            time.sleep(10)
            element = driver.find_element(*rp.REAL_ESTATE)
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

    @staticmethod
    def validate_user_icon(driver: webdriver):
        try:
            wf.wait_for_element(driver, rp.USER_ICON)
            driver.find_element(*rp.USER_ICON)
            logging.info('validate_user_icon')
            print('validate_user_icon')
            return True
        except NoSuchElementException as err:
            logging.error('did not validate_user_icon')
            print('did not validate_user_icon')
            take_screenshot(driver, 'validate_user_icon')
            raise err 
