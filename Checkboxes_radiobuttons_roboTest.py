from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/math.html"
driver = webdriver.Chrome()

try:
    driver.get(link)
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = driver.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    driver.find_element_by_css_selector("#answer").send_keys(y)
    driver.find_element_by_id("robotCheckbox").click()
    driver.find_element_by_id("robotsRule").click()
    driver.find_element_by_css_selector(".btn.btn-default").click()

finally:
    time.sleep(5)
    driver.quit()

