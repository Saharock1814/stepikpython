from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import os
import math

browser = webdriver.Chrome('/Users/sah_m/Desktop/Foravtotests/chromedriver 3')
browser.get('http://suninjuly.github.io/explicit_wait2.html')
price_value = wdw(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
book_button = browser.find_element_by_id("book").click()
x_element = browser.find_element_by_id("input_value")
x = x_element.text


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


y = calc(x)
answer = browser.find_element_by_id("answer").send_keys(y)
submit2 = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
