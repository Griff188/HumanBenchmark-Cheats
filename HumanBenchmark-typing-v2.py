
import time
from selenium import webdriver

browser = webdriver.Chrome('\chromedriver.exe')
browser.get('https://www.humanbenchmark.com/tests/typing')

input("ready? ")

element = browser.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[1]/div/div[2]/div')
letters = browser.find_elements_by_xpath('/html/body/div[1]/div/div[4]/div[1]/div/div[2]/div')


letters = letters[0].text

print(letters)
element.send_keys(letters)

time.sleep(3)

browser.quit()
