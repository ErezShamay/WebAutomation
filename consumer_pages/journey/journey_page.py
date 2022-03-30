import logging
import time

from selenium import webdriver
from selenium.common.exceptions import *

from reali_web.conftest import take_screenshot
from reali_web.consumer_pages.journey import journey_page_locators
from reali_web.wait import wait_options
from reali_web.consumer_pages.buy.homes import homes_page

jpl = journey_page_locators.JourneyPageLocators
wf = wait_options.wait_functions
hp = homes_page.HomesPage


class JourneyPage:
    @staticmethod
    def navigate_to_journey_page(driver: webdriver):
        try:
            element = driver.find_element(*jpl.JOURNEY_TAB)
            element.click()
            logging.info('clicked on journey tab')
            print('clicked on journey tab')
            assert JourneyPage.validate_navigation_to_journey_page(driver)
            return True
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not clicked on journey tab')
            print('did not clicked on journey tab')
            take_screenshot(driver, 'navigate_to_journey_page')
            raise err

    @staticmethod
    def validate_navigation_to_journey_page(driver: webdriver):
        try:
            wf.wait_for_element(driver, jpl.STEP_2)
            driver.find_element(*jpl.STEP_2)
            logging.info('validate_navigation_to_journey_page')
            print('validate_navigation_to_journey_page')
            return True
        except NoSuchElementException as err:
            logging.error('did not validate_navigation_to_journey_page')
            print('did not validate_navigation_to_journey_page')
            take_screenshot(driver, 'validate_navigation_to_journey_page')
            raise err

    @staticmethod
    def click_on_search_for_listings(driver: webdriver):
        try:
            element = driver.find_element(*jpl.SEARCH_FOR_LISTINGS_BUTTON)
            element.click()
            logging.info('click_on_search_for_listings')
            print('click_on_search_for_listings')
            assert hp.validate_navigation_to_homes_primary_page(driver)
            return True
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_search_for_listings')
            print('did not click_on_search_for_listings')
            take_screenshot(driver, 'click_on_search_for_listings')
            raise err

    @staticmethod
    def click_on_browse_listings_tab(driver: webdriver):
        try:
            element = driver.find_element(*jpl.BROWSE_LISTINGS)
            element.click()
            logging.info('click_on_browse_listings_tab')
            print('click_on_browse_listings_tab')
            assert JourneyPage.validate_navigate_to_browse_listings_tab(driver)
            return True
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_browse_listings_tab')
            print('did not click_on_browse_listings_tab')
            take_screenshot(driver, 'click_on_browse_listings_tab')
            raise err

    @staticmethod
    def click_on_take_a_tour_tab(driver: webdriver):
        try:
            element = driver.find_element(*jpl.TAKE_A_TOUR)
            element.click()
            logging.info('click_on_take_a_tour_tab')
            print('click_on_take_a_tour_tab')
            assert JourneyPage.validate_navigate_to_take_a_tour_tab(driver)
            return True
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_take_a_tour_tab')
            print('did not click_on_take_a_tour_tab')
            take_screenshot(driver, 'click_on_take_a_tour_tab')
            raise err

    @staticmethod
    def click_on_get_home_valuation_tab(driver: webdriver):
        try:
            element = driver.find_element(*jpl.GET_HOME_VALUATION)
            element.click()
            logging.info('click_on_get_home_valuation_tab')
            print('click_on_get_home_valuation_tab')
            assert JourneyPage.validate_navigate_to_get_home_valuation_tab(driver)
            return True
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_get_home_valuation_tab')
            print('did not click_on_get_home_valuation_tab')
            take_screenshot(driver, 'click_on_get_home_valuation_tab')
            raise err

    @staticmethod
    def click_on_get_reali_verified_tab(driver: webdriver):
        try:
            element = driver.find_element(*jpl.GET_REALI_VERIFIED)
            element.click()
            logging.info('click_on_get_reali_verified_tab')
            print('click_on_get_reali_verified_tab')
            assert JourneyPage.validate_navigate_to_get_reali_verified_tab(driver)
            return True
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_get_reali_verified_tab')
            print('did not click_on_get_reali_verified_tab')
            take_screenshot(driver, 'click_on_get_reali_verified_tab')
            raise err

    @staticmethod
    def click_on_step_2_button(driver: webdriver):
        try:
            element = driver.find_element(*jpl.STEP_2)
            element.click()
            logging.info('click_on_step_2_button')
            print('click_on_step_2_button')
            assert JourneyPage.validate_navigate_to_step_2_button(driver)
            return True
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_step_2_button')
            print('did not click_on_step_2_button')
            take_screenshot(driver, 'click_on_step_2_button')
            raise err

    @staticmethod
    def validate_navigate_to_browse_listings_tab(driver: webdriver):
        try:
            wf.wait_for_element(driver, jpl.SEARCH_FOR_LISTINGS_BUTTON)
            driver.find_element(*jpl.SEARCH_FOR_LISTINGS_BUTTON)
            logging.info('validate_navigation_to_browse_listings_tab')
            print('validate_navigation_to_browse_listings_tab')
            return True
        except NoSuchElementException as err:
            logging.error('did not managed to validate_navigation_to_browse_listings_tab')
            print('did not managed to validate_navigation_to_browse_listings_tab')
            take_screenshot(driver, 'validate_navigate_to_browse_listings_tab')
            raise err

    @staticmethod
    def validate_navigate_to_take_a_tour_tab(driver: webdriver):
        try:
            wf.wait_for_element(driver, jpl.SCHEDULE_A_TOUR_BUTTON)
            driver.find_element(*jpl.SCHEDULE_A_TOUR_BUTTON)
            logging.info('validate_navigate_to_take_a_tour_tab')
            print('validate_navigate_to_take_a_tour_tab')
            return True
        except NoSuchElementException as err:
            logging.error('did not managed to validate_navigate_to_take_a_tour_tab')
            print('did not managed to validate_navigate_to_take_a_tour_tab')
            take_screenshot(driver, 'validate_navigate_to_take_a_tour_tab')
            raise err

    @staticmethod
    def validate_navigate_to_get_home_valuation_tab(driver: webdriver):
        try:
            wf.wait_for_element(driver, jpl.REQUEST_HOME_VALUATION_BUTTON)
            driver.find_element(*jpl.REQUEST_HOME_VALUATION_BUTTON)
            logging.info('click_on_get_home_valuation_tab')
            print('click_on_get_home_valuation_tab')
            return True
        except NoSuchElementException as err:
            logging.error('did not click_on_get_home_valuation_tab')
            print('did not click_on_get_home_valuation_tab')
            take_screenshot(driver, 'validate_navigate_to_get_home_valuation_tab')
            raise err

    @staticmethod
    def validate_navigate_to_get_reali_verified_tab(driver: webdriver):
        try:
            actual = driver.current_url
            assert 'get-reali-verified' in actual
            logging.info('validate_navigate_to_get_reali_verified_tab')
            print('validate_navigate_to_get_reali_verified_tab')
            return True
        except (AssertionError, WebDriverException) as err:
            logging.error('did not managed to validate_navigate_to_get_reali_verified_tab')
            print('did not managed to validate_navigate_to_get_reali_verified_tab')
            take_screenshot(driver, 'validate_navigate_to_get_reali_verified_tab')
            raise err

    @staticmethod
    def validate_navigate_to_step_2_button(driver: webdriver):
        try:
            wf.wait_for_element(driver, jpl.STEP_3)
            driver.find_element(*jpl.STEP_3)
            driver.find_element(*jpl.STEP_1)
            logging.info('click_on_step_2_button')
            print('click_on_step_2_button')
            return True
        except NoSuchElementException as err:
            logging.error('did not click_on_step_2_button')
            print('did not click_on_step_2_button')
            take_screenshot(driver, 'validate_navigate_to_step_2_button')
            raise err

    @staticmethod
    def click_on_schedule_a_tour_button(driver: webdriver):
        try:
            element = driver.find_element(*jpl.SCHEDULE_A_TOUR_BUTTON)
            element.click()
            logging.info('click_on_schedule_a_tour_button')
            print('click_on_schedule_a_tour_button')
            assert JourneyPage.validate_navigation_to_wishlist(driver)
            return True
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_schedule_a_tour_button')
            print('did not click_on_schedule_a_tour_button')
            take_screenshot(driver, 'click_on_schedule_a_tour_button')
            raise err

    @staticmethod
    def click_on_request_home_valuation_button(driver: webdriver):
        try:
            element = driver.find_element(*jpl.REQUEST_HOME_VALUATION_BUTTON)
            element.click()
            logging.info('click_on_request_home_valuation_button')
            print('click_on_request_home_valuation_button')
            assert JourneyPage.validate_navigation_to_wishlist(driver)
            return True
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_request_home_valuation_button')
            print('did not click_on_request_home_valuation_button')
            take_screenshot(driver, 'click_on_request_home_valuation_button')
            raise err

    @staticmethod
    def click_on_get_pre_approved_button(driver: webdriver):
        try:
            if driver.find_elements(*jpl.REQUEST_SENT) is None:
                element = driver.find_element(*jpl.GET_PRE_APPROVED_BUTTON)
                element.click()
                logging.info('click_on_get_pre_approved_button')
                print('click_on_get_pre_approved_button')
                assert JourneyPage.validate_navigation_to_pre_approved_section(driver)
            return True
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_get_pre_approved_button')
            print('did not click_on_get_pre_approved_button')
            take_screenshot(driver, 'click_on_get_pre_approved_button')
            raise err

    @staticmethod
    def validate_navigation_to_wishlist(driver: webdriver):
        try:
            current_url = driver.current_url
            logging.info('validate_navigation_to_wishlist')
            print('validate_navigation_to_wishlist')
            assert 'wishlist' in current_url
            return True
        except (AssertionError, WebDriverException) as err:
            logging.error('did not validate_navigation_to_wishlist')
            print('did not validate_navigation_to_wishlist')
            take_screenshot(driver, 'validate_navigation_to_wishlist')
            raise err

    @staticmethod
    def validate_navigation_to_pre_approved_section(driver: webdriver):
        try:
            driver.find_element(*jpl.CONNECT_ME)
            logging.info('validate_navigation_to_pre_approved_section')
            print('validate_navigation_to_pre_approved_section')
            return True
        except NoSuchElementException as err:
            logging.error('did not validate_navigation_to_pre_approved_section')
            print('did not validate_navigation_to_pre_approved_section')
            take_screenshot(driver, 'validate_navigation_to_pre_approved_section')
            raise err

    @staticmethod
    def click_on_connect_me_button(driver: webdriver):
        try:
            driver.find_element(*jpl.CONNECT_ME).click()
            logging.info('click_on_connect_me_button')
            print('click_on_connect_me_button')
            assert JourneyPage.validate_clicked_on_connect_ne_button(driver)
            return True
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_connect_me_button')
            print('did not click_on_connect_me_button')
            take_screenshot(driver, 'click_on_connect_me_button')
            raise err

    @staticmethod
    def validate_clicked_on_connect_ne_button(driver: webdriver):
        try:
            wf.wait_for_element(driver, jpl.REQUEST_SENT)
            driver.find_element(*jpl.REQUEST_SENT)
            logging.info('validate_clicked_on_connect_ne_button')
            print('validate_clicked_on_connect_ne_button')
            return True
        except NoSuchElementException as err:
            logging.error('did not validate_clicked_on_connect_ne_button')
            print('did not validate_clicked_on_connect_ne_button')
            take_screenshot(driver, 'validate_clicked_on_connect_ne_button')
            raise err

    @staticmethod
    def click_on_how_to_sell_your_home_tab(driver: webdriver):
        try:
            element = driver.find_element(*jpl.HOW_TO_SELL_YOUR_HOME_TAB)
            element.click()
            logging.info('click_on_how_to_sell_your_home_tab')
            print('click_on_how_to_sell_your_home_tab')
            return True
        except (NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_how_to_sell_your_home_tab')
            print('did not click_on_how_to_sell_your_home_tab')
            take_screenshot(driver, 'click_on_how_to_sell_your_home_tab')
            raise err

    @staticmethod
    def click_on_home_valuation_tab(driver: webdriver):
        try:
            element = driver.find_element(*jpl.HOME_VALUATION_TAB)
            element.click()
            logging.info('click_on_home_valuation_tab')
            print('click_on_home_valuation_tab')
            return True
        except (NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_home_valuation_tab')
            print('did not click_on_home_valuation_tab')
            take_screenshot(driver, 'click_on_home_valuation_tab')
            raise err

    @staticmethod
    def click_on_listings_presentation_tab(driver: webdriver):
        try:
            element = driver.find_element(*jpl.LISTINGS_PRESENTATION_TAB)
            element.click()
            logging.info('click_on_listings_presentation_tab')
            print('click_on_listings_presentation_tab')
            return True
        except (NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_listings_presentation_tab')
            print('did not click_on_listings_presentation_tab')
            take_screenshot(driver, 'click_on_listings_presentation_tab')
            raise err

    @staticmethod
    def click_on_listing_agreement_tab(driver: webdriver):
        try:
            element = driver.find_element(*jpl.LISTING_AGREEMENT_TAB)
            element.click()
            logging.info('click_on_listing_agreement_tab')
            print('click_on_listing_agreement_tab')
            return True
        except (NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_listing_agreement_tab')
            print('did not click_on_listing_agreement_tab')
            take_screenshot(driver, 'click_on_listing_agreement_tab')
            raise err

    @staticmethod
    def validate_clicked_on_how_to_sell_your_home_tab(driver: webdriver):
        try:
            wf.wait_for_element(driver, jpl.SELL_YOUR_HOME_OPTIONS)
            driver.find_element(*jpl.SELL_YOUR_HOME_OPTIONS)
            logging.info('validate_clicked_on_how_to_sell_your_home_tab')
            print('validate_clicked_on_how_to_sell_your_home_tab')
            return True
        except NoSuchElementException as err:
            logging.error('did not validate_clicked_on_how_to_sell_your_home_tab')
            print('did not validate_clicked_on_how_to_sell_your_home_tab')
            take_screenshot(driver, 'validate_clicked_on_how_to_sell_your_home_tab')
            raise err

    @staticmethod
    def validate_clicked_on_home_valuation_tab(driver: webdriver):
        try:
            time.sleep(3)
            actual = driver.current_url
            assert 'home-valuation' in actual
            logging.info('validate_clicked_on_home_valuation_tab')
            print('validate_clicked_on_home_valuation_tab')
            return True
        except (AssertionError, NoSuchElementException) as err:
            logging.error('did not validate_clicked_on_home_valuation_tab')
            print('did not validate_clicked_on_home_valuation_tab')
            take_screenshot(driver, 'validate_clicked_on_home_valuation_tab')
            raise err

    @staticmethod
    def validate_clicked_on_listings_presentation_tab(driver: webdriver):
        try:
            wf.wait_for_element(driver, jpl.REQUEST_VISIT_BUTTON)
            driver.find_element(*jpl.REQUEST_VISIT_BUTTON)
            logging.info('validate_clicked_on_listings_presentation_tab')
            print('validate_clicked_on_listings_presentation_tab')
            return True
        except NoSuchElementException as err:
            logging.error('did not validate_clicked_on_listings_presentation_tab')
            print('did not validate_clicked_on_listings_presentation_tab')
            take_screenshot(driver, 'validate_clicked_on_listings_presentation_tab')
            raise err

    @staticmethod
    def validate_clicked_on_listing_agreement_tab(driver: webdriver):
        try:
            wf.wait_for_element(driver, jpl.LISTING_AGREEMENT)
            driver.find_element(*jpl.LISTING_AGREEMENT)
            logging.info('validate_clicked_on_listing_agreement_tab')
            print('validate_clicked_on_listing_agreement_tab')
            return True
        except NoSuchElementException as err:
            logging.error('did not validate_clicked_on_listing_agreement_tab')
            print('did not validate_clicked_on_listing_agreement_tab')
            take_screenshot(driver, 'validate_clicked_on_listing_agreement_tab')
            raise err

    @staticmethod
    def click_on_buy_and_sell_option(driver: webdriver):
        try:
            element = driver.find_element(*jpl.BUY_AND_SELL_OPTION)
            element.click()
            logging.info('click_on_listing_agreement_tab')
            print('click_on_listing_agreement_tab')
            return True
        except (NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_listing_agreement_tab')
            print('did not click_on_listing_agreement_tab')
            take_screenshot(driver, 'click_on_buy_and_sell_option')
            raise err

    @staticmethod
    def validate_clicked_on_buy_and_sell_option(driver: webdriver):
        try:
            wf.wait_for_element(driver, jpl.GET_STARTED_BUTTON)
            driver.find_element(*jpl.GET_STARTED_BUTTON)
            logging.info('validate_clicked_on_buy_and_sell_option')
            print('validate_clicked_on_buy_and_sell_option')
            return True
        except NoSuchElementException as err:
            logging.error('did not managed to validate_clicked_on_buy_and_sell_option')
            print('did not managed to validate_clicked_on_buy_and_sell_option')
            take_screenshot(driver, 'validate_clicked_on_buy_and_sell_option')
            raise err

    @staticmethod
    def click_on_sell_option(driver: webdriver):
        try:
            element = driver.find_element(*jpl.SELL_OPTION)
            element.click()
            logging.info('click_on_listing_agreement_tab')
            print('click_on_listing_agreement_tab')
            return True
        except (NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_listing_agreement_tab')
            print('did not click_on_listing_agreement_tab')
            take_screenshot(driver, 'click_on_sell_option')
            raise err

    @staticmethod
    def validate_clicked_on_sell_option(driver: webdriver):
        try:
            wf.wait_for_element(driver, jpl.SELL_OPTION)
            element = driver.find_element(*jpl.SELL_OPTION)
            element.click()
            logging.info('validate_clicked_on_sell_option')
            print('validate_clicked_on_sell_option')
            return True
        except NoSuchElementException as err:
            logging.error('did not managed to validate_clicked_on_sell_option')
            print('did not managed to validate_clicked_on_sell_option')
            take_screenshot(driver, 'validate_clicked_on_sell_option')
            raise err

    @staticmethod
    def click_on_request_visit_button(driver: webdriver):
        try:
            element = driver.find_element(*jpl.REQUEST_VISIT_BUTTON)
            element.click()
            logging.info('click_on_request_visit_button')
            print('click_on_request_visit_button')
            return True
        except (NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_request_visit_button')
            print('did not click_on_request_visit_button')
            take_screenshot(driver, 'click_on_request_visit_button')
            raise err

    @staticmethod
    def click_on_get_started_button(driver: webdriver):
        try:
            element = driver.find_element(*jpl.GET_STARTED_BUTTON)
            element.click()
            logging.info('click_on_get_started_button')
            print('click_on_get_started_button')
            return True
        except (NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_get_started_button')
            print('did not click_on_get_started_button')
            take_screenshot(driver, 'click_on_get_started_button')
            raise err

    @staticmethod
    def validate_clicked_on_get_started_button(driver: webdriver):
        try:
            wf.wait_for_element(driver, jpl.REQUEST_HOME_VALUATION)
            driver.find_element(*jpl.REQUEST_HOME_VALUATION)
            logging.info('validate_clicked_on_get_started_button')
            print('validate_clicked_on_get_started_button')
            return True
        except NoSuchElementException as err:
            logging.error('did not validate_clicked_on_get_started_button')
            print('did not validate_clicked_on_get_started_button')
            take_screenshot(driver, 'validate_clicked_on_get_started_button')
            raise err

    @staticmethod
    def click_on_close_x_button(driver: webdriver):
        try:
            wf.wait_for_element(driver, jpl.CLOSE_X)
            element = driver.find_element(*jpl.CLOSE_X)
            element.click()
            logging.info('click_on_close_x_button')
            print('click_on_close_x_button')
            return True
        except (NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_close_x_button')
            print('did not click_on_close_x_button')
            take_screenshot(driver, 'click_on_close_x_button')
            raise err

    @staticmethod
    def validate_clicked_on_request_home_valuation_button(driver: webdriver):
        try:
            wf.wait_for_element(driver, jpl.REQUEST_HOME_VALUATION)
            driver.find_element(*jpl.CLOSE_X).click()
            logging.info('validate_clicked_on_request_home_valuation_button')
            print('validate_clicked_on_request_home_valuation_button')
            return True
        except NoSuchElementException as err:
            logging.error('did not validate_clicked_on_request_home_valuation_button')
            print('did not validate_clicked_on_request_home_valuation_button')
            take_screenshot(driver, 'validate_clicked_on_request_home_valuation_button')
            raise err

    @staticmethod
    def validate_clicked_on_request_visit_button(driver: webdriver):
        try:
            if driver.find_elements(*jpl.REFER_ME) is None:
                wf.wait_for_element(driver, jpl.REFER_ME)
                driver.find_element(*jpl.REFER_ME)
            logging.info('validate_clicked_on_request_visit_button')
            print('validate_clicked_on_request_visit_button')
            return True
        except NoSuchElementException as err:
            logging.error('did not validate_clicked_on_request_visit_button')
            print('did not validate_clicked_on_request_visit_button')
            take_screenshot(driver, 'validate_clicked_on_request_visit_button')
            raise err

    @staticmethod
    def click_on_cash_back_tab(driver: webdriver):
        try:
            element = driver.find_element(*jpl.CASH_BACK)
            element.click()
            logging.info('click_on_cash_back_tab')
            print('click_on_cash_back_tab')
            assert JourneyPage.validate_clicked_on_cash_back_tab(driver)
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_cash_back_tab')
            print('did not click_on_cash_back_tab')
            take_screenshot(driver, 'click_on_cash_back_tab')
            raise err

    @staticmethod
    def click_on_contingency_period_tab(driver: webdriver):
        try:
            element = driver.find_element(*jpl.CONTINGENCY_PERIOD)
            element.click()
            logging.info('click_on_contingency_period_tab')
            print('click_on_contingency_period_tab')
            assert JourneyPage.validate_clicked_on_contingency_period_tab(driver)
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_contingency_period_tab')
            print('did not click_on_contingency_period_tab')
            take_screenshot(driver, 'click_on_contingency_period_tab')
            raise err

    @staticmethod
    def click_on_last_looks_tab(driver: webdriver):
        try:
            element = driver.find_element(*jpl.LAST_LOOKS)
            element.click()
            logging.info('click_on_last_looks_tab')
            print('click_on_last_looks_tab')
            assert JourneyPage.validate_clicked_on_last_looks_tab(driver)
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_last_looks_tab')
            print('did not click_on_last_looks_tab')
            take_screenshot(driver, 'click_on_last_looks_tab')
            raise err

    @staticmethod
    def click_on_closing_time_tab(driver: webdriver):
        try:
            element = driver.find_element(*jpl.CLOSING_TIME)
            element.click()
            logging.info('click_on_closing_time_tab')
            print('click_on_closing_time_tab')
            assert JourneyPage.validate_clicked_on_closing_time_tab(driver)
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_closing_time_tab')
            print('did not click_on_closing_time_tab')
            take_screenshot(driver, 'click_on_closing_time_tab')
            raise err

    @staticmethod
    def click_on_open_escrow_tab(driver: webdriver):
        try:
            element = driver.find_element(*jpl.OPEN_ESCROW)
            element.click()
            logging.info('click_on_closing_time_tab')
            print('click_on_closing_time_tab')
            assert JourneyPage.validate_clicked_on_open_escrow_tab(driver)
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_closing_time_tab')
            print('did not click_on_closing_time_tab')
            take_screenshot(driver, 'click_on_open_escrow_tab')
            raise err

    @staticmethod
    def click_on_make_your_offer_tab(driver: webdriver):
        try:
            element = driver.find_element(*jpl.MAKE_YOUR_OFFER)
            element.click()
            logging.info('click_on_make_your_offer_tab')
            print('click_on_make_your_offer_tab')
            assert JourneyPage.validate_clicked_on_make_your_offer_tab(driver)
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_make_your_offer_tab')
            print('did not click_on_make_your_offer_tab')
            take_screenshot(driver, 'click_on_make_your_offer_tab')
            raise err

    @staticmethod
    def click_on_sign_and_submit_tab(driver: webdriver):
        try:
            driver.find_element(*jpl.SIGN_AND_SUBMIT).click()
            logging.info('click_on_sign_and_submit_tab')
            print('click_on_sign_and_submit_tab')
            assert JourneyPage.validate_clicked_on_sign_and_submit_tab(driver)
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_sign_and_submit_tab')
            print('did not click_on_sign_and_submit_tab')
            take_screenshot(driver, 'click_on_sign_and_submit_tab')
            raise err

    @staticmethod
    def click_on_negotiate_tab(driver: webdriver):
        try:
            element = driver.find_element(*jpl.NEGOTIATE)
            element.click()
            logging.info('click_on_negotiate_tab')
            print('click_on_negotiate_tab')
            assert JourneyPage.validate_clicked_on_negotiate_tab(driver)
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_negotiate_tab')
            print('did not click_on_negotiate_tab')
            take_screenshot(driver, 'click_on_negotiate_tab')
            raise err

    @staticmethod
    def click_on_make_your_offer(driver: webdriver):
        try:
            element = driver.find_element(*jpl.MAKE_YOUR_OFFER)
            element.click()
            logging.info('click_on_make_your_offer')
            print('click_on_make_your_offer')
            assert JourneyPage.validate_clicked_on_make_your_offer(driver)
        except (AssertionError, NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('did not click_on_make_your_offer')
            print('did not click_on_make_your_offer')
            take_screenshot(driver, 'click_on_make_your_offer')
            raise err

    @staticmethod
    def validate_clicked_on_cash_back_tab(driver: webdriver):
        try:
            wf.wait_for_element(driver, jpl.GET_CASH_BACK)
            driver.find_element(*jpl.GET_CASH_BACK)
            logging.info('validate_clicked_on_cash_back_tab')
            print('validate_clicked_on_cash_back_tab')
            return True
        except NoSuchElementException as err:
            logging.error('did not validate_clicked_on_cash_back_tab')
            print('did not validate_clicked_on_cash_back_tab')
            take_screenshot(driver, 'validate_clicked_on_cash_back_tab')
            raise err

    @staticmethod
    def validate_clicked_on_contingency_period_tab(driver: webdriver):
        try:
            wf.wait_for_element(driver, jpl.DES_CONTINGENCY_PERIOD)
            driver.find_element(*jpl.DES_CONTINGENCY_PERIOD)
            logging.info('validate_clicked_on_contingency_period_tab')
            print('validate_clicked_on_contingency_period_tab')
            return True
        except NoSuchElementException as err:
            logging.error('did not validate_clicked_on_contingency_period_tab')
            print('did not validate_clicked_on_contingency_period_tab')
            take_screenshot(driver, 'validate_clicked_on_contingency_period_tab')
            raise err

    @staticmethod
    def validate_clicked_on_last_looks_tab(driver: webdriver):
        try:
            wf.wait_for_element(driver, jpl.DES_LAST_LOOKS)
            driver.find_element(*jpl.DES_LAST_LOOKS)
            logging.info('validate_clicked_on_last_looks_tab')
            print('validate_clicked_on_last_looks_tab')
            return True
        except NoSuchElementException as err:
            logging.error('did not validate_clicked_on_last_looks_tab')
            print('did not validate_clicked_on_last_looks_tab')
            take_screenshot(driver, 'validate_clicked_on_last_looks_tab')
            raise err

    @staticmethod
    def validate_clicked_on_closing_time_tab(driver: webdriver):
        try:
            wf.wait_for_element(driver, jpl.DES_CLOSING_TIME)
            driver.find_element(*jpl.DES_CLOSING_TIME)
            logging.info('validate_clicked_on_closing_time_tab')
            print('validate_clicked_on_closing_time_tab')
            return True
        except NoSuchElementException as err:
            logging.error('did not validate_clicked_on_closing_time_tab')
            print('did not validate_clicked_on_closing_time_tab')
            take_screenshot(driver, 'validate_clicked_on_closing_time_tab')
            raise err

    @staticmethod
    def validate_clicked_on_open_escrow_tab(driver: webdriver):
        try:
            wf.wait_for_element(driver, jpl.DES_OPEN_ESCROW)
            driver.find_element(*jpl.DES_OPEN_ESCROW)
            logging.info('validate_clicked_on_open_escrow_tab')
            print('validate_clicked_on_open_escrow_tab')
            return True
        except NoSuchElementException as err:
            logging.error('did not validate_clicked_on_open_escrow_tab')
            print('did not validate_clicked_on_open_escrow_tab')
            take_screenshot(driver, 'validate_clicked_on_open_escrow_tab')
            raise err

    @staticmethod
    def validate_clicked_on_make_your_offer_tab(driver: webdriver):
        try:
            wf.wait_for_element(driver, jpl.DRAFT_AN_OFFER_BUTTON)
            driver.find_element(*jpl.DRAFT_AN_OFFER_BUTTON)
            logging.info('validate_clicked_on_make_your_offer_tab')
            print('validate_clicked_on_make_your_offer_tab')
            return True
        except NoSuchElementException as err:
            logging.error('did not validate_clicked_on_make_your_offer_tab')
            print('did not validate_clicked_on_make_your_offer_tab')
            take_screenshot(driver, 'validate_clicked_on_make_your_offer_tab')
            raise err

    @staticmethod
    def validate_clicked_on_sign_and_submit_tab(driver: webdriver):
        try:
            wf.wait_for_element(driver, jpl.DES_SIGN_AND_SUBMIT)
            driver.find_element(*jpl.DES_SIGN_AND_SUBMIT)
            logging.info('validate_clicked_on_sign_and_submit_tab')
            print('validate_clicked_on_sign_and_submit_tab')
            return True
        except NoSuchElementException as err:
            logging.error('did not validate_clicked_on_sign_and_submit_tab')
            print('did not validate_clicked_on_sign_and_submit_tab')
            take_screenshot(driver, 'validate_clicked_on_sign_and_submit_tab')
            raise err

    @staticmethod
    def validate_clicked_on_negotiate_tab(driver: webdriver):
        try:
            wf.wait_for_element(driver, jpl.DES_NEGOTIATE)
            driver.find_element(*jpl.DES_NEGOTIATE)
            logging.info('validate_clicked_on_negotiate_tab')
            print('validate_clicked_on_negotiate_tab')
            return True
        except NoSuchElementException as err:
            logging.error('did not validate_clicked_on_negotiate_tab')
            print('did not validate_clicked_on_negotiate_tab')
            take_screenshot(driver, 'validate_clicked_on_negotiate_tab')
            raise err

    @staticmethod
    def validate_clicked_on_make_your_offer(driver: webdriver):
        try:
            wf.wait_for_element(driver, jpl.DES_MAKE_YOUR_OFFER)
            driver.find_element(*jpl.DES_MAKE_YOUR_OFFER)
            logging.info('validate_clicked_on_make_your_offer')
            print('validate_clicked_on_make_your_offer')
            return True
        except NoSuchElementException as err:
            logging.error('did not validate_clicked_on_make_your_offer')
            print('did not validate_clicked_on_make_your_offer')
            take_screenshot(driver, 'validate_clicked_on_make_your_offer')
            raise err
