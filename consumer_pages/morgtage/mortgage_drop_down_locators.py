from selenium.webdriver.common.by import By


class MortgageDropDownLocators:
    PURCHASE = (By.XPATH, '//*[.=" Purchase "]')
    REFINANCE = (By.XPATH, '//*[.=" Refinance "]')
    MORTGAGE_DROP_DOWN_MENU = (By.ID, 'mat-menu-panel-0')
