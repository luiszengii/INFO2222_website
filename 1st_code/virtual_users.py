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
register_button = driver.find_element_by_xpath("/html/body/p[9]/a")
about_button = driver.find_element_by_xpath("/html/body/ul/li[3]/a")
profile_button = driver.find_element_by_xpath("/html/body/ul/li[4]/a")
tutorial_button = driver.find_element_by_xpath("/html/body/ul/li[5]/a")


def tourist(driver):
    print("I'm a tourist who hasn't registered yet")
    print("I should have the access to all tutorial content, and home page and discussion page, but I can't post anything on discussion")

    # click home button to start
    print("ready to print button")
    home_button.click()
    print("home button printed, now at home page")

    # now go to login page, try random username and password
    print("going to type smth special")
    login_button.click()
    print("try click login without typing anything")
    login = driver.find_element_by_xpath("/html/body/form/input[3]")
    login.click()
    back_to_login = driver.find_element_by_xpath("/html/body/p[4]/a")
    back_to_login.click()

    

    
def user():
    print("I will regist as a user first then I can post and check my own profile")
    print("I will fist register, then log in, then look through the tutorial page, then go to profile page, then make some post")


    # click home button to start
    print("ready to print button")
    home_button.click()
    print("home button printed, now at home page")

    # now go to register page, create a new account
    print("going to register")
    login_button.click()
    register_button.click()
    print("try to create a new account")
    set_useranme = driver.find_element_by_xpath("/html/body/form/p[1]/input")
    set_username.send_keys("tester")
    set_password = driver.find_element_by_xpath("/html/body/form/p[2]/input")
    set_password.send_keys("tester1")
    set_confirm_password = driver.find_element_by_xpath("/html/body/form/p[3]/input")
    set_confirm_password.send_keys("tester1")
    driver.find_element_by_xpath("/html/body/form/p[5]/input").click()
    print("finish register")
    driver.find_element_by_xpath("/html/body/p[2]/a").click()
    print("come back to login")
    input_username = driver.find_element_by_xpath("/html/body/form/input[1]")
    input_username.send_keys("tester")
    input_password = driver.find_element_by_xpath("/html/body/form/input[2]")
    input_username.send_keys("tester1")
    driver.find_element_by_xpath("/html/body/form/input[3]").click()
    print("login successfully")

    # now go to tut page
    print("I will go through tut page")
    driver.find_element_by_xpath("/html/body/p[3]/a").click()
    print("I will try to jump to CSS part for example")
    driver.find_element_by_xpath("/html/body/ul[2]/li[3]/a").click()
    print("ohhhhhhhhhhh!It works")

    # now go to profile and tyr to change password
    print("I will go to see the profile")
    driver.find_element_by_xpath("/html/body/ul[1]/li[4]/a").click()
    print("now try to change password!")
    driver.find_element_by_xpath("/html/body/form/input[1]").send_keys("tester1")
    driver.find_element_by_xpath("/html/body/form/input[2]").send_keys("tester2")
    driver.find_element_by_xpath("/html/body/form/input[3]").send_keys("tester2")
    driver.find_element_by_xpath("/html/body/form/input[4]").click()
    print("okaaaaaaaaaaay!Then back to login an have a try")
    driver.find_element_by_xpath("/html/body/ul[1]/li[2]/a").click()
    driver.find_element_by_xpath("/html/body/form/input[1]").send_keys("tester")
    driver.find_element_by_xpath("/html/body/form/input[2]").send_keys("tester2")
    driver.find_element_by_xpath("/html/body/form/input[3]").click()
    print("ohhhhhhhhhhhh it works!")

    #now go to disccusion try to post sth
    print("now go to discussion")
    driver.find_element_by_xpath("/html/body/ul/li[6]/a").click()
    print("trying to post now!")
    driver.find_element_by_xpath("/html/body/form/button").click()
    driver.find_element_by_xpath("/html/body/div[1]/form/input").send_keys("Yifan is handsome")
    driver.find_element_by_xpath("/html/body/div[2]/select").click()
    print("post sth in CSS for example!")
    driver.find_element_by_xpath("/html/body/div[2]/select/option[3]").click()
    driver.find_element_by_xpath("/html/body/input").click()
    print("lets have a check")
    driver.find_element_by_xpath("/html/body/ul[2]/li[3]/a").click()
    print("woooooooooooooooooooooooooooooooow!")




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
