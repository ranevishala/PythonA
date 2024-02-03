from selenium import webdriver
from LoginPage import Login

class Test_Login:
    url = 'https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F'
    username = 'admin@yourstore.com'
    password = 'admin'

    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.loginpage = Login(self.driver)
        self.loginpage.sendusername(self.username)
        self.loginpage.sendpassword(self.password)
        self.loginpage.click_login()
        title = self.driver.title
        if title == 'Dashboard / nopCommerce administration':
            assert True
        else:
            assert False

#test1 = Test_Login()
#test1.test_login()