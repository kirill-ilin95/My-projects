from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_css_selector('[placeholder="Input your first name"]').send_keys("Kirill")
    browser.find_element_by_css_selector('[placeholder="Input your last name"]').send_keys("Ilin")
    browser.find_element_by_css_selector('[placeholder="Input your email"]').send_keys("asus7783905@gmail.com")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(2)
    browser.quit()