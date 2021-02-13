from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.by import By


def config_whatsapp_bot(home_directory):
    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=" + home_directory + "WebWhatsAppBot")

    global driver
    
    driver = webdriver.Chrome(home_directory + 'chromedriver', chrome_options=options)

    driver.get("https://web.whatsapp.com/")
    
    return driver
    
    
def define_contact_and_message(target, message_string):
    
    wait = WebDriverWait(driver, 600)

    x_arg = '//span[contains(@title,' + target + ')]'
    group_title = wait.until(EC.presence_of_element_located((
	    By.XPATH, x_arg)))
    group_title.click()
    
    send_message(message_string)

def send_message(message_string):
    wait = WebDriverWait(driver, 600)
    
    message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]

    message.click()

    message.send_keys(message_string)

    send_button_ref = '//*[@id="main"]/footer/div[1]/div[3]/button'

    sendbutton = wait.until(EC.presence_of_all_elements_located((By.XPATH, send_button_ref)))[0]

    sendbutton.click()
    
    
# config_whatsapp_bot("/home/alberto/")
# define_contact_and_message("'David Piso Valencia'", "Quieres pito?")