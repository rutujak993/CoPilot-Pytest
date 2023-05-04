import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webself.driver.common.by import By
from selenium.webself.driver.common.action_chains import ActionChains
from selenium import webdriver
from AmazonLocators import *

driver = None


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class TestLogin(BaseTest):
    def test_login(self,username,password):
        self.driver.get("https://www.amazon.in/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        element_to_hover_over = self.driver.find_element(By.XPATH,"//span[contains(text(),'Account & Lists')]")
        hover = ActionChains(driver).move_to_element(element_to_hover_over)
        hover.perform()

        self.driver.find_element(By.XPATH,"//*[@id='nav-flyout-ya-signin']//span").click()
        self.driver.find_element(By.ID, "ap_email").send_keys(username)
        self.driver.find_element(By.ID, "continue").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.ID, "ap_password").send_keys(password)
        self.driver.find_element(By.ID, "signInSubmit").click()
        self.driver.implicitly_wait(2)

    def connect_with_us_on_facebook(self):
        self.driver.find_element(By.XPATH, "//div[text()='Connect with Us']/following-sibling::ul//a[contains(text(),'Facebook')]")
        self.driver.find_element(By.XPATH, "//div[text()='Connect with Us']/following-sibling::ul//a[contains(text(),'Facebook')]").click()
        self.driver.wait.until(EC.presence_of_element_located((By.ID, "//span[contains(text(),'See more of Amazon India on Facebook')]")))

    def connect_with_us_on_Twitter(self):
        self.driver.find_element(By.XPATH, "//div[text()='Connect with Us']/following-sibling::ul//a[contains(text(),'Twitter')]")
        self.driver.find_element(By.XPATH, "//div[text()='Connect with Us']/following-sibling::ul//a[contains(text(),'Twitter')]").click()
        self.driver.wait.until(EC.presence_of_element_located((By.ID, "//span[contains(text(),'The official Twitter profile of ')]")))