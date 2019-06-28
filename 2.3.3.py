from selenium import webdriver

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

butn = browser.find_element_by_xpath("//button[@type = 'submit']")
butn.click()

confirm = browser.switch_to.alert
confirm.accept()

x = browser.find_element_by_xpath('//span[@id = "input_value"]')
x1 = x.text
y = calc(x1)

input = browser.find_element_by_xpath('//input[@name = "text"]')
input.send_keys(y)

buttn = browser.find_element_by_xpath('//button[@type = "submit"]')
buttn.click() 