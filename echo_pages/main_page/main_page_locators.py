from selenium.webdriver.common.by import By


class MainPageLocators:
    CHAT_CARD = (By.XPATH, '//*[@re2e="cardUserName"]')
    REQUESTS_TAB = (By.XPATH, '//*[.="Requests "]')
