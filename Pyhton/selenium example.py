from re import search
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://animekisa.tv/")
print(driver.title)

search = driver.find_element_by_name("q")
search.send_keys("naruto")
search.send_keys(Keys.RETURN)

driver.maximize_window()
time.sleep(10)
driver.find_element_by_link_text("Naruto Dubbed")



time.sleep(50)
driver.quit()

