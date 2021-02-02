from selenium import webdriver
# = str(input("Enter value a: "))
#user_input_b = str(input("Enter value b: "))
chrome_browser = webdriver.Chrome("./chromedriver")

chrome_browser.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

button = chrome_browser.find_element_by_class_name("btn-default")
print(button.get_attribute("innerHTML"))

#chrome_browser.find_element_by_css_select("#get-input > .btn")
#user_msg = chrome_browser.find_element_by_id("user-message")
#user_msg.clear()
#user_msg.send_keys("Hi hello!")
#button.click()
#msg_display = chrome_browser.find_element_by_id("display")
#print(msg_display)
print(chrome_browser.find_element_by_id("gettotal"))

user_msg_a = chrome_browser.find_element_by_id("sum1")
user_msg_a.clear()
user_msg_a.send_keys("5")

user_msg_b = chrome_browser.find_element_by_id("sum2")
user_msg_b.clear()
user_msg_b.send_keys("5")

button_total = chrome_browser.find_element_by_class_name("btn btn_default")
button_total.click()

chrome_browser.quit()