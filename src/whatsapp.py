#importing modules
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

#setting options for drivers
options = webdriver.ChromeOptions()
options.add_argument(r'--user-data-dir=C:\Users\admin\AppData\Local\Google\Chrome\User Data\Default')
options.add_argument('--profile-directory=Default')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_browser = webdriver.Chrome(executable_path=r'C:\Users\admin\Downloads\chromedriver.exe',options=options)      

#register status listener on given phone number
def registerListener(phone):
    chrome_browser.get('https://web.whatsapp.com/send?phone=91${}'.format(phone))
    time.sleep(10)

def getStatus():
    try:
        element = chrome_browser.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/header/div[2]/div[2]/span')
        return element.text
    except NoSuchElementException:
        return 'offline'