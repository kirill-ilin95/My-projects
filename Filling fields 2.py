from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/huge_form.html")
elements = browser.find_elements_by_css_selector("[maxlength='32']")
for element in elements:
        element.send_keys("Kirill")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

time.sleep(5)
browser.quit()