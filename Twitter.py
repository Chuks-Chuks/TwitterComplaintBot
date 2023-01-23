from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import os
import dotenv


def click(action):
    sleep(5)
    action.click()


class Twitter:
    def __init__(self):
        self.path = os.path.expanduser('../TwitterComplaintBot')
        dotenv.load_dotenv(os.path.join(self.path, '.env'))

        self.driver_location = "c:/Development/chromedriver.exe"
        self.ser = Service(self.driver_location)
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)

        self.browser = webdriver.Chrome(service=self.ser, options=self.chrome_options)

        self.url = "https://www.twitter.com"
        self.browser.get(self.url)
        self.browser.maximize_window()
        self.login()

    def login(self):
        sleep(3)
        # To accept all the cookies
        i_accept = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[2]/div/div'
                                                       '/div/div[2]/div[1]/div/span/span')
        click(i_accept)

        sleep(5)
        login = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[1]/div/div'
                                                    '/div/div/div[2]/div/div/div[1]/a/div/span/span')
        click(login)

        sleep(10)
        # To input my username
        username = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div'
                                                       '/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label'
                                                       '/div/div[2]/div/input')
        username.send_keys(os.getenv('TWITTER_USERNAME') + Keys.ENTER)

        sleep(10)
        # To fill password
        password = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div'
                                                       '/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div'
                                                       '/label/div/div[2]/div[1]/input')
        password.send_keys(os.getenv('TWITTER_PASSWORD') + Keys.ENTER)

        sleep(5)
        whats_happening = self.browser.find_element(By.CSS_SELECTOR, '.public-DraftEditorPlaceholder-root div')
        print(whats_happening.text)
        sleep(5)

    def tweet(self, message):
        sleep(5)

        text_input = self.browser.find_element(By.CSS_SELECTOR, '.public-DraftStyleDefault-block')
        # click(text_input)
        sleep(3)
        text_input.send_keys(message)
        tweet_button = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div'
                                                           '/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]'
                                                           '/div[3]/div/div/div[2]/div[3]/div/span/span')
        click(tweet_button)


# twi = Twitter()
# # twi.tweet('this tweet was made using code xx')
