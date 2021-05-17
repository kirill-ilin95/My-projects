from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"

with webdriver.Chrome() as driver:
    driver.get(link)
    input1 = driver.find_element_by_name("first_name").send_keys("Kirill")
    input2 = driver.find_element_by_name("last_name").send_keys("Ilin")
    input3 = driver.find_element_by_css_selector(".form-control.city").send_keys("Kharkov")
    input4 = driver.find_element_by_id("country").send_keys("Ukraine")
    button = driver.find_element_by_xpath("/html/body/div/form/div[6]/button[3]").click()
    time.sleep(5)
