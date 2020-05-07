import time
from selenium import webdriver


constUrl = "www.google.com"

mobile_emulation = { "deviceName": "Nexus 5" }
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome('/home/hiraki/Desktop/projects/fill-form/chromedriver')  # Optional argument, if not specified will search path.
driver.get(constUrl);
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()