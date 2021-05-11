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

target_url = "https://canvas.sydney.edu.au/courses/30588/groups#tab-6293"
PATH = "/mnt/c/Users/82751/Documents/2021 S1/INFO2222/lec slides/security/set1/chromedriver.exe"

#------------------------------------------------
# Useage: 
# python canvas_group_scraper.py <target groups page>
#------------------------------------------------
class VirtualUser():

    def tourist():
        print("I'm a tourist who hasn't registered yet")
        print("I should have the access to all tutorial content, and home page and discussion page, but I can't post anything on discussion")
        

if __name__ == '__main__':
    while True:
        x = random.randint(1,3)
        print(x)
    print("finished")
