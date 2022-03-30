from selenium.webdriver.common.by import By


class VerificationPageLocators:
    TOASTER_ERROR_MESSAGE = (By.CLASS_NAME, 'cdk-global-overlay-wrapper')
    FIRST_DIGIT = (By.XPATH, '//*[@id="cdk-overlay-0"]/rui-slide-modal/rw-sign-up-questions/rui-stepper/rw-verification-step/div/div[1]/rui-verification-code/rui-verification-input[1]')
    SECOND_DIGIT = (By.XPATH, '//*[@id="cdk-overlay-0"]/rui-slide-modal/rw-sign-up-questions/rui-stepper/rw-verification-step/div/div[1]/rui-verification-code/rui-verification-input[2]')
    THIRD_DIGIT = (By.XPATH, '//*[@id="cdk-overlay-0"]/rui-slide-modal/rw-sign-up-questions/rui-stepper/rw-verification-step/div/div[1]/rui-verification-code/rui-verification-input[3]')
    FOURTH_DIGIT = (By.XPATH, '//*[@id="cdk-overlay-0"]/rui-slide-modal/rw-sign-up-questions/rui-stepper/rw-verification-step/div/div[1]/rui-verification-code/rui-verification-input[4]')
    FIFTH_DIGIT = (By.XPATH, '//*[@id="cdk-overlay-0"]/rui-slide-modal/rw-sign-up-questions/rui-stepper/rw-verification-step/div/div[1]/rui-verification-code/rui-verification-input[5]')
    SIXTH_DIGIT = (By.XPATH, '//*[@id="cdk-overlay-0"]/rui-slide-modal/rw-sign-up-questions/rui-stepper/rw-verification-step/div/div[1]/rui-verification-code/rui-verification-input[6]')
    VERIFICATION_CODE = (By.XPATH, '//*[@re2e="verificationCodeInput"]')
    WAIT = (By.CLASS_NAME, 'header__sign-in-button')
