import requests
import time
import getpass
import selenium
import time
import sys
import csv
import random

from selenium import webdriver

#------------------------------------------------

url = "http://10.86.227.4:8080/"
PATH = "home/hr/info2222_2021_Team4/1st_code/chromedriver"

#------------------------------------------------
# Useage: 
# python canvas_group_scraper.py <target groups page>
#------------------------------------------------
class VirtualUser():

    def tourist():
        print("I'm a tourist who hasn't registered yet")
        print("I should have the access to all tutorial content, and home page and discussion page, but I can't post anything on discussion")
        

if __name__ == '__main__':

    driver = webdriver.Chrome(PATH)
    driver.get(url)

    print("finished")
