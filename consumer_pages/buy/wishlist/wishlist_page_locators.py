from selenium.webdriver.common.by import By


class WishListPageData:
    FAVORITE = (By.XPATH, '/html/body/rw-root/rw-slide-panel/mat-sidenav-container/mat-sidenav-content/main/section/rw-buyer-journey/div/rw-wishlist/rw-wishlist-list/div/rw-wishlist-grid[1]/div/rw-listing-card/a/div[2]/div[1]/div[2]/div/mat-icon')
    LISTINGS_CARD = (By.CLASS_NAME, 'listing-info-favorite')
    WISHLIST_TAB = (By.XPATH, '//*[.="Wishlist"]')
    LISTING_INFO = (By.XPATH, '//*[@re2e="listingInfo"]')
