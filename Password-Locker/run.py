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