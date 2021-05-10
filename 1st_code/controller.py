'''
    This file will handle our typical Bottle requests and responses 
    You should not have anything beyond basic page loads, handling forms and 
    maybe some simple program logic
'''

from os import curdir
from bottle import route, get, post, error, request, static_file, template

import model

#-----------------------------------------------------------------------------
# Static file paths
#-----------------------------------------------------------------------------

# Allow image loading
@route('/img/<picture:path>')
def serve_pictures(picture):
    '''
        serve_pictures

        Serves images from static/img/

        :: picture :: A path to the requested picture

        Returns a static file object containing the requested picture
    '''
    return static_file(picture, root='/home/rh/info2222_2021_Team4/1st_code/static/img/')

#-----------------------------------------------------------------------------

# Allow CSS
@route('/css/<css:path>')
def serve_css(css):
    '''
        serve_css

        Serves css from static/css/

        :: css :: A path to the requested css

        Returns a static file object containing the requested css
    '''
    return static_file(css, root='/home/rh/info2222_2021_Team4/1st_code/static/css/')

#-----------------------------------------------------------------------------

# Allow javascript
@route('/js/<js:path>')
def serve_js(js):
    '''
        serve_js

        Serves js from static/js/

        :: js :: A path to the requested javascript

        Returns a static file object containing the requested javascript
    '''
    return static_file(js, root='/home/rh/info2222_2021_Team4/1st_code/static/js/')

#-----------------------------------------------------------------------------
# Pages
#-----------------------------------------------------------------------------

# Redirect to login
@get('/')
@get('/home')
def get_index():
    '''
        get_index
        
        Serves the index page
    '''
    return model.index()

#-----------------------------------------------------------------------------

# Display the login page
@get('/login')
def get_login_controller():
    '''
        get_login
        
        Serves the login page
    '''
    return model.login_form()

#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------

# Display the register page
@get('/register')
def get_register_controller():
    '''
        get_register
        
        Serves the registerpage
    '''
    return model.register_form()

#-----------------------------------------------------------------------------
# Attempt the login
@post('/login')
def post_login():
    '''
        post_login
        
        Handles login attempts
        Expects a form containing 'username' and 'password' fields
    '''

    # Handle the form processing
    username = request.forms.get('username')
    password = request.forms.get('password')
    
    # Call the appropriate method
    return model.login_check(username, password)

#-----------------------------------------------------------------------------
# Post a new psot
@post('/post_discussion')
def post_discussion():

    # Handle the form processing, username in model.py
    post = request.forms.get('post')
    category = request.forms.get('category')

    if len(post) > 254:
        return template('/home/rh/info2222_2021_Team4/1st_code/templates/post_failed.tpl')

    return model.post(post, category)


#-----------------------------------------------------------------------------

@post('/register')
def post_register():
    '''
        post_register
        
    '''

    # Handle the form processing
    username = request.forms.get('username')
    password = request.forms.get('password')
    cpassword = request.forms.get('confirm password')
    # Call the appropriate method
    if password == cpassword:
        return model.register(username, password)
    if password != cpassword:
        return '''<style>
    	      p {text-align: center;}
                      form {text-align: center;}
                      </style><p>The two passwords entered do not match </p>
 	     <p><a href="/register">back to register page</a></p>'''



#-----------------------------------------------------------------------------
# Attempt to make a new post
@get('/try_new_post')
def try_new_post():
    '''
        will first check if the user has login
        then check if been muted
        if all conditions met make a new post box for the user
    '''
    cur_name = model.get_username()
    if cur_name == "tourist":
        return model.register_form()
    if cur_name == "muted":
        return template('/home/rh/info2222_2021_Team4/1st_code/templates/muted_message.tpl')
    else:
        return template('/home/rh/info2222_2021_Team4/1st_code/templates/new_post.tpl')

#-----------------------------------------------------------------------------
@get('/about')
def get_about():
    '''
        get_about
        
        Serves the about page
    '''
    return model.about()
#-----------------------------------------------------------------------------
# display the user profile page
@get('/profile')
def get_profile():
    '''
        get_profile
        
        Serves the profile page
    '''
    return model.profile()

# update the passward of users
@post('/profile_0')
def post_update():
    '''
        post_update
        
        Handles passward update attempts
    '''
    old_password = request.forms.get('old_password')
    new_password = request.forms.get('new_password')
    retype_password = request.forms.get('confirm_password')

    if new_password == retype_password:
        return model.update(old_password, new_password)
    else:
        return model.update_failure()



#-----------------------------------------------------------------------------
# Help with debugging
@post('/debug/<cmd:path>')
def post_debug(cmd):
    return model.debug(cmd)

#-----------------------------------------------------------------------------

# 404 errors, use the same trick for other types of errors
# @error(404)
# def error(error): 
#     return model.handle_errors(error)


#-----------------------------------------------------------------------------

@get('/tut')
def get_tut():
    '''
        get_tut
        
        Serves the tutorial page
    '''
    return model.tut()


#-----------------------------------------------------------------------------

@get('/user_list')
def get_user_list():
    '''
        get_user_list

        serves for getting users list
    '''

    return template('/home/rh/info2222_2021_Team4/1st_code/templates/user_list', user_list = model.user_list())

@post('/profile_1')
def add_user():
    added_user_name = request.forms.get('added_user')
    return model.add_user(added_user_name)

@post('/profile_2')
def delete_user():
    deleted_user_name = request.forms.get('deleted_user')
    return model.delete_user(deleted_user_name)

@post('/profile_3')
def mute_user():
    muted_user_name = request.forms.get('muted_user')
    return model.mute_user(muted_user_name)

@post('/profile_4')
def unmute_user():
    unmuted_user_name = request.forms.get('unmuted_user')
    return model.unmute_user(unmuted_user_name)
#-----------------------------------------------------------------------------
# delete all posts
#-----------------------------------------------------------------------------
@get('/clear_discussion')
def clear_discussion():
    return model.clear_discussion()

#-----------------------------------------------------------------------------
# accessing all posts
#-----------------------------------------------------------------------------

@get('/discussion')
def get_discussion():
    '''
        get_tut
        
        Serves the tutorial page
    '''
    return template('/home/rh/info2222_2021_Team4/1st_code/templates/discussions', dis_list=model.dis_list())