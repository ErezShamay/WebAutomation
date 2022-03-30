from selenium.webdriver.common.by import By


class InterestedInPageLocators:
    BUYING = (By.XPATH, '//*[.="Buying"]')
    SELLING = (By.XPATH, '//*[.="Selling"]')
    BUYING_AND_SELLING = (By.XPATH, '//*[.="Buying and Selling"]')
