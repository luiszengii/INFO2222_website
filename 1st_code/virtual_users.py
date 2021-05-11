import requests
import time
import getpass
import selenium
import time
import sys
import csv
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
#------------------------------------------------

url = "http://10.86.227.4:8080/"
PATH = "/home/rh/info2222_2021_Team4/1st_code/chromedriver"
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")

class VirtualUser():

    def tourist():
        print("I'm a tourist who hasn't registered yet")
        print("I should have the access to all tutorial content, and home page and discussion page, but I can't post anything on discussion")
        

if __name__ == '__main__':

    # x = random.randint(1,3)
    # if x == 1:
    #     VirtualUser.tourist()
    # elif x == 2:
    #     VirtualUser.user()
    # elif x == 3:
    #     VirtualUser.admin()

    driver = webdriver.Chrome(options=chrome_options, executable_path=PATH)
    driver.get(url)

    """ to test driver is set properly  """
    print(driver.page_source.encode("utf-8"))

    driver.quit()
    print("finished")
