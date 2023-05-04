from selenium.webdriver.common.by import By

AMAZON_LOGO = (By.ID, "nav-logo-sprites")
AMAZON_HELLO_USER=(By.XPATH,"//span[contains(text(),'Hello, User')]")
SIGN_IN = (By.XPATH, "//span[contains(text(),'Sign in')]")
EMAIL = (By.ID, "ap_email")
CONTINUE = (By.ID, "continue")
PASSWORD = (By.ID, "ap_password")
SIGN_IN_SUBMIT = (By.ID, "signInSubmit")
SEARCH = (By.ID, "twotabsearchtextbox")
SEARCH_SUBMIT = (By.ID, "nav-search-submit-button")
ADD_TO_CART = (By.ID, "add-to-cart-button")
CART = (By.ID, "nav-cart-count")
DELETE = (By.NAME, "submit.delete.C2B2C2E2WZ8G")


