import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get("https://suninjuly.github.io/explicit_wait2.html")

    # ждем нужный текст на странице
    button = WebDriverWait(browser, 12).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    browser.find_element(By.CSS_SELECTOR, "#book").click()

    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_element.text
    y = calc(x)

    browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(f"{y}")

    browser.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()

    time.sleep(10)
