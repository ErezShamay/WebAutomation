from selenium.webdriver.common.by import By


class SignInPageLocators:
    SIGN_UP = (By.XPATH, '//*[.="Sign Up"]')
    GENERAL_EMAIL_LOCATOR = (By.ID, 'mat-input-0')
    GENERAL_PASSWORD_LOCATOR = (By.ID, 'mat-input-1')
    EMAIL_LOCATOR = (By.ID, 'mat-input-2')
    PASSWORD_LOCATOR = (By.ID, 'mat-input-3')
    SIGN_IN_BUTTON = (By.XPATH, '//*[.=" Sign In "]')
    HEADER_SIGN_IN_BUTTON = (By.XPATH, '//*[@re2e="headerSignIn"]')
    USER_ICON = (By.CLASS_NAME, 'header__sign-in-button')
    FORGOT_PASSWORD = (By.CLASS_NAME, 'forgot-password')
