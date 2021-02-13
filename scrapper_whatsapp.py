from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=/home/alberto/WebWhatsAppBot")

driver = webdriver.Chrome('/home/alberto/chromedriver', chrome_options=options)

driver.get("https://web.whatsapp.com/")

wait = WebDriverWait(driver, 600)

target = '"David Piso Valencia"'

string = "El asistente de voz te dice gilipollas tu"

x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((
	By.XPATH, x_arg)))
group_title.click()

message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]

message.click()

message.send_keys(string)

send_button_ref = '//*[@id="main"]/footer/div[1]/div[3]/button'

sendbutton = wait.until(EC.presence_of_all_elements_located((By.XPATH, send_button_ref)))[0]

sendbutton.click()