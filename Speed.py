import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import os
import dotenv


def click(action):
    time.sleep(5)
    action.click()


path = os.path.expanduser('../TwitterComplaintBot')
dotenv.load_dotenv(os.path.join(path, '.env'))


class Speed:
    def __init__(self):
        self.driver_location = "c:/Development/chromedriver.exe"
        self.ser = Service(self.driver_location)
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)

        self.browser = webdriver.Chrome(service=self.ser, options=self.chrome_options)

        self.url = "https://www.speedtest.net/"
        self.browser.get(self.url)
        self.browser.maximize_window()
        # self.run_test()

    # To click the I accept button
    def run_test(self):
        """Performs a speed test and returns the download and upload speeds as a list object. The first element is the
        download speed and the second is the upload speed."""
        time.sleep(3)
        i_accept = self.browser.find_element(By.ID, 'onetrust-accept-btn-handler')
        click(i_accept)

        # To click on the GO button:
        time.sleep(10)
        go_button = self.browser.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/'
                                                        'div[1]/a/span[4]')
        click(go_button)

        time.sleep(47)

        internet_speed = self.browser.find_elements(By.CSS_SELECTOR, '.u-align-left span')
        internet_speeds = [t.text for t in internet_speed]
        print(internet_speeds)
        return internet_speeds


