#!/usr/bin/env python3.8

import string
import random
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


def find_credential(account)
    '''
    Function to find credentials
    '''
    return credentials.find_by_account(account)


def createpassword(stringLength=10):
    '''
    generate a strong random password consisting of string of letters and digits and special characters
    '''
    string.ascii_lowercase + string.digits + "!~#@$%&*^"
    return ''.join(random.choice(password) for i in range(stringLength))


    
def main():
    print(" ")
    print("Hello Welcome, What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

     while True:
        print("-"*120)
        print
        ("Use these short codes : cc - create a new credentials, dc - display accounts, fc -find a credentials, cp -create password, dd - delete a credentials, lg - login to aacount, ex -exit the application ")

        short_code = input().lower()
        if short_code == 'cc':

           print("")
           print("-" * 120)

           print("New Credential")
           print(" ")

           print ("what username would you like to use? ")
           print("")
                            
           name = input().lower()
           print("what is the account name?")
           print("")

           user_name = input.lower()
           print("what is the account password?")
           print("")

           pass_word = input.lower()
           save_user(create_account(name, user_name)) # create and save account.
           print ('\n')

           save_credentials(create_credentials(name, user_name, pass_word, pass_word)) # create and save new credentials.
           print ('\n')
           print("" * 90)
                            
           print(f"New account {name} {user_name} created")
           print ('\n')

        elif short_code == 'dc':

            if display_users():
                print(" ")
                print("User name")
                print(" ")
                print('\n')

                for user in display_users():
                    print(f"{name} ")
                for credentials in display_credentials()
                    print(f "{pass_word}")       
                    print ("")
            else:
                print('\n')
                print("You dont seem to have any account yet")
                print('\n')

        elif short_code == 'fc':

            print("Enter the account you want to search for")

            search_name = input().lower()
            if check_existing_credentials(search_name):
                earch_contact = find_contact(search_number)
                print(f"account name : {search_credentials.account}")
                print('-' * 60)

                print(f"user name : {search_credentials.username}  password : {search_credentials.password}" )
                print('-' * 60)

            else:
                print("That credentials does not exist")


        elif short_code == "dd":
            print("Enter the account you want to delete")
            search_name = input().lower()
            if find_credential = find_credential(search_name)
                print("_"*40)
                save_credentials.delete_credentials()
                print(f"your credentials for : {search_credentials.aacount} successfuly deleted!!")
                print('\n')

            else :
                print("That Credential does not exit")
                    
        elif short_code == 'cp':
            print(" ")
            print("  To create a password, enter your name and account below")
            print(" ")
            list_of_inputs = [c for c in input()]
            list_of_inputs.reverse()
            print(list_of_inputs)
                    
        
        elif short_code == "lg":
            print('\n')
            print("*"*40)
            print("log in")
            print(f"welcome{username} to your credentials")
            print("-"*120)

            while True:
                print(''' choose a short code \n
                    cc - CREATE NEW CREDENTIALS
                    dc-  DISPLAY ACCOUNTS
                    fc - FIND A CREDENTIAL 
                    dd - DELETE A CREDENTIAL
                    cp - CREATE PASSWORD
                    lg - LOGIN IN TO ACCOUNT
                    ex - EXIT THE APPLICATION ''' )
                short_code = input().lower()
        
        elif short_code == "ex":
            print("-"*120)
            print(" ")
            print("Bye .......")
            print(" ")
            print("-"*120)
            break
         else:
            print("I really didn't get that. Please use the short codes")
    


    
if __name__ == '__main__':

    main()      