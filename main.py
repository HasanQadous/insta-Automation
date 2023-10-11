from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import ElementClickInterceptedException
import time

username = "0777142703"
password = "Ha$n1998"
similar_account = ""
url = "https://www.instagram.com/accounts/login/"


class InstaBot:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get(url)
        time.sleep(5)
        user = self.driver.find_element(By.XPATH, "//input[@aria-label='Phone number, username, or email']")
        user.send_keys(username)

        passwordi = self.driver.find_element(By.XPATH, '//input[@aria-label="Password"]')
        passwordi.send_keys(password)
        passwordi.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(10)
        self.driver.get("https://www.instagram.com/realmadrid/")
        time.sleep(3)
        followers_button = self.driver.find_element(By.XPATH, "//a[text()=' followers']")
        followers_button.click()
        time.sleep(5)
        modal = self.driver.find_element(By.XPATH, '//div[@class="_aano"]')
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        time.sleep(2)
        self.driver.quit()

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaBot()
bot.login()
bot.find_followers()
bot.follow()