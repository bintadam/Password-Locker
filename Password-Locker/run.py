#!/usr/bin/env python3.8

from password import User
from credential import credentials

def create_account(username, password):
    '''
    Function to create a new user
    '''
    new_user = User(username, password)
    return new_user

def save_account():
    '''
    Function to save user
    '''
    user.save_user() 

def create_credentials(username, password, account):
    '''
    Function to create a new credentials
    '''
    new_credentials = credentials(username, password, account)
    return new_credentials    

def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()    

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

def display_credential():
    '''
    Function that returns all the saved credentials
    '''
    return credentials.display_credentials()

def log_in(user, password):
    '''
    Function to log in users
    '''
    verified_user = User.verified_users(user, password)
    return verified_user

def generatepassword(stringLength=8):
    '''
    generate a strong random password consisting of string of letters and digits and special characters
    '''
    string.ascii_lowercase + string.digits + "!~#@$%&*^"
    return ''.join(random.choice(password))
    
    


    
      