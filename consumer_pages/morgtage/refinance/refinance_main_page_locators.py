from selenium.webdriver.common.by import By


class RefinanceMainPageLocators:
    REFINANCE_OPTION = (By.XPATH, '//*[.=" Refinance "]')
    USER_ICON = (By.XPATH, '//*[@re2e="userIcon"]')
    INTEREST_RATES = (By.XPATH, '//*[.=" Interest Rate "]')
    REAL_ESTATE = (By.XPATH, '/html/body/loans-root/loans-header/header/nav/ul/li[1]/div')
    RATES_TITLE = (By.XPATH, '//*[@re2e="ratesTitle"]')
    ZIP_CODE = (By.ID, 'mat-input-4')
