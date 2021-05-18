'''
    Our Model class
    This should control the actual "logic" of your website
    And nicely abstracts away the program logic from your page loading
    It should exist as a separate layer to any database or data structure that you might be using
    Nothing here should be stateful, if it's stateful let the database handle it
'''
from os import close
from sqlite3.dbapi2 import complete_statement
from string import Template
from bottle import template
import view
import controller
import random
import sqlite3
import bottle
from bottle import *
# Initialise our views, all arguments are defaults for the template
page_view = view.View()
# Initialise a variable which is the current user name, the default one is "tourist"
cur_username = "tourist"

#-----------------------------------------------------------------------------
# Index
#-----------------------------------------------------------------------------

def index():
    '''
        index
        Returns the view for the index
    '''
    return page_view("index")

#-----------------------------------------------------------------------------
# Login
#-----------------------------------------------------------------------------

def login_form():
    '''
        login_form
        Returns the view for the login_form
    '''
    return page_view("login")

#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
# register
#-----------------------------------------------------------------------------

def register_form():
    '''
       register_form
        Returns the view for the register_form
    '''
    return page_view("register")

#-----------------------------------------------------------------------------
def register(username, password):
   
    conn = sqlite3.connect('/home/app/user.db')
    c = conn.cursor()
    c.execute("SELECT username FROM user")
    
    userlist= [item[0] for item in c.fetchall()]
    if username not in userlist:
        c.execute("INSERT INTO user(username, password) VALUES (?,?)", (username, password))
        conn.commit()
        c.close()
        return '''<style>
    	      p {text-align: center;}
                      form {text-align: center;}
                      </style><p>The user was inserted into the database</p>
                      <p><a href="/login">go to login page</a></p>'''
    if username in userlist:
        return '''<style>
    	      p {text-align: center;}
                      form {text-align: center;}
                      </style>
	      <p>The user already exsits in the database</p>
	      <p><a href="/register">go back to register page</a></p>'''

#--------------------------------------------------------------------------
# Check the login credentials
def login_check(username, password):
    '''
        login_check
        Checks usernames and passwords

        :: username :: The username
        :: password :: The password

        Returns either a view for valid credentials, or a view for invalid credentials
    '''
    conn = sqlite3.connect('/home/app/user.db')
    c = conn.cursor()
    c.execute("SELECT 1 FROM user WHERE username = ? and password =?", (username,password))
    cur_data = c.fetchone()
   
    login = True
    
    if not cur_data:
        err_str = "Incorrect :("
        login = False
    
    if login:
        """ send a cookie to client storing the username and a valid login """
        cur_username = username
        # if already logged in do not perform login again
        if request.get_cookie("loggedIn"):
            return page_view("invalid", reason="already logged in as" + username + "!!!")
        else:
            response.set_cookie("loggedIn", "yes")
            response.set_cookie("username", username)
            return page_view("valid", name=username)
    else:
        return page_view("invalid", reason=err_str)

#-----------------------------------------------------------------------------
# About
#-----------------------------------------------------------------------------

def about():
    '''
        about
        Returns the view for the about page
    '''
    return page_view("about", garble=about_garble())



# Returns a random string each time
def about_garble():
    '''
        about_garble
        Returns one of several strings for the about page
    '''
    garble = ["leverage agile frameworks to provide a robust synopsis for high level overviews.", 
    "iterate approaches to corporate strategy and foster collaborative thinking to further the overall value proposition.",
    "organically grow the holistic world view of disruptive innovation via workplace change management and empowerment.",
    "bring to the table win-win survival strategies to ensure proactive and progressive competitive domination.",
    "ensure the end of the day advancement, a new normal that has evolved from epistemic management approaches and is on the runway towards a streamlined cloud solution.",
    "provide user generated content in real-time will have multiple touchpoints for offshoring."]
    return garble[random.randint(0, len(garble) - 1)]

#-----------------------------------------------------------------------------
# Profile
#-----------------------------------------------------------------------------

def profile():
    '''
        about
        Returns the view for the user profile page
    '''
    conn = sqlite3.connect('/home/app/user.db')
    c = conn.cursor()
    c.execute("SELECT admin,mute FROM user WHERE username = ?", (cur_username,))
    cur_data = c.fetchone()
    if cur_data is None:
        return page_view("profile", cur_name=cur_username, mute = "Normal")
    if cur_data[0] == 1:
        return page_view("admin", cur_name=cur_username)
    else:
        if (cur_data[1] == 1):
            return page_view("profile", cur_name=cur_username, mute = "Muted")
        elif (cur_data[1] == 0):
            return page_view("profile", cur_name=cur_username, mute = "Normal")

def get_username():
    # returns the name
    # first check if is muted
    conn = sqlite3.connect('/home/app/user.db')
    c = conn.cursor()
    c.execute("SELECT mute FROM user WHERE username = ?", (cur_username,))
    cur_data = c.fetchone()

    if cur_data is None:
        return "tourist"
    elif cur_data[0] == 1:
        return "muted"

    return cur_username
    

def update(old, new):
    '''
        update
        update the password of users

        :: username :: The username
        :: password :: The password

        Returns either a view for valid credentials, or a view for invalid credentials
    '''
    conn = sqlite3.connect('/home/app/user.db')
    c = conn.cursor()
    c.execute("SELECT * FROM user WHERE password=? AND username=?", (old, cur_username))
    cur_data = c.fetchone()

    if cur_data is None:
        return page_view("update_failture1")
    else:
        c.execute("UPDATE user SET password = ? WHERE password = ?", (new, old))
        conn.commit()
        c.close()
        return page_view("update_success")

