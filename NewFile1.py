import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5000/")
ele = driver.find_element(By.NAME, 'keyword')
time.sleep(3)
ele.send_keys('Python')