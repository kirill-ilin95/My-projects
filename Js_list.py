from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
driver = webdriver.Chrome()
try:

    driver.get(link)
    select = Select(driver.find_element_by_tag_name("select"))
    select.select_by_value("1")  # ищем элемент с текстом "Python"
    driver.find_element_by_css_selector(".btn.btn-default").click()

finally:
    time.sleep(5)
    driver.quit()