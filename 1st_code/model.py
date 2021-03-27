'''
    Our Model class
    This should control the actual "logic" of your website
    And nicely abstracts away the program logic from your page loading
    It should exist as a separate layer to any database or data structure that you might be using
    Nothing here should be stateful, if it's stateful let the database handle it
'''
import view
import random
import sqlite3
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
   
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute("SELECT username FROM user")
    
    userlist= [item[0] for item in c.fetchall()]
    if username not in userlist:
        c.execute("INSERT INTO user(username, password) VALUES (?,?)", (username, password))
        conn.commit()
        c.close()
        return '<p>The user was inserted into the database</p>' 
    if username in userlist:
        return '<p>The user already exsits in the database</p>' 

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
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute("SELECT 1 FROM user WHERE username = ? and password =?", (username,password))
    cur_data = c.fetchone()
   
    login = True
    
    if  not cur_data:
        err_str = "Incorrect :("
        login = False
    
        
    if login:
        global cur_username
        cur_username = username
        #change the cur_username to global variable
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
    return page_view("profile", cur_name=cur_username)

def update(old, new):
    '''
        update
        update the password of users

        :: username :: The username
        :: password :: The password

        Returns either a view for valid credentials, or a view for invalid credentials
    '''
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute("SELECT * FROM user WHERE password=? AND username=?", (old, cur_username))
    print(cur_username)
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