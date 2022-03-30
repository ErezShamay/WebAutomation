import logging
import time

from selenium import webdriver
from selenium.common.exceptions import *

from reali_web.conftest import take_screenshot
from reali_web.consumer_pages.buy.wishlist import wishlist_page_locators
from reali_web.wait import wait_options
from reali_web.consumer_pages.buy.homes import homes_page

wpl = wishlist_page_locators.WishListPageData
w = wait_options.wait_functions
hp = homes_page.HomesPage


class WishListPage:
    @staticmethod
    def navigate_to_wishlist(driver: webdriver):
        try:
            w.wait_for_element(driver, wpl.WISHLIST_TAB)
            element = driver.find_element(*wpl.WISHLIST_TAB)
            element.click()
            logging.info('navigate_to_wishlist')
            print('navigate_to_wishlist')
            assert WishListPage.validate_navigation_to_wishlist(driver)
            return True
        except (AssertionError, NoSuchElementException) as err:
            logging.error('did not navigate_to_wishlist')
            print('did not navigate_to_wishlist')
            take_screenshot(driver, 'validate_in_sign_in_page')
            raise err

    @staticmethod
    def validate_navigation_to_wishlist(driver: webdriver):
        try:
            url = driver.current_url
            assert 'wishlist' in url
            logging.info('validate_navigation_to_wishlist')
            print('validate_navigation_to_wishlist')
            return True
        except (AssertionError, NoSuchElementException) as err:
            logging.error('did not validate_navigation_to_wishlist')
            print('did not validate_navigation_to_wishlist')
            take_screenshot(driver, 'validate_navigation_to_wishlist')
            raise err

    @staticmethod
    def validate_items_in_wishlist(driver: webdriver):
        try:
            w.wait_for_element(driver, wpl.LISTING_INFO)
            driver.find_element(*wpl.LISTING_INFO)
            logging.info('validate_items_in_wishlist')
            print('validate_items_in_wishlist')
            return True
        except (AssertionError, NoSuchElementException) as err:
            logging.error('did not validate_items_in_wishlist')
            print('did not validate_items_in_wishlist')
            take_screenshot(driver, 'validate_items_in_wishlist')
            raise err

    @staticmethod
    def remove_favorite_and_clear_test_data(driver: webdriver):
        try:
            listing_cards = driver.find_elements(*wpl.LISTINGS_CARD)
            for listing_card in listing_cards:
                element = listing_card.find_element(*wpl.FAVORITE)
                element.click()
            time.sleep(5)
            logging.info('remove_favorite_and_clear_test_data')
            assert hp.click_on_homes_tab(driver)
            return True
        except (AssertionError, NoSuchElementException) as err:
            logging.error('did not remove_favorite_and_clear_test_data')
            print('did not remove_favorite_and_clear_test_data')
            take_screenshot(driver, 'remove_favorite_and_clear_test_data')
            raise err
