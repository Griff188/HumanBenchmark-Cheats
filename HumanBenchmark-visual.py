from PIL import ImageGrab
from pynput.mouse import Button, Controller
import time
from selenium import webdriver

# enter what level to go to
limit = input("go to level: ")
counter = 0

# default to level 20
try:
    limit = int(limit)
except:
    limit = 20

# print target level
print("going to", limit)

# define location of chrome driver and open new window to visual memory test
driver = webdriver.Chrome('\chromedriver.exe')
driver.get('https://www.humanbenchmark.com/tests/memory')
driver.maximize_window()

# time to sign-in
input("ready? ")

mouse = Controller()
image = None

# identify start button
start = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[1]/div/div/div/div[2]/button')

# for first run
if counter == 0:
    # mouse to center of the screen
    mouse.position = (440, 460)
    time.sleep(1)
    
    # click start
    start.click()
    counter += 1

time.sleep(1.5)

for level in range(0, limit):

    # take screenshot of box
    image = ImageGrab.grab(bbox=(750, 259, 1150, 659))
    image.save("screenshot" + str(level + 1) + ".png")

    time.sleep(1.1)

    # go through x, y coords
    for xSize in range(0, 400, 20):
        for ySize in range(0, 400, 20):

            # if white, click
            if image.getpixel((xSize, ySize)) == (255, 255, 255):
                mouse.position = (xSize + 750, ySize + 259)
            mouse.click(Button.left, 1)
            mouse.position = (440, 460)

    time.sleep(2)
