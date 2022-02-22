import unittest # Importing the unittest module
from password import User # Importing the password class
from credential import credentials # Importing the credential class


class TestUser(unittest.TestCase):

    def setUp(self):
      '''
      Set up method to run before each test cases.
      '''
      self.new_user = User("bint-den","password") # create contact object


    def test_init(self):
      '''
      test_init test case to test if the class has been initialized properly
      '''

      self.assertEqual(self.new_user.username, "bint-den")
      self.assertEqual(self.new_user.password,"password")
        
    
    def test_save_user(self):
        '''
        test_save_user test case to test if the new user is saved into
         the user list
        '''
        self.new_user.test_save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)


    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a contact from our user list
        '''
        self.new_user.save_user()
        test_user = User("bint-den","password")         
        test_user.save_user()

        self.new_user.delete_user()# Deleting a user object
        self.assertEqual(len(User.user_list),1)
    

class Testcredentials(unittest.TestCase):

    def setUp(self):
      '''
      Set up method to run before each test cases.
      '''
      self.new_credentials = credentials("bint-den","instagram","password") # create contact object

    
    def test_save_credentials(self):
        '''
        test_save_user test case to test if the new credentials is saved into
         the credentials list
        '''
        self.new_credentials.test_save_credentials() # saving the new credentials
        self.assertEqual(len(credentials.credentials_list),1)


    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        credentials.credentials_list = []


    def test_delete_credentials(self):
        '''
        test_delete_credentials to test if we can remove a credentials from our credentials list
        '''
        self.new_credentials.save_credentials()
        test_credentials = User("bint-den","password")         
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()# Deleting a credentials object
        self.assertEqual(len(credentials.credentials_list),1)


    def test_username_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the username.
        '''

        self.new_credentials.save_credentials()
        test_credentials= credentials("bintden",  "instagram","password") # new credentials
        test_credentials.save_credentials()

        credentials_exists = credentials.credentials_exist("bint-den")

        self.assertTrue(credentials_exists)
    
    
    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials been saved
        '''

        self.assertEqual(credentials.display_credentials(),credentials.credentials_list)    


    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credentials to check if we can save multiple credentials
            objects to our credentials_list
            '''
            self.new_credentials.save_credentials()
            test_multiple = credentials("bint-den","instagram","password") 
            test_multiple.save_credentials()
            self.assertEqual(len(credentials.credentials_list),2)


    def test_find_credentials_by_account(self):
        '''
        test to check if we can find a credentials by account and display information
        '''

        self.new_credentials.save_credentials()
        test_credentials = credentials("bint-den","instagram","password") 
        test_credentials.save_credentials()

        found_credentials= credentials.find_by_account("instagram")

        self.assertEqual(found_credentials.account,test_credentials.account)
        
    