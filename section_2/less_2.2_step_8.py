import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/file_input.html")
    browser.find_element(By.XPATH, "//input[@placeholder='Enter first name']").send_keys("Anna")
    browser.find_element(By.XPATH, "//input[@placeholder='Enter last name']").send_keys("Smitt")
    browser.find_element(By.XPATH, "//input[@placeholder='Enter email']").send_keys("qwerty@gmail.com")
    file_button = browser.find_element(By.XPATH, "//input[@id='file']")

    path_file = os.path.abspath(os.path.dirname(__file__))

    file_path = os.path.join(path_file, 'less_2.2_step_8.txt')
    file_button.send_keys(file_path)
    browser.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()

    time.sleep(10)
