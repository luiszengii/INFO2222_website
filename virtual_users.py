import requests
import time
import getpass
import selenium
import time
import sys
import csv

from selenium import webdriver

#------------------------------------------------

default_target = "https://canvas.sydney.edu.au/courses/30588/groups#tab-6293"
PATH = "/mnt/c/Users/82751/Documents/2021 S1/INFO2222/lec slides/security/set1/chromedriver.exe"

#------------------------------------------------
# Useage: 
# python canvas_group_scraper.py <target groups page>
#------------------------------------------------


def scrape(target):

    driver = webdriver.Chrome(PATH)
    groups = {}


    print("Canvas login creds:")

    print("Loading login portal")
    driver.get("https://canvas.sydney.edu.au/")

    username = input("Enter your canvas username: ")
    password = getpass.getpass() # getpass 输入密码不会显示在

    print("Logging in")

    time.sleep(2)

    # Enter username
    username_field = driver.find_element_by_name("username")
    username_field.clear()
    username_field.send_keys(username)

    # Enter password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)

    # Hit the button
    login_button = driver.find_element_by_id("okta-signin-submit")
    login_button.click()

    time.sleep(2)

    print("Logged in!")
    time.sleep(10)

    driver.get(target)

    for group in range(1, 50):
        try:
            # Click to expand group header
            group_xpath = '//*[@class="span9 groups"]//div//ul//li[{group}]//div//div//a'
            group_heading = driver.find_element_by_xpath(group_xpath.format(group=group))
            group_name = group_heading.text
            group_heading.click()

            groups[group_name] = []

            # Get members from group
            for member in range(1,6):
                try:
                    member_xpath = '//*[@class="span9 groups"]//div//ul//li[{group}]//div[2]//ul//li[{member}]//div'
                    member_name = driver.find_element_by_xpath(member_xpath.format(group=group, member=member)).text 

                    groups[group_name].append(member_name)
                except:
                    print("Member not found")

            print("Group: {} contains {}".format(group_name, groups[group_name].__repr__()) )
        except:
            print("cannot find any group")
            pass

        

    print("Scraping finished, closing web driver.")
    return groups


#------------------------------------------------

def csv_groups(groups):
    with open('groups.csv', 'w') as groups_file:
        csv_writer = csv.writer(groups_file) 
        for count, group in enumerate(groups):
            if len(groups[group]) > 0:
                for member in groups[group]:
                    group_line = ['group_{}'.format(count ), member]
                    csv_writer.writerow(group_line)
    print("CSV written")
    return

#------------------------------------------------

if __name__ == '__main__':
    # allow user to specify its own target
    if len(sys.argv) == 1:
        target_url = default_target
    else:
        target_url = sys.argv[1]

    # first get all members and then make them into a csv file
    groups = scrape(target_url)
    csv_groups(groups)


print("Finished!")
