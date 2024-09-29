import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

timeout = time.time() + 3*60      #timeout

browser = webdriver.Firefox()
browser.get('https://play2048.co/')
time.sleep(5)

buttonCookie = browser.find_element('id', 'ez-accept-all')
buttonCookie.click()

htmlElem = browser.find_element('tag name', 'html')

while(True):
    htmlElem.send_keys(Keys.UP)
    time.sleep(0.5)
    htmlElem.send_keys(Keys.RIGHT)
    time.sleep(0.5)
    htmlElem.send_keys(Keys.DOWN)
    time.sleep(0.5)
    htmlElem.send_keys(Keys.LEFT)
    time.sleep(0.5)
    if time.time() > timeout:
        break

htmlElem.send_keys(Keys.HOME)
