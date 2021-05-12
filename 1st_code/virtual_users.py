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

driver = webdriver.Chrome(options=chrome_options, executable_path=PATH)
driver.get(url)

home_button = driver.find_element_by_xpath("/html/body/ul/li[1]/a")
login_button = driver.find_element_by_xpath("/html/body/ul/li[2]/a")
about_button = driver.find_element_by_xpath("/html/body/ul/li[3]/a")
profile_button = driver.find_element_by_xpath("/html/body/ul/li[4]/a")
tutorial_button = driver.find_element_by_xpath("/html/body/ul/li[5]/a")


def tourist(driver):
    print("I'm a tourist who hasn't registered yet")
    print("I should have the access to all tutorial content, and home page and discussion page, but I can't post anything on discussion")

    # click home button to start
    print("ready to print button")
    home_button.click()
    print("home button printed, new at home page")

    # now go to login page, try random username and password
    print("going to type smth special")
    login_button.click()
    print("try click login without typing anything")
    login = driver.find_element_by_xpath("/html/body/form/input[3]")
    login.click()
    back_to_login = driver.find_element_by_xpath("/html/body/p[4]/a")
    back_to_login.click()

    

    
def user():
    print("fist login, then look through the tutorial page, then ")

def admin():
    print("login as admin")

if __name__ == '__main__':

    x = random.randint(1,3)
    if x == 1:
        tourist()
    elif x == 2:
        user()
    elif x == 3:
        admin()

    """ to test driver is set properly  """
    print(driver.page_source.encode("utf-8"))

    driver.quit()
    print("finished")
