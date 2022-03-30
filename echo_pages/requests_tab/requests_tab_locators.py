from selenium.webdriver.common.by import By


class RequestsTabLocators:
    REQUESTS_TAB = (By.XPATH, '/html/body/app-root/app-main/mat-sidenav-container/mat-sidenav/div/app-side-navigation'
                              '/mat-nav-list/a[5]/div/span')
    VERIFICATIONS_TAB = (By.XPATH, '/html/body/app-root/app-main/mat-sidenav-container/mat-sidenav/div/app-side'
                                   '-navigation/mat-nav-list/mat-nav-list/a[1]/div/span')
