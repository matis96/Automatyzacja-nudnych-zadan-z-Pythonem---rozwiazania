# This Bot works with protonmail and Firefox webdriver

import sys, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

mail = sys.argv[1]
text = ' '.join(sys.argv[2:])
browser = webdriver.Firefox()
browser.get('https://account.proton.me/mail')       #open webpage
time.sleep(5)

#send user id and password
userElem = browser.find_element('id', 'username')
userElem.send_keys('')        #Fill here your email adress
passElem = browser.find_element('id', 'password')
passElem.send_keys('')        # Fill here your password
passElem.submit()

#open new message
time.sleep(25)
htmlElem = browser.find_element('tag name', 'html')
htmlElem.send_keys('N')     #pm.me feature

time.sleep(10)
mailElem = browser.find_element('xpath', "//*[starts-with(@id, 'to-composer')]")
mailElem.send_keys(mail)
subjElem = browser.find_element('xpath', "//*[starts-with(@id, 'subject-composer')]")
subjElem.send_keys('Mail wyslany przez Bota napisanego w Pythonie')        # topic 
textElem = browser.find_element('tag name', 'textarea')

#delete protonmail Post Scriptum
info_len = len('Sent with Proton Mail secure email.')
for i in range(info_len+5):
    textElem.send_keys(Keys.BACK_SPACE)
textElem.send_keys(text)
textElem.send_keys(Keys.CONTROL, Keys.ENTER)
#print(text)
