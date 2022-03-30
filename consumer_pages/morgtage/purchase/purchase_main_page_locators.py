from selenium.webdriver.common.by import By


class PurchaseMainPageLocators:
    PURCHASE_OPTION = (By.XPATH, '//*[.=" Purchase "]')
    USER_ICON = (By.XPATH, '//*[@re2e="userIcon"]')
    INTEREST_RATES = (By.XPATH, '//*[.=" Interest Rate "]')
    REAL_ESTATE = (By.XPATH, '/html/body/loans-root/loans-header/header/nav/ul/li[1]/div')
    ZIP_CODE = (By.ID, 'mat-input-3')
