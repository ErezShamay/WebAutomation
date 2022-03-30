from selenium.webdriver.common.by import By


class VerificationTabPageLocators:
    VERIFICATIONS_TAB = (By.XPATH, '/html/body/app-root/app-main/mat-sidenav-container/mat-sidenav/div/app-side'
                                   '-navigation/mat-nav-list/mat-nav-list/a[1]/div/span')
    VERIFICATIONS_TABLE = (By.TAG_NAME, 'tbody')
    STATUS_FIELD = (By.ID, 'mat-select-2')
    STATUS_DROP_DOWN_MENU = (By.ID, 'mat-option-4')
    PENDING = (By.ID, 'mat-option-3')
    WORKING = (By.ID, 'mat-option-4')
    TOASTER_MESSAGE = (By.XPATH, '//*[@dir="ltr"]')
