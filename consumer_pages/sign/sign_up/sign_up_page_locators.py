from selenium.webdriver.common.by import By


class SignUpPageLocators:
    ZERO_EMAIL_LOCATOR = (By.ID, 'mat-input-0')
    ZERO_PASSWORD_LOCATOR = (By.ID, 'mat-input-1')
    EMAIL_LOCATOR = (By.ID, 'mat-input-2')
    PASSWORD_LOCATOR = (By.ID, 'mat-input-3')
    SIGN_UP_BUTTON = (By.XPATH, '//*[.=" sign up "]')
    FIRST_NAME = (By.ID, 'mat-input-4')
    LAST_NAME = (By.ID, 'mat-input-5')
    PHONE_NUMBER = (By.ID, 'mat-input-6')
    CONTINUE_BUTTON = (By.XPATH, '//*[.=" Continue "]')
    CALIFORNIA = (By.XPATH, '//*[.="California"]')
    OUTSIDE_CALIFORNIA = (By.XPATH, '//*[.="Outside California"]')
    SIGN_IN_LINK = (By.XPATH, '//*[@re2e="modalSignInBtn"]')
