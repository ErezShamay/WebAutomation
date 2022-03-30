from selenium.webdriver.common.by import By


class TimeLinePageLocators:
    OPTION_1 = (By.XPATH, '//*[.="0-3 Months"]')
    OPTION_2 = (By.XPATH, '//*[.="4-6 Months"]')
    OPTION_3 = (By.XPATH, '//*[.="6+ Months"]')