def update_failture():
    return page_view("update_failture2")


#-----------------------------------------------------------------------------
# Debug
#-----------------------------------------------------------------------------

def debug(cmd):
    try:
        return str(eval(cmd))
    except:
        pass


#-----------------------------------------------------------------------------
# 404
# Custom 404 error page
#-----------------------------------------------------------------------------

# def handle_errors(error):
#     error_type = error.status_line
#     error_msg = error.body
#     return page_view("error", error_type=error_type, error_msg=error_msg)

#-----------------------------------------------------------------------------
# Tutorial
#-----------------------------------------------------------------------------
def tut():
    # returns the view for tutorial page
    return page_view("tut")
#-----------------------------------------------------------------------------
# Discussion Board
#-----------------------------------------------------------------------------
def discussion():
    # returns the view for tutorial page
    return page_view("discussion")
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Admin
#-----------------------------------------------------------------------------
# def admin():
#     return page_view("admin", cur_name=cur_username)

def user_list():
    conn = sqlite3.connect('/home/app/user.db')
    c = conn.cursor()
    c.execute("SELECT username FROM user")
    cur_data = c.fetchall()
    list = []
    for a in cur_data:
        list.append(a[0])
    return list

def add_user(new_name):
    conn = sqlite3.connect('/home/app/user.db')
    c = conn.cursor()
    c.execute("SELECT username FROM user")
    
    userlist= [item[0] for item in c.fetchall()]
    if new_name in userlist:
        return page_view("add_failure", name = new_name)
    else:
        c.execute("INSERT INTO user(username, password) VALUES (?,?)", (new_name, 123))
        conn.commit()
        conn.close()
        return page_view("add_success", name = new_name)

def delete_user(delete_name):
    conn = sqlite3.connect('/home/app/user.db')
    c = conn.cursor()
    c.execute("SELECT username FROM user")
    
    userlist= [item[0] for item in c.fetchall()]
    if delete_name not in userlist:
        return page_view("delete_failure", name = delete_name)
    else:
        c.execute("DELETE FROM user WHERE username = ?", (delete_name,))
        conn.commit()
        conn.close()
        return page_view("delete_success", name = delete_name)

def mute_user(mute_name):
    conn = sqlite3.connect('/home/app/user.db')
    c = conn.cursor()
    c.execute("SELECT username FROM user")
    
    userlist= [item[0] for item in c.fetchall()]
    if mute_name not in userlist:
        return page_view("mute_failure", name = mute_name)
    else:
        c.execute("UPDATE user SET mute = ? WHERE username = ?", (1, mute_name))
        conn.commit()
        conn.close()
        return page_view("mute_success", name = mute_name)

def unmute_user(unmute_name):
    conn = sqlite3.connect('/home/app/user.db')
    c = conn.cursor()
    c.execute("SELECT username FROM user")
    
    userlist= [item[0] for item in c.fetchall()]
    if unmute_name not in userlist:
        return page_view("unmute_failure", name = unmute_name)
    else:
        c.execute("UPDATE user SET mute = ? WHERE username = ?", (0, unmute_name))
        conn.commit()
        conn.close()
        return page_view("unmute_success", name = unmute_name)
#-----------------------------------------------------------------------------
# New Post
#-----------------------------------------------------------------------------
def post(post, category):

# first insert a new post
    conn = sqlite3.connect('/home/app/user.db')
    c = conn.cursor()
    c.execute("INSERT INTO discussion(username, txt, category) VALUES (?, ?, ?)", (cur_username, post, category))
    conn.commit()
    conn.close()

    # to get all the posts we fetched from user.db to the page of "discussion", the pass in variable is called dis_list, contains all posts
    # but because the page_view() only render html files, we have to directly call controller to return the html page
    return controller.get_discussion()
    # return page_view("discussion", dis_list=dis_list)


#-----------------------------------------------------------------------------
# clear discussion
# -----------------------------------------------------------------------------
def clear_discussion():
    conn = sqlite3.connect('/home/app/user.db')
    c = conn.cursor()
    c.execute("DELETE FROM discussion")
    conn.commit()
    conn.close()
    return controller.get_discussion()

#-----------------------------------------------------------------------------
# accessing all posts
#-----------------------------------------------------------------------------
def dis_list():
    conn = sqlite3.connect('/home/app/user.db')
    c = conn.cursor()
    c.execute("SELECT * FROM discussion")
    cur_data = c.fetchall()
    dis_list = []
    for e in cur_data:
        dis_list.append(e)

    conn.commit()
    conn.close()

    # then fetch all the post in user.db
    conn = sqlite3.connect('/home/app/user.db')
    c = conn.cursor()
    c.execute("SELECT * FROM discussion")
    cur_data = c.fetchall()
    print("all the post up to now: ", cur_data)
    conn.close()

    web_list = []
    html_list = []
    css_list = []
    js_list = []

    for elem in dis_list:
        if elem[2] == "web":
            web_list.append(elem)
        elif elem[2] == "html":
            html_list.append(elem)
        elif elem[2] == "css":
            css_list.append(elem)
        elif elem[2] == "js":
            js_list.append(elem)

    list_of_all = [web_list, html_list, css_list, js_list]
    print(list_of_all)

    return list_of_all
    

