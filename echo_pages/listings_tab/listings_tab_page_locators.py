from selenium.webdriver.common.by import By


class ListingsTabPageLocators:
    LISTINGS_TAB = (By.ID, 'mat-badge-content-7')
    LISTINGS_TABLE = (By.TAG_NAME, 'tbody')
