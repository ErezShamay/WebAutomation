from selenium.webdriver.common.by import By


class SellPageLocators:
    VALIDATE_NAVIGATION = (By.CLASS_NAME, 'sell-your-home__description')
    TRADE_IN_OPTION = (By.XPATH, '//*[.=" Move hassle-free. Use our cash to buy before you sell. "]')
    SELL_OPTION = (By.XPATH, '//*[.=" Sell with superior service and save thousands. "]')
    GET_STARTED = (By.XPATH, '//*[.="Get started"]')
    HOME_VALUATION = (By.CLASS_NAME, 'home-valuation-modal__container')
    SEARCH_ADDRESS = (By.XPATH, '//*[@re2e="searchInputField"]')
    SEARCH_VALUE = (By.XPATH, '//*[.="100 Dool Avenue, Calexico, CA 92231"]')
    SELECT_SEARCH_VALUE = (By.CLASS_NAME, 'selected-text')
    REQUEST_HOME_VALUATION_BUTTON = (By.XPATH, '//*[.=" Request home valuation "]')
    CONGRATS_MESSAGE = (By.CLASS_NAME, 'congrats-message')
