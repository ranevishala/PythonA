from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


a = 123
b,c = divmod(123,10)
print(b,c)

c,d = divmod(b,10)
print()
def number_Change(num):
    num = str(num)
    num = num[::-1]
    return (int(num))

numb = number_Change(123)
print(numb)


driver = webdriver.Chrome()
driver.get('url')
list1 = driver.window_handles
for i in list1:
    driver.switch_to.window(i)
element = 'qqq'
actions = ActionChains(driver)
actions.double_click(element).perform()
driver.implicitly_wait(12)
alert = driver.switch_to.alert
alert.accept()

WebDriverWait(driver,10).until(EC.presence_of_element_located(By.XPATH, "//[@id=\"gbwa\"]/div/a"))

import requests

requests.get('https://ww.google.com')
