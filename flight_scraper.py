import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
# selenium 4
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# options:
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
#chrome to stay open
options.add_experimental_option("detach", True)

# which drivercommand is it?
# driver = webdriver.Chrome()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
# url = 'https://www.kayak.ch/flights/ZRH,BSL,GVA-KGL/2024-07-11/2students?sort=bestflight_a' # option to add more

#try if this works, add list as to location --> loop over
to_location = 'KGL'
url = 'https://www.kayak.ch/flights/ZRH,BSL,GVA-{to_location}/2024-07-11/2students?sort=bestflight_a'.format(to_location=to_location)

driver.get(url)


popup_path = '//*[@id="portal-container"]/div/div[2]/div/div/div[1]/div/span[2]/button'
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, popup_path))).click()