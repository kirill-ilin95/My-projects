from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/find_link_text"

with webdriver.Chrome() as driver:
    driver.get(link)
    link = driver.find_element_by_partial_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000))).click()
    input1 = driver.find_element_by_name("first_name").send_keys("Kirill")
    input2 = driver.find_element_by_name("last_name").send_keys("Ilin")
    input3 = driver.find_element_by_css_selector(".form-control.city").send_keys("Kharkov")
    input4 = driver.find_element_by_id("country").send_keys("Ukraine")
    button = driver.find_element_by_css_selector(".btn.btn-default").click()
    time.sleep(3)