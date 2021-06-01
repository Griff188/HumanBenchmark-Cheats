import time

import pytesseract
from PIL import Image
from selenium import webdriver
import keyboard

pytesseract.pytesseract.tesseract_cmd = r"\Program Files\Tesseract-OCR\tesseract.exe"

# open to 2nd monitor
# (on my machine the screenshot bugs out on monitor #1 - typically, this argument can be left out)
driver = webdriver.ChromeOptions()
driver.add_argument('window-position=3000,0')

driver = webdriver.Chrome('\chromedriver.exe', options=driver)

try:
    # load site & open to full screen
    driver.get('https://humanbenchmark.com/tests/typing')
    driver.maximize_window()

    # time to sign-in
    input("ready? ")

    # take screenshot & get size of element
    element = driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div[2]/div')
    location = element.location
    size = element.size
    driver.save_screenshot("pageImage.png")

    # crop screenshot
    x = location['x']
    y = location['y']
    width = location['x'] + size['width']
    height = location['y'] + size['height']
    im = Image.open('pageImage.png')
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save('pageImage.png')

    # run image through tesseract OCR
    finishedText = pytesseract.image_to_string(Image.open("pageImage.png"), lang='eng+eng1')

    # set allowed characters for text to start with
    allowed = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # remove first character if it starts with unapproved character
    # this is done because OCR tends to represent cursor as a [ or | character
    if not any(finishedText.startswith(x) for x in allowed):
        finishedText = finishedText[1:(len(finishedText) - 1)]
    else:
        finishedText = finishedText[:(len(finishedText) - 1)]

    # split by line, and add a space at the end of each line
    # these may be unnecessary steps, but I ran into issues without it
    finishedText = finishedText.splitlines()
    finishedText = [item + " " for item in finishedText]

    # string processing for most common OCR errors
    finishedText = [w.replace('|', 'I') for w in finishedText]

    print(finishedText)

    # type modified text into webpage element
    element.send_keys(finishedText)

finally:
    time.sleep(30)
    driver.quit()
