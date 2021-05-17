from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"
driver = webdriver.Chrome()

try:
    driver.get(link)
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = driver.find_element_by_id("treasure").get_attribute("valuex")
    x = x_element
    y = calc(x)
    driver.find_element_by_css_selector("#answer").send_keys(y)
    driver.find_element_by_css_selector("#robotCheckbox").click()
    driver.find_element_by_css_selector("#robotsRule").click()
    driver.find_element_by_css_selector(".btn.btn-default").click()
finally:
    time.sleep(15)
    driver.quit()

