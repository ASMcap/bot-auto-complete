from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#username and password
usernameStr = 'Put here youre username '
passwordStr = 'Put here youre password'

#auto execute driver
browser = webdriver.Chrome()
browser.get(('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'))

#get id element to auto complete
username = browser.find_element_by_id('identifierId')
username.send_keys(usernameStr)

#auto click next button
nextButton = browser.find_element_by_id('identifierNext')
nextButton.click()

#get id element to auto complete
password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'Password')))
password.send_keys(passwordStr)

#auto click next button 
signInButton = browser.find_element_by_id('passwordNext')
signInButton.click()

