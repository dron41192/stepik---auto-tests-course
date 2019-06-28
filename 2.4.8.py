from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = WebDriverWait(browser, 12).until(
		EC.text_to_be_present_in_element((By.ID, "price"), "10000"))

but = browser.find_element_by_xpath("//button[@id='book']")
but.click()

x = browser.find_element_by_xpath('//span[@id = "input_value"]')
x1 = x.text
y = calc(x1)

input = browser.find_element_by_xpath('//input[@name = "text"]')
input.send_keys(y)

buttn = browser.find_element_by_xpath('//button[@type = "submit"]')
buttn.click() 