import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://w3.acumulepontosdeviagem.com/d224e55a-8d95-11ea-ba74-de1c0c70a00b/aapf/login.jsp')
time.sleep(2)

agc_input = driver.find_element_by_xpath('/html/body/div/section/div/div/div[2]/form/div[1]/input') #agencia input
agc_input.click()
agc_input.send_keys("0953")
cnt_input = driver.find_element_by_xpath('/html/body/div/section/div/div/div[2]/form/div[2]/input') #bank account input
cnt_input.click()
cnt_input.send_keys("10221654")
pwd_input = driver.find_element_by_xpath('/html/body/div/section/div/div/div[2]/form/div[3]/input') # password input
pwd_input.click()
pwd_input.send_keys("147852963")


data_submt = driver.find_element_by_xpath('/html/body/div/section/div/div/div[2]/form/button').send_keys(Keys.ENTER) # btn submit 

time.sleep(10)

driver.close()
#driver.find_element_by_xpath("agc_input").click()
#driver.find_element_by_xpath("agc_input").send_keys("teste01")
#driver.find_element_by_xpath("cnt_input").send_keys("teste01")
#driver.find_element_by_xpath("pwd_input").send_keys("teste01")

