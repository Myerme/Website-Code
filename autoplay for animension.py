from re import search
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(path)

driver.get("https://animension.to/")
print(driver.title)

search = driver.find_element_by_class_name("search-live")
search.send_keys("naruto")
search.send_keys(Keys.RETURN)

driver.maximize_window()
time.sleep(10)
driver.find_element_by_link_text("Naruto Dubbed")



time.sleep(500)
driver.quit()