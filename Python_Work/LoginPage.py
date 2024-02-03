from selenium.webdriver.common.by import By
from selenium import webdriver
class Login:
    user_id = 'Email'
    user_password = 'Password'
    login_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver= driver

    def sendusername(self, user):
        self.driver.find_element(By.ID, self.user_id).clear()
        self.driver.find_element(By.ID, self.user_id).send_keys(user)

    def sendpassword(self, password):
        self.driver.find_element(By.ID, self.user_password).clear()
        self.driver.find_element(By.ID, self.user_password).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_xpath).click()