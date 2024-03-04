from time import sleep
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

import os

driver = webdriver.Chrome()

# url = 'https://www.kayak.ch/flights/ZRH,BSL,GVA-KGL/2024-07-11/2students?sort=bestflight_a' # option to add more

#try if this works, add list as to location --> loop over
to_location = 'KGL'
url = 'https://www.kayak.ch/flights/ZRH,BSL,GVA-{to_location}/2024-07-11/2students?sort=bestflight_a'.format(to_location=to_location)

driver.get(url)
sleep(10)

# pop_window = '//*[@id="portal-container"]/div/div[2]/div/div/div[3]/div/div[1]/button[3]/div'
popup_window = '//*[@id="portal-container"]/div/div[2]/div/div/div[1]/div/span[2]/button/'
driver.find_element(popup_window).click()

# noch keine möglichkeit gefunden, um die cookies zu schliessen, weil kein spezifischer xpath -->

# hier noch optionen drin zum anpassen, wie dass Seite nicht schliesst
# https://stackoverflow.com/questions/72835195/accept-bypass-cookies-with-selenium
