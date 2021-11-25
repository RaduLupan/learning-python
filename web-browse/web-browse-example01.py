from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")

message_field = driver.find_element(By.XPATH, '//*[@id="user-message"]')
message_field.send_keys('Hello World!')

show_message_button = driver.find_element(By.XPATH, '//*[@id="get-input"]/button')
show_message_button.click()

message_field_a = driver.find_element(By.XPATH, '//*[@id="sum1"]')
message_field_a.send_keys('25')

message_field_b = driver.find_element(By.XPATH, '//*[@id="sum2"]')
message_field_b.send_keys('50')

get_total_button = driver.find_element(By.XPATH, '//*[@id="gettotal"]/button')
get_total_button.click()

