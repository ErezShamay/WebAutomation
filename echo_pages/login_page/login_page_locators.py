from selenium.webdriver.common.by import By


class LoginPageLocators:
    GOOGLE_SIGN_IN_BUTTON = (By.XPATH, '//*[.="Sign in with Google"]')
    GOOGLE_USER = (By.XPATH, '//*[@data-identifier="erez@reali.com"]')
    EMAIL_FIELD = (By.ID, 'identifierId')
    EMAIL_NEXT_BUTTON = (By.ID, 'identifierNext')
    PASSWORD_FIELD = (By.ID, 'password')
    PASSWORD_NEXT_BUTTON = (By.ID, 'passwordNext')
