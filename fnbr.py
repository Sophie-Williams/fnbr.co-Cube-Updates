from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

while True:
    print('\n'*50)
    try:
        print('Loading webdriver')
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')

        sel = webdriver.Chrome(chrome_options=options)
    except:
        print('An error occurred loading the webdriver.')
    try:
        print('Loading website.')
        sel.get('http://fnbr.co/cube')
        print('Grabbing time left.\n')
        print('Time until next movement: ' + sel.find_element_by_xpath('/html/body/main/div/h2').text)
        print('\nURL for image: https://image.fnbr.co/cube.jpg')
    except:
        print('An error occurred while loading the website. ')

    try:
        print('Closing browser. Loading again in 10 seconds')
        sel.close()
    except:
        print('An error occurred.')
    time.sleep(10)
