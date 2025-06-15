import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    new_window = browser.window_handles[1]
    # переход на новую вкладку
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_element.text
    y = calc(x)

    browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(f"{y}")

    browser.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()

    time.sleep(10)
