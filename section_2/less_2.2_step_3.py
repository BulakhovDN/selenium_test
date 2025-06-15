import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

with webdriver.Chrome() as browser:
    browser.get("https://suninjuly.github.io/selects1.html")

    x1_element = browser.find_element(By.XPATH, "//span[@id='num1']")
    x1 = int(x1_element.text)
    x2_element = browser.find_element(By.XPATH, "//span[@id='num2']")
    x2 = int(x2_element.text)
    sum_x1_and_x2 = x1 + x2

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(f"{sum_x1_and_x2}")

    browser.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()
    time.sleep(10)
    