
import time
from selenium import webdriver

# open chrome to benchmark page
browser = webdriver.Chrome('\chromedriver.exe')
browser.get('https://www.humanbenchmark.com/tests/typing')


input("ready? ")

# grab text box element 
element = browser.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[1]/div/div[2]/div')

# grab all elements within the text box
# this is needed as a separate .find because each letter is in its own element 
letters = browser.find_elements_by_xpath('/html/body/div[1]/div/div[4]/div[1]/div/div[2]/div')

# turn element into string
letters = letters[0].text

# print it out and send it to textbox
print(letters)
element.send_keys(letters)


# uncomment to have browser close after completion   
# time.sleep(3)
# browser.quit()
