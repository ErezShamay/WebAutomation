import logging
import time

from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains

from reali_web.conftest import take_screenshot
from reali_web.consumer_pages.sign.sign_in import sign_in_page
from reali_web.wait import wait_options
from reali_web.consumer_pages.buy.homes import homes_page_locators
from reali_web.consumer_pages.sell import sell_page
from reali_web.consumer_pages.morgtage import mortgage_drop_down

si = sign_in_page.SignInPage
w = wait_options.wait_functions
hpl = homes_page_locators.HomesPageLocators
sp = sell_page.SellPage
mdd = mortgage_drop_down.MortgageDropDown


class HomesPage:

    @staticmethod
    def navigate_to_homes_primary_page(driver: webdriver):
        try:
            w.wait_for_element(driver, hpl.REALI_LOGO)
            driver.find_element().click(*hpl.REALI_LOGO)
            assert HomesPage.validate_navigation_to_homes_primary_page(driver)
            logging.info('click on reali logo')
            print('click on reali logo')
            return True
        except (NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not find element or did not managed to clicked on reali logo')
            print('navigate_to_homes_primary_page')
            take_screenshot(driver, 'navigate_to_homes_primary_page')
            raise err

    @staticmethod
    def validate_navigation_to_homes_primary_page(driver: webdriver):
        try:
            w.wait_for_element(driver, hpl.SELL_TAB)
            driver.find_element(*hpl.SELL_TAB)
            logging.info('validate navigation to homes primary page')
            print('validate navigation to homes primary page')
            return True
        except NoSuchElementException as err:
            logging.error('did not find element to validate navigation to homes primary page')
            print('did not find element to validate navigation to homes primary page')
            take_screenshot(driver, 'validate_navigation_to_homes_primary_page')
            raise err

    @staticmethod
    def click_on_sign_in(driver: webdriver):
        try:
            element = driver.find_element(*hpl.SIGN_IN)
            element.click()
            logging.info('clicked on sign in')
            print('clicked on sign in')
            assert si.validate_in_sign_in_page(driver)
            return True
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException,
                ElementNotInteractableException) as err:
            logging.error('did not clicked on sign in')
            print('did not clicked on sign in')
            take_screenshot(driver, 'click_on_sign_in')
            raise err

    @staticmethod
    def get_all_listings(driver: webdriver):
        try:
            time.sleep(5)
            listings_list = driver.find_elements(*hpl.LISTINGS)
            logging.info('get_all_listings')
            print('get_all_listings')
        except NoSuchElementException as err:
            logging.error('did not managed to get_all_listings')
            print('did not managed to get_all_listings')
            take_screenshot(driver, 'get_all_listings')
            raise err
        return listings_list

    @staticmethod
    def validate_listings_as_designed(driver: webdriver):
        actual_beds: str
        actual_baths: str
        actual_size: str
        actual_street: str
        actual_city: str
        actual_listing_summary_price: str
        try:
            listings_list = HomesPage.get_all_listings(driver)
            specific_listing = HomesPage.navigate_to_specific_listing(listings_list)
            driver.switch_to.window(driver.window_handles[1])
            w.wait_for_element(driver, hpl.WAIT)
            actual_street = driver.find_element(*hpl.ACTUAL_STREET)
            list_location = driver.find_elements(*hpl.ACTUAL_LOCATION)
            actual_beds = driver.find_element(*hpl.ACTUAL_BEDS)
            actual_baths = driver.find_element(*hpl.ACTUAL_BATHS)
            actual_size = driver.find_element(*hpl.ACTUAL_SIZE)
            actual_city = list_location[0]
            actual_listing_summary_price = driver.find_element(*hpl.ACTUAL_PRICE)
            assert actual_beds, specific_listing[0]
            assert actual_baths, specific_listing[1]
            assert actual_size, specific_listing[2]
            assert actual_street, specific_listing[3]
            assert actual_city, specific_listing[4]
            assert actual_listing_summary_price, specific_listing[5]
            logging.info('listings are as designed')
            print('listings are as designed')
            return True
        except (AssertionError, NoSuchElementException) as err:
            logging.error('listings as not as designed')
            print('listings as not as designed')
            take_screenshot(driver, 'validate_listings_as_designed')
            raise err

    @staticmethod
    def navigate_to_specific_listing(listings_list: list):
        try:
            time.sleep(5)
            listing = listings_list[1]
            street = listing.find_element(*hpl.STREET).text
            listing_summary_price = listing.find_element(*hpl.PRICE).text
            city = listing.find_element(*hpl.CITY).text
            beds = listing.find_element(*hpl.BEDS_AMOUNT).text
            baths = listing.find_element(*hpl.BATHS_AMOUNT).text
            size = listing.find_element(*hpl.SIZE_LISTING_SQUARE_FOOT).text
            listing.click()
            logging.info('navigate_to_specific_listing')
            print('navigate_to_specific_listing')
            time.sleep(5)
        except (NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not navigate_to_specific_listing')
            print('did not navigate_to_specific_listing')
            raise err
        return beds, baths, size, street, city, listing_summary_price

    @staticmethod
    def validate_search(driver: webdriver, address: str):
        try:
            assert HomesPage.validate_search_badge_in_header(driver)
            assert HomesPage.send_keys_to_search_badge_and_select_option(driver, address)
            logging.info('search functionality was validated correctly')
            print('search functionality was validated correctly')
            return True
        except (AssertionError, WebDriverException) as err:
            logging.error('search functionality was NOT validated')
            take_screenshot(driver, 'validate_search')
            print('search functionality was NOT validated')
            raise err

    @staticmethod
    def validate_search_badge_in_header(driver: webdriver):
        try:
            header = driver.find_element(*hpl.HEADER)
            text = header.text
            assert 'search' in text
            logging.info('search_badge_is in_header')
            print('search_badge_is in_header')
            return True
        except (AssertionError, NoSuchElementException, WebDriverException) as err:
            logging.error('search_badge_is NOT in_header')
            print('search_badge_is NOT in_header')
            take_screenshot(driver, 'validate_search_badge_in_header')
            raise err

    @staticmethod
    def send_keys_to_search_badge_and_select_option(driver: webdriver, address: str):
        try:
            element = driver.find_element(*hpl.SEARCH_INPUT_FIELD)
            element.send_keys(address)
            w.wait_for_element(driver, hpl.SEARCH_RESULT)
            element = driver.find_element(*hpl.SEARCH_RESULT)
            element.click()
            logging.info('send_keys_to_search_badge_and_select_option')
            print('send_keys_to_search_badge_and_select_option')
            return True
        except (NoSuchElementException, WebDriverException, ElementClickInterceptedException) as err:
            logging.error('did not managed to send_keys_to_search_badge_and_select_option')
            print('did not managed to send_keys_to_search_badge_and_select_option')
            take_screenshot(driver, 'send_keys_to_search_badge_and_select_option')
            raise err

    @staticmethod
    def validate_listings_filter_options(driver: webdriver):
        list_options = hpl.OPTION_LIST
        try:
            time.sleep(5)
            element = driver.find_element(*hpl.FEED_SORT_DROP_DOWN_MENU)
            element.click()
            w.wait_for_element(driver, hpl.MAT_OPTIONS)
            mat_options = driver.find_elements(*hpl.MAT_OPTIONS)
            for option in mat_options:
                assert option.text in list_options
            logging.info('listings_filter_options is as expected')
            print('listings_filter_options is as expected')
            assert HomesPage.validate_listing_sorting(driver)
            return True
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('listings_filter_options is NOT as expected')
            print('listings_filter_options is NOT as expected')
            take_screenshot(driver, 'validate_listings_filter_options')
            raise err

    @staticmethod
    def validate_listing_sorting(driver: webdriver):
        try:
            HomesPage.select_most_beds(driver)
            assert HomesPage.validate_is_max(driver)
            logging.info('sorting listing by attribute works correctly')
            print('sorting listing by attribute works correctly')
            return True
        except(AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('sorting listing by attribute does not work as expected')
            print('sorting listing by attribute does not work as expected')
            take_screenshot(driver, 'validate_listing_sorting')
            raise err

    @staticmethod
    def select_most_beds(driver: webdriver):
        try:
            driver.find_element(*hpl.BEDS_OPTION).click()
            w.wait_for_element(driver, hpl.LISTINGS_CARDS)
            logging.info('select_most_beds')
            print('select_most_beds')
            return True
        except(NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not select most beds')
            print('did not select most beds')
            take_screenshot(driver, 'select_most_beds')
            raise err

    @staticmethod
    def validate_is_max(driver: webdriver):
        mat_options = driver.find_elements(*hpl.LISTINGS_CARDS)
        option = mat_options[0]
        max_global_beds = option.find_element(*hpl.BEDS_AMOUNT).text
        for card in mat_options:
            candidate = card.find_element(*hpl.BEDS_AMOUNT).text
            if candidate > max_global_beds:
                logging.error('Error in sorting by max beds')
                print('Error in sorting by max beds')
                take_screenshot(driver, 'validate_is_max')
                return False
        return True

    @staticmethod
    def click_on_sell_tab(driver: webdriver):
        try:
            element = driver.find_element(*hpl.SELL_TAB)
            element.click()
            logging.info('clicked on_sell_tab')
            print('clicked on_sell_tab')
            sp.validate_navigation_to_sell_page(driver)
        except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException) as err:
            logging.error('did not find/clicked on_sell_tab')
            print('did not find/clicked on_sell_tab')
            take_screenshot(driver, 'click_on_sell_tab')
            raise err

    @staticmethod
    def move_to_on_mortgage_tab(driver: webdriver):
        try:
            w.wait_for_element(driver, hpl.MORTGAGE_TAB)
            element = driver.find_element(*hpl.MORTGAGE_TAB)
            action = ActionChains(driver)
            action.move_to_element(element).perform()
            logging.info('move_to_on_mortgage_tab')
            print('move_to_on_mortgage_tab')
            assert mdd.validate_mortgage_drop_down_open(driver)
            return True
        except (AssertionError, NoSuchElementException) as err:
            logging.error('did not move_to_on_mortgage_tab or assertion error')
            print('did not move_to_on_mortgage_tab or assertion error')
            take_screenshot(driver, 'move_to_on_mortgage_tab')
            raise err

    @staticmethod
    def validate_user_icon(driver: webdriver):
        try:
            w.wait_for_element(driver, hpl.USER_ICON)
            driver.find_element(*hpl.USER_ICON)
            logging.info('validate_user_icon is visible')
            print('validate_user_icon is visible')
            return True
        except NoSuchElementException as err:
            logging.error('user_icon is not visible/found')
            print('user_icon is not visible/found')
            take_screenshot(driver, 'validate_user_icon')
            raise err

    @staticmethod
    def click_on_buy_in_header_nav_bar(driver: webdriver):
        try:
            driver.find_element(*hpl.BUY_TAB).click()
            logging.info('click_on_buy_in_header_nav_bar')
            print('click_on_buy_in_header_nav_bar')
            assert HomesPage.validate_navigation_to_homes_primary_page(driver)
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not managed to click_on_buy_in_header_nav_bar')
            print('did not managed to click_on_buy_in_header_nav_bar')
            take_screenshot(driver, 'click_on_buy_in_header_nav_bar')
            raise err

    @staticmethod
    def click_on_sell_in_header_nav_bar(driver: webdriver):
        try:
            w.wait_for_element(driver, hpl.SELL_TAB)
            element = driver.find_element(*hpl.SELL_TAB)
            element.click()
            logging.info('click_on_sell_in_header_nav_bar')
            print('click_on_sell_in_header_nav_bar')
            assert sp.validate_navigation_to_sell_page(driver)
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not managed to click_on_sell_in_header_nav_bar')
            print('did not managed to click_on_sell_in_header_nav_bar')
            take_screenshot(driver, 'click_on_sell_in_header_nav_bar')
            raise err

    @staticmethod
    def click_on_search_result(driver: webdriver):
        try:
            w.wait_for_element(driver, hpl.SEARCH_RESULT)
            element = driver.find_element(*hpl.SEARCH_RESULT)
            element.click()
            logging.info('click_on_search_result')
            print('click_on_search_result')
            return True
        except (NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not managed to click_on_search_result')
            print('did not managed to click_on_search_result')
            take_screenshot(driver, 'click_on_search_result')
            raise err

    @staticmethod
    def select_favorite(driver: webdriver):
        try:
            w.wait_for_element(driver, hpl.FAVORITE_ICON)
            favorites_list = HomesPage.get_favorites_list(driver)
            for favorite in favorites_list:
                favorite.click()
                HomesPage.validate_add_favorite_toaster_message(driver)
                break
            logging.info('select_favorites')
            print('select_favorites')
            return True
        except (NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not managed to select_favorite')
            print('did not managed to select_favorite')
            take_screenshot(driver, 'select_favorite')
            raise err

    @staticmethod
    def get_favorites_list(driver: webdriver):
        try:
            favorites_list = driver.find_elements(*hpl.FAVORITE_ICON)
            logging.info('select_favorite')
            print('select_favorite')
            return favorites_list
        except (NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not managed to select_favorite')
            print('did not managed to select_favorite')
            take_screenshot(driver, 'select_favorite')
            raise err

    @staticmethod
    def click_on_cancel_search_result_in_map(driver: webdriver):
        try:
            action = ActionChains(driver)
            w.wait_for_element(driver, hpl.CANCEL_X)
            if driver.find_elements(*hpl.CANCEL_X) is not None:
                element = driver.find_element(*hpl.CANCEL_X)
                action.move_to_element(element)
                action.click(element)
                action.perform()
            logging.info('click_on_cancel_search_result_in_map')
            print('click_on_cancel_search_result_in_map')
            return True
        except (NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not managed to click_on_cancel_search_result_in_map')
            print('did not managed to click_on_cancel_search_result_in_map')
            take_screenshot(driver, 'click_on_cancel_search_result_in_map')
            raise err

    @staticmethod
    def validate_add_favorite_toaster_message(driver: webdriver):
        try:
            w.wait_for_element(driver, hpl.TOASTER)
            driver.find_element(*hpl.TOASTER)
            logging.info('validate_add_favorite_toaster_message')
            return True
        except NoSuchElementException as err:
            logging.error('did not managed to validate_add_favorite_toaster_message')
            print('did not managed to validate_add_favorite_toaster_message')
            take_screenshot(driver, 'validate_add_favorite_toaster_message')
            raise err

    @staticmethod
    def click_on_homes_tab(driver: webdriver):
        try:
            w.wait_for_element(driver, hpl.HOMES_TAB)
            element = driver.find_element(*hpl.HOMES_TAB)
            element.click()
            logging.info('click_on_homes_tab')
            return True
        except NoSuchElementException as err:
            logging.error('did not managed to click_on_homes_tab')
            print('did not managed to click_on_homes_tab')
            take_screenshot(driver, 'click_on_homes_tab')
            raise err
